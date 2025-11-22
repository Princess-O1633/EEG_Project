Research Log – 11/21/2025 5-7:30pm

Tasks Completed 
- Implemented all preproccessing before epoching on subject 001 
- Loaded EEG dataset (sub-001_task-Rest_eeg.set) and checked channel info.
- Marked bad channels based on visual inspection.
- Set standard 10–20 montage.
- Re-referenced to common average.
- Applied bandpass filter (1–45 Hz) and notch filter (60 Hz).
- Resampled data to 250 Hz.
- Prepared data for ICA.
- Ran ICA and plotted components for manual artifact identification.

Progress Notes
- Ready to select artifacts ICs and apply ICA

Next Steps

- Identify and selects ICs corresponding to artifacts (eye blinks, muschle, heartbeat) for exclusion
- Apply ICA to remove selected artifact components
- Interpolate bad channels
- Epoch the data
- Feature Extraction