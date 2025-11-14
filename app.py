### Importing path for the showing file's path easier
from pathlib import Path

## importing mne library for displaying data using python
import mne, matplotlib.pyplot as plt
import os

# storing data's path into eeg_file variable
eeg_file = Path("/Users/sai.laca/Desktop/cleaningEEG/data/1.edf")

# participant = int(input("Choose Participant by entering number between 1 to 34: "))

# reading raw dataset
raw = mne.io.read_raw_edf(str(eeg_file), preload=True)

raw_cleaned = raw.copy()

raw_cleaned.notch_filter(freqs=[50])
raw_cleaned.filter(l_freq = 0.5, h_freq = 80.0, picks = "eeg", method = "fir", phase = "zero", fir_window = "hamming")

# Printing raw data to the termnilal
print(raw.info)
print(raw_cleaned.info)

# Displaying the dataset
raw.plot(duration = 10,
        scalings = "auto",
        block = False)
raw_cleaned.plot(duration = 10,
        scalings = "auto",
        event_color="green",
        block = False)
plt.show()