Research Log - Methods Justification for 4‑Second Epochs
Date: 12/25/2025 🎄

Context: Originally, my pipeline used 2‑second epochs with 50% overlap for PSD and connectivity extraction following a common precedent in EEG literature and in my own initial protocols. However, after rereading “Electroencephalography‑based machine learning for cognitive profiling in Parkinson’s disease” where preprocessing included 4‑second epoch segmentation, I realized a mismatch between the methods of current PD cognition EEG papers and the assumptions behind my feature extraction strategy.

The paper explicitly said:

“Finally, a 4‑second epoch segmentation was performed… Only plots with at least 20 segments of 4 seconds at the end of preprocessing were kept for further analysis.” (this situates 4‑second windows as the preprocessing standard for their PSD features).

This has two implications:
    1. PD cognitive resting EEG studies may prefer longer epoch windows (4 s) to improve frequency resolution and feature stability, and
    2. my original 2 s epoch strategy was not actually derived from methods in cognition‑focused PD EEG, but from general EEG workflows.

Physiological / methodological justification
In resting EEG, the oscillations of interest for cognition (especially in PD) — theta (4–8 Hz) and alpha (8–12 Hz) — occupy low frequencies where spectral estimation variance is large with short windows. EEG signals are quasi‑stationary over several seconds, meaning longer windows can capture stable rhythms without sacrificing stationarity. 

Key methodological reviews on EEG epoching notes:
    - Quasi‑stationarity over multi‑second windows is reasonable. 
    - Connectivity reliability depends on epoch length and should be considered carefully. 
    - Longer windows (≥4 s) are generally recommended for phase‑based measures in the low frequency range. 

Literature support:
- Quasi‑stationarity over multi-second windows is reasonable (PMC6200063). 
- Phase-based connectivity reliability improves with longer epochs (ResearchGate 2021).
- Longer windows (≥4 s) are recommended for low-frequency connectivity measures.

Even non-PD-specific EEG studies show that absolute and relative power over 4 s epochs produces lower coefficient of variation, indicating more stable spectral estimates relevant to cognitive markers.
Connectivity-specific caution

My attempt to compute PLI connectivity with only 2.0 s windows triggered a runtime warning from MNE:

    " RuntimeWarning: fmin=1.000 Hz corresponds to 2.004 < 5 cycles based on the epoch length 2.004 sec,
    need at least 5.000 sec epochs or fmin=2.495. Spectrum estimate will be unreliable. "