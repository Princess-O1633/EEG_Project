Research Log – 12/22/2025 (~5+ hours)

Tasks Completed
- Applied batch epoching to subjects 50–150; identified some subjects needing redo.
- Validated ICA on problematic subjects.
- Developed scripts to validate ICA artifact rejection:
- 1/f slope computation script to quantify broadband artifact removal (EMG, eye movement).
- Occipital alpha power script to extract PSD and alpha peak before/after ICA.
- Alpha integrity script computing peak frequency, relative alpha power, and theta/alpha ratio.
- Implemented per-subject and batch epoching scripts, saving cleaned epochs in corresponding subject folders.
- Saved plots showing:
    -PSD shape preservation after ICA
    -Effective removal of EMG and eye movement noise
    -Maintenance of alpha oscillatory structure
- Recorded quantitative metrics for each subject (1/f slope, alpha peak, relative alpha, theta/alpha ratio) for ICA validation.

Progress Notes
- Scripts allow systematic QC of ICA artifact removal across all subjects.
- PSD comparisons show successful removal of artifacts while preserving physiologically meaningful alpha.
- Batch and per-subject epoching scripts streamline preprocessing and ensure outputs are organized.

Next Steps

- Continue applying ICA validation scripts on remaining subjects.
- Document all metrics in research log per subject.
- Epoch cleaned data for analysis and feature extraction.
- Refine scripts if needed to automate alpha integrity checks for EMG-heavy subjects.