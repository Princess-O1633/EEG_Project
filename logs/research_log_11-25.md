Research Log – 11/25/2025

Tasks Completed

- Created preprocess_all.ipynb to attempt batch preprocessing of EEG data prior to ICA.
- Noticed some subjects had very noisy time periods
- Observed that rereferencing appeared to amplify noise in some datasets.
- Revisited dataset paper and confirmed which channels should be removed: Pz (online reference), Iz, I1, and I2 (inconsistent across participants).

Observations / Notes

- Decided full channel removal may be preferable over interpolation for these problematic channels.
- Considering whether to attempt recovery of Pz as a reference or continue w/ common average reference for preprocessing.

Next Steps

- Decide referencing strategy (Pz vs. common average) for batch preprocessing.
- Adjust batch preprocessing pipeline based on channel removal decisions.
- Continue preparing data for ICA artifact removal.
- Adjust methods correspondingly