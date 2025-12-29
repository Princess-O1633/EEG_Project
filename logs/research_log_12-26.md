# Research Log - 12/26/25

Tasks Completed

- Computed Discrete Wavelet Transform (DWT) features for all subjects using broad canonical bands only (delta, theta, alpha, beta).
- Finalized spectral entropy feature extraction for all subjects and generated a combined mean summary file for the first 50 subjects.
- Evaluated spectral entropy as a potential predictor of cognitive impairment.
- Reviewed and extracted findings from “The Increase of Theta Power and Decrease of Alpha/Theta Ratio as a Manifestation of Cognitive Impairment in Parkinson’s Disease.”

Progress Notes

DWT band design
    - Alpha was not subdivided into alpha1 / alpha2 for DWT features due to limited frequency resolution at the chosen wavelet levels, which would lead to unstable or noisy sub-band estimates.
    - Alpha1 / alpha2 separation is preserved only in FFT / PSD features, where frequency resolution is well-defined.
    - This design reduces feature redundancy, limits overfitting risk, and preserves interpretability while maintaining complementary time–frequency information between FFT and DWT.

Wavelet level → frequency mapping (fs ≈ 250 Hz)

D3 → Beta (13–30 Hz)

D4 → Alpha (8–13 Hz)

D5 → Theta (4–8 Hz)

A5 → Delta (1–4 Hz)

D1–D2 ignored (high-frequency gamma / EMG noise).

Spectral entropy
    - Combined mean spectral entropy outputs across the first 50 subjects into a single dataset for quick sanity check analysis.
    - Preliminary analysis showed no meaningful correlation between spectral entropy and cognitive impairment metrics. Low entropy does not appear to be a reliable standalone biomarker in this cohort.

Clinical covariates
    - UPDRS score and age are statistically significantly correlated with  MoCA in the dataset.

Literature integration
Findings from Increase of Theta Power and Decrease of Alpha/Theta Ratio as a Manifestation of Cognitive Impairment in PD:
    - Theta power increased in PD-D vs PD-CogN (global, left temporal/occipital, right occipital).
    - Beta power decreased in PD-D.
    - Alpha/theta ratio globally decreased in PD-D (p = 0.001).
    - These results support prioritizing theta, beta, and alpha/theta-based features over spectral entropy.