Research Log - 12/3/2025 and 12/4/2025
- Researched automatic ICA artifact labeling tools w/out EOG/ECG reference signal
- Decided against using find_bads_eog w/ Frontal channels as prozy EOG
- Reviewed multiple ICA components (e.g., IC047, IC050, IC018, IC019) with their:
    -Topographies
    -Segment variance plots
    -Power spectra
    -ERP/ERP images
- Identified IC019 visually as a strong muscle candidate (frontal/temporal hotspot, irregular time series, elevated high-frequency tail).
- Attempted to automate Muscle detection using MNE function
- Original custom computation of band ratio produced nan: Warning: Mean of empty slice
    - Caused by the 45 Hz low-pass filter, leaving too few (or zero) PSD bins >20 Hz.
    - This does not invalidate muscle detection; it only breaks the custom metric.
- Developed Kurtosis and Z score metrics to flag especially noisy, burst, irregular ICA components linked to muscle
- LP at 45 Hz restricts high-frequency analysis.
Band-ratio metrics above ~20 Hz become unreliable. However, using a higher low-pass cutoff would also reintroduce heavy EMG contamination above ~40 Hz, degrading ICA stability and reducing the reliability of downstream PD-relevant features.
- Unfiltered or higher LP cutoff would give more interpretable muscle spectral signatures.