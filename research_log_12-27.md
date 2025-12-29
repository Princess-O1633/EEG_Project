Research Log – 12/27/2025

Tasks Completed

- Finalized design decision to mass-compute phase-lag index (PLI) connectivity at full channel resolution across all subjects and canonical frequency bands (delta, theta, alpha, beta).
- Defined separation between data capture and theory-driven interpretation: all connectivity matrices will be extracted and stored now; only frontal–parietal theta/alpha connectivity will be tested in hypothesis-constrained analyses later.
- Established PLI as the primary phase-based connectivity metric due to its robustness to volume conduction and zero-lag coupling, making it suitable for long-range network integrity assessment in PD cognition.

Methods Justification – PLI Connectivity Extraction

PLI quantifies the consistency of non-zero phase-lag relationships between EEG signals, providing an index of true functional coupling that is less sensitive to common-source artifacts. Cognitive impairment in Parkinson’s disease has been repeatedly associated with disruption of large-scale control networks. Extracting full PLI matrices at the channel level allows later aggregation into anatomically defined circuits while avoiding premature feature selection.

Connectivity will be computed per frequency band and saved as channel × channel matrices for each subject. Interpretation will be based on hypotheses, while other bands and regions will remain as supporting physiological data only.

Will compute phase-based connectivity (PLV and PLI) across canonical bands: delta, theta, alpha, beta.

Alpha not split into alpha1/alpha2 to ensure reliable estimation of phase relationships given 4 s epochs.

Connectivity will be computed per channel and saved; ROI aggregation will be done later for theory-driven analysis.

Spectral coherence omitted for now because PLV/PLI capture phase synchronization more robustly and are widely used in PD cognition studies.