Research Log – 12/23/2025

Tasks Completed

- Plotted raw EEG data before ICA for visual inspection (all channels + PSD).
- Set up and fitted ICA on each subject.
- Visualized ICA components and their topographies.
- Reviewed component properties (time series + PSD) to identify candidate artifact ICs.
- Selected ICs for exclusion based on artifact type:
    - Eye artifacts (frontal, low-frequency)
    - EMG (broadband, 20–45 Hz, monotonic rise)
- Applied ICA to remove selected artifact components and generated cleaned EEG.
- Compared pre/post ICA data visually (raw traces + PSD).
Quantitatively checked ICA validity using:
    - 1/f slope
    - Alpha peak amplitude and frequency
    - Relative alpha power
    - Theta/Alpha ratio
Flagged unusable subjects (flatline recordings).

Progress Notes – Subject-Level
Subject 033
- 1/f slope: −0.14 → −0.64
- Alpha peak freq: 9.52 Hz → 9.52 Hz
- Relative alpha: 0.132 → 0.139
- Theta/Alpha: 1.14 → 1.12
Notes: ICA effectively removed broadband artifacts while preserving alpha.
EMG-heavy Subject 005
- 1/f slope: −0.73 → −1.31
- Alpha peak freq: 12.21 Hz → 8.30 Hz
- Alpha peak amplitude: 2.36e−11 → 6.18e−12
- Relative alpha: 0.236 → 0.267
- Theta/Alpha: 0.77 → 1.29
Notes: ICA removed neck EMG (ICA 0), steepened slope; peak frequency shift due to peak detection instability, not neural loss. Band-integrated alpha used for analysis.

Subject 121
- Raw EEG flat across all channels
- Notes: Unusable; excluded from analysis.

Subject w/ minor alpha shift
- 1/f slope: −1.36 → −1.19
- Alpha peak freq: 10.99 Hz → 9.89 Hz
- Relative alpha: 0.205 → 0.224
- Theta/Alpha: 1.09 → 1.05
Notes: Acceptable ICA; minor alpha shift, relative alpha improved.

