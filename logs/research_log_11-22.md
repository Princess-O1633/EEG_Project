Research Log – 11/22/2025

Tasks Completed
- Plotted preprocessed EEG data before ICA for visual inspection (raw traces + PSD).
- Set up and fitted ICA (n_components=20) on the dataset.
- Visualized ICA components and their topographies.
- Reviewed component properties (time series + PSD) for candidate artifact ICs [0, 3, 6, 13].
- Selected ICs to exclude ([0, 6]) corresponding to eye artifacts.
- Applied ICA to remove selected artifact components and generated cleaned EEG (raw_clean).
- Compared before/after ICA data visually with raw traces and PSD.
- Noted expected PSD drop in frontal electrodes due to eye artifact removal.

Progress Notes

- ICA successfully removed major eye artifacts; frontal low-frequency power decreased as expected.
- Overall signal shape largely preserved, indicating minimal distortion to other channels.
- Visual inspection confirms data is ready for further preprocessing steps or feature extraction.

Next Steps

- Identify and select ICs corresponding to all major artifacts (eye blinks, muscle activity, heartbeat, line noise) for exclusion.
- Apply ICA to remove the selected artifact components.
- Interpolate any remaining bad channels if needed.
- Epoch the cleaned EEG data for analysis.
- Extract features for ML and connectivity analysis 
- Quantitatively compare pre/post ICA data for artifact reduction (variance, PSD drop in affected channels)