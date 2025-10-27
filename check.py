# 10/26/2025 - Check EEG montage for 60 channels used in analysis (excluding Iz, I1, I2)
import mne
import matplotlib.pyplot as plt
import numpy as np

# Load the EEG file
raw = mne.io.read_raw_eeglab(r'rEEG/sub-001/eeg/sub-001_task-Rest_eeg.set', preload=True)

# Pick 60 channels used in analysis (exclude Iz, I1, I2)
channels_to_use = ['Fp1', 'Fz', 'F3', 'F7', 'FT9', 'FC5', 'FC1', 'C3', 'T7', 'TP9',
                   'CP5', 'CP1', 'P3', 'P7', 'O1', 'Oz', 'O2', 'P4', 'P8', 'TP10',
                   'CP6', 'CP2', 'Cz', 'C4', 'T8', 'FT10', 'FC6', 'FC2', 'F4', 'F8',
                   'Fp2', 'AF7', 'AF3', 'AFz', 'F1', 'F5', 'FT7', 'FC3', 'C1', 'C5',
                   'TP7', 'CP3', 'P1', 'P5', 'PO7', 'PO3', 'POz', 'PO4', 'PO8', 'P6',
                   'P2', 'CPz', 'CP4', 'TP8', 'C6', 'C2', 'FC4', 'FT8', 'F6', 'AF8',
                   'AF4', 'F2', 'FCz']
raw.pick_channels(channels_to_use)

# Plot the montages (2D and 3D)
raw.plot_sensors(show_names=True, kind='topomap', title='60-channel EEG Montage')
plt.show()
raw.plot_sensors(kind='3d', show_names=True, title='60-channel EEG Montage (3D)')
plt.show()
