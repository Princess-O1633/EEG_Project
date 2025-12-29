import numpy as np
import matplotlib.pyplot as plt

# Load the PSD data
psd_file = r"rEEG\sub-001\data\sub-001_psd.npy"
psd_data = np.load(psd_file)  # shape might be (n_epochs, n_channels, n_freqs)

# Example: Plot PSD for the first epoch and first channel
epoch_idx = 50
channel_idx = 45

# Assuming you know the frequency axis (e.g., 0–125 Hz for fs=250 Hz and n_freqs=128)
freqs = np.linspace(0, 125, psd_data.shape[2])  # adjust according to your PSD

plt.figure(figsize=(8,4))
plt.plot(freqs, psd_data[epoch_idx, channel_idx, :])
plt.xlabel("Frequency (Hz)")
plt.ylabel("Power Spectral Density")
plt.title(f"PSD: Epoch {epoch_idx}, Channel {channel_idx}")
plt.show()
