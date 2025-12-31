Research Log - 12/30/25

Tasks Completed
Debugged the connectivity analysis pipeline:
    - Identified the “Zero Variance” error in previous t-test scripts caused by empty or triangular PLI matrices.
    - Implemented matrix symmetrization to ensure all channel pairs are accessible, handling both dense and triangular storage formats.
    - Added robust channel indexing with case-insensitive lookup to accommodate subject-specific electrode naming variations.
Refined channel selection strategy:
    - Transitioned from Fz–P3 to Fz–Oz for frontal–occipital connectivity, targeting cognitive biomarkers relevant to Parkinson’s Disease (PD).
Conducted statistical analysis:
    - Extracted Fz–Oz alpha-band PLI values for 50 PD subjects and 49 Healthy Controls (HC), skipping sub-121.
    - Performed independent samples t-test; found statistically significant increased alpha-band connectivity in PD (PD mean = 0.158, HC mean = 0.128, t = 2.227, p = 0.028).

Visualization:
- Generated box plots and stripplots for Fz–Oz alpha PLI, displaying individual subject data points and significance annotation.

Progress Notes
    - The Fz–Oz switch successfully revealed a significant biomarker for PD.
    - The increased alpha-band connectivity suggests potential pathological hypersynchrony or compensatory frontal mechanism.
    - The pipeline is now robust against matrix indexing errors and can handle missing/triangular data without crashing.

Next Steps
    - Run Fz–Oz analysis for beta-band to determine frequency specificity of hypersynchrony.
    - Investigate inter-hemispheric motor circuits (C3–C4 beta PLI) for PD-related disruptions.
    - Correlate Fz–Oz alpha PLI with clinical scores (MoCA/UPDRS) to validate clinical relevance.
    - Compute global mean PLI to ensure finding is circuit-specific rather than reflecting general whole-brain connectivity shifts.
    - Expand visualization with heatmaps of PD vs HC connectivity matrices for full-network context.


Task: Statistical analysis of ROI theta/alpha ratio in PD cohort
Methods: Aggregated ROI-level DWT features for theta and alpha bands across frontal, central, temporal, parietal, and occipital regions. Calculated theta/alpha ratio per ROI, then averaged across ROIs for each subject. PD subjects were split by MoCA score (<26 impaired, ≥26 unimpaired). Performed two-sample t-test and Pearson correlation with MoCA.

Results:
    - Total PD subjects with MoCA + ROI data: 100 (Impaired: 53, Unimpaired: 47)
    - Mean theta/alpha ratio: Impaired = 1.063 ± 0.637, Unimpaired = 0.740 ± 0.389
    - Group comparison: t = 3.063, p = 0.00291 → statistically significant
    - Correlation with MoCA: r = -0.467, p = 9.978×10⁻⁷ → significant negative correlation

Interpretation: Theta/alpha ratio is elevated in cognitively impaired PD subjects and negatively correlates with MoCA, consistent with theory-driven predictions and literature (e.g., The Increase of Theta Power and Decrease of Alpha/Theta Ratio as a Manifestation of Cognitive Impairment in Parkinson’s Disease; Longitudinal EEG changes correlate with cognitive measure deterioration in Parkinson's disease).

Next steps: Visualize ROI-wise distribution of theta/alpha ratio and explore other cognitive-related ratios (theta/beta, alpha/delta) for additional markers.

Reviewed literature on PD-MCI EEG biomarkers, focusing on narrowband microstate dynamics, spectral power, connectivity, and complexity measures.

Identified key narrowband frequency ranges for microstate analysis:

Delta (1–4 Hz)

Theta (4–8 Hz)

Alpha (8–13 Hz)

Defined microstate features to extract per band (MS-A → MS-D):

Coverage

Mean duration

Occurrence rate

Transition probabilities, including MS-D → MS-A, MS-A → MS-D, and self-transitions

Discussed importance of narrowband analysis versus broadband to avoid dopaminergic masking.

Outlined spectral power features correlated with cognitive status (MoCA):

Delta, theta, pre-alpha, alpha, beta, gamma power

Ratios: theta/alpha, slow/fast frequencies

Alpha reactivity

Reviewed LEAPD indices and LPC-derived oscillatory features; prioritized those with strongest MoCA correlations.

Defined region- and band-specific connectivity targets:

Theta: frontal–temporal (right-left, right-right)

Alpha: occipital–frontal (left-right, right-left)

Metrics: coherence, PLI, temporal variability

Compiled cross-feature coupling ideas (novel hypothesis testing):

Delta MS-A coverage × frontal delta power

Theta MS-D occurrence × frontal–central PLV

MS-D → MS-A transition × theta-band entropy

Drafted tiered testing plan:

Tier 1: narrowband microstates, spectral power/ratios, LEAPD

Tier 2: connectivity, temporal instability proxies

Tier 3: cross-feature coupling

Tier 4: optional microstate-conditioned power features

Developed and integrated Python code for:

Narrowband microstate extraction per subject

Temporal feature computation (coverage, duration, occurrence)

Transition probability computation

Optional label smoothing to remove short flickers

Batch processing across all subjects with CSV export

Posterior DPBF (P3/P4/Oz/O2/O1/POz/P2/P4)

Delta (1–4 Hz)

PD count: 100; Impaired: n=53 (mean=1.131), Unimpaired: n=47 (mean=1.101)

Group difference: t=1.507, p=0.138 → not significant

Correlation with MoCA: Pearson r=-0.034 (p=0.736), Spearman r=-0.016 (p=0.871)

Theta (4–8 Hz)

PD count: 100; Impaired mean=6.898, Unimpaired mean=7.249

Group difference: t=-1.436, p=0.154 → trend-level

Correlation with MoCA: Pearson r=0.248 (p=0.013), Spearman r=0.296 (p=0.003) → significant

Alpha (8–13 Hz)

PD count: 100; Impaired mean=8.713, Unimpaired mean=9.129

Group difference: t=-1.886, p=0.063 → trend-level

Correlation with MoCA: Pearson r=0.195 (p=0.052), Spearman r=0.233 (p=0.019) → moderate significance

Beta (13–30 Hz)

PD count: 100; Impaired mean=14.285, Unimpaired mean=14.334

Group difference: t=-0.116, p=0.908 → not significant

Correlation with MoCA: Pearson r=0.051 (p=0.614), Spearman r=0.069 (p=0.497)

Derived Ratios

Delta/Beta ratio

Impaired: mean=7.531, Unimpaired: mean=5.705

Group difference: t=1.788, p=0.077 → trend-level

Correlation with MoCA: Pearson r=-0.302, p=0.0023 → significant

Theta/Alpha ratio

Impaired: mean=1.063, Unimpaired: mean=0.740

Group difference: t=3.063, p=0.0029 → significant

Correlation with MoCA: Pearson r=-0.467, p<1e-6 → strong significance

Connectivity / PLI

Beta-band PLI (Fz-Oz)

Impaired: mean=0.104, Unimpaired: mean=0.112

Group difference: t=-2.619, p=0.010 → significant

Correlation with MoCA: Pearson r=0.240, p=0.016 → significant