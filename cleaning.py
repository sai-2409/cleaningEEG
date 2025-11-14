# import os
# import tkinter as tk
# from tkinter import filedialog

# import matplotlib
# matplotlib.use('TkAgg')

# import mne
# import matplotlib.pyplot as plt
# import numpy as np

# root = tk.Tk()
# root.withdraw()

# # For all functions, the arguments aren't really needed because everything is global and the functions are in the same file, 
# # but the arguements will stay for the option to move these functions to a separate file
# def getFilePath():
#     while(True):
#         file_name = filedialog.askopenfilename()
#         file_root, file_extension = os.path.splitext(file_name)
#         # file path is not necessary because .plot works with the name
#         #file_path = os.path.abspath(file_name)
#         if (file_extension.lower() == '.edf'):
#             return file_name
        
# def filterData(raw):
#     if (input('Do you want to filter? Yes or no: ').lower() != 'yes'):
#         return False
#     l_freq = float(input('Input the lower bound for the cutoff frequency: '))
#     h_freq = float(input('Input the upper bound for the cutoff frequency: '))
#     # Right now we are assuming it is European data because .edf
#     # so notch filter will exclude
#     raw.filter(l_freq=l_freq, h_freq=h_freq, fir_design='firwin')
#     raw.notch_filter(freqs=50, picks='eeg', fir_design='firwin')
#     return True

# def reReferenceData(raw):
#     if (input('Do you want to Re-reference? Yes or no: ').lower() != 'yes'):
#         return False
#     while (True):
#         channelNames = raw.ch_names
#         print('How do you want to Re-reference?')
#         print('   1. Use A1 and A2 channels')
#         print('   2. Use Cz electrode as a reference')
#         print('   3. Average the signal from all electrodes')
#         option = int(input('Enter the number corresponding to your choice: '))

#         print('\n')

#         if (option == 1):
#             channelToCheck1 = 'A1'
#             channelToCheck2 = 'A2'
#             if (channelToCheck1 in channelNames and channelToCheck2 in channelNames):
#                 raw.set_eeg_reference(ref_channels=['A1', 'A2'])
#                 break
#             print('\nChannels doesn\'t exist\n')
#             continue
#         if (option == 2):
#             channelToCheck1 = 'Cz'
#             if (channelToCheck1 in channelNames):
#                 raw.set_eeg_reference()
#                 break
#             print('\nChannel missing\n')
#             continue
#         if (option == 3):
#             raw.set_eeg_reference("average", projection=True)
#             # print('Info: ', raw.info["projs"])
#             raw.apply_proj()
#             break
#         print('\n-Invalid Choice! Please try again-\n\n')
#     return True


# def showEDFData(duration, filter, reReference):
#     raw.plot(
#         duration=float(duration),
#         bad_color = 'red',
#         scalings='auto',
#         title='EEG data',
#         time_format='clock',
#         picks=mne.pick_types(raw.info, eeg=True, exclude='bads')
#     )        
    
#     if (filter):
#         rawBefore.plot(
#             duration=float(duration),
#             bad_color='red',
#             scalings='auto',
#             title='Unfiltered EEG data',
#             time_format='clock',
#         )
#         if (reReference):
#             rawFilter.plot(
#                 duration=float(duration),
#                 bad_color='red',
#                 scalings='auto',
#                 title='Filtered EEG data',
#                 time_format='clock',
#                 picks= mne.pick_types(raw.info, eeg=True, exclude='bads')
#             )
    
#     plt.show()




# # Start of Executed Code

# # Pick .edf file
# file_name = getFilePath()

# # Load file and determine duration
# raw = mne.io.read_raw_edf(file_name, preload=True)
# rawBefore = raw.copy()
# duration = input('Input the duration of the EEG data to view: ')
# filter = False
# reReference = False

# # Plot unfiltered data and you can mark bad channels
# showEDFData(duration, filter, reReference)
# # Option to filter data
# filter = filterData(raw)
# rawFilter = raw.copy()
# if (filter):
#     reReference = reReferenceData(raw)
# # Replot data but now it's possibly filtered and/or has removed bad channels
# showEDFData(duration, filter, reReference)