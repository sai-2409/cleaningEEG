### Importing path for the showing file's path easier
from pathlib import Path
# importing numpy library
import numpy as np

## importing mne library for displaying data using python
import mne, matplotlib.pyplot as plt
import os

# importing ica components
from mne.preprocessing import ICA, create_eog_epochs

# storing data's path into eeg_file variable
# eeg_file_path = Path("/Users/sai.laca/Desktop/cleaningEEG/data/")

# participant = int(input("Choose Participant by entering number between 1 to 34: "))
# eeg_file = eeg_file_path / f"{participant}.edf"

# Print selected file
# print("You selected:", eeg_file)

def cleaning(eegFile):

    # reading raw dataset
    raw = mne.io.read_raw_edf(str(eegFile), preload=True)

    # displaying raw data
    raw.plot(duration = 10,
            scalings = "auto",
            block = True,
            title = "Raw Data - Mark Bad Channels",
            )

    raw_cleaned = raw.copy()

    # excluding bad channels 
    badChannels = raw.info["bads"]
    goodChannels = mne.pick_types(raw.info, eeg = True, exclude = badChannels)


    raw_cleaned.notch_filter(freqs=[50], picks = goodChannels)
    raw_cleaned.filter(l_freq = 0.5, 
                       h_freq = 80.0, 
                       picks = goodChannels, 
                       method = "fir", 
                       phase = "zero", 
                       fir_window = "hamming",
                       )
    # referencing 
    raw_cleaned, _ = mne.set_eeg_reference(raw_cleaned, ref_channels='average')

    # applying ICA on a good referenced data
    icaPicks = mne.pick_types(raw_cleaned.info, eeg = True, exclude = badChannels)
    n_channels = len(icaPicks)
    ica = ICA(n_components=min(19, n_channels), random_state=97, max_iter="auto")
    ica.fit(raw_cleaned, picks = icaPicks)

    # eog_epochs = create_eog_epochs(raw_cleaned)  # if you have EOG or can infer blinks

    eog_picks = mne.pick_types(raw_cleaned.info, eog=True)

    if len(eog_picks) > 0:
        # if there is at least one EOG channel, we are looking for EOG component
        eog_inds, eog_scores = ica.find_bads_eog(raw_cleaned)
        ica.exclude = eog_inds
        print("Found EOG-related ICs:", eog_inds)
    else:
        # if not, just skip
        print("No EOG channels found – skipping find_bads_eog()")
        eog_inds, eog_scores = [], []

    ica.exclude = eog_inds

    # applying ica component back to raw_cleaned
    raw_cleaned = ica.apply(raw_cleaned)

    # bringing back bad channels and estimating their signals from their neighbors
    raw_cleaned.interpolate_bads(reset_bads = False)

    # rereferencing again after ICA and bringing back bad channels 
    raw_final, _ = mne.set_eeg_reference(raw_cleaned, ref_channels="average")



    # Printing raw data to the termnilal
    print(raw.info)
    print(raw_cleaned.info)
    print(raw.info["bads"])

    # Displaying the dataset
    raw_final.plot(duration = 10,
            scalings = "auto",
            event_color="green",
            block = False,
            
            title = "Cleaned Data",
            )

    # plt.show()