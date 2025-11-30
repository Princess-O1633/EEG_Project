Research Log – 11/28/2025

Tasks Completed
- Completed Preproccesing prior to ICA for all remaining subject (068-149)
- Handled issues with subjects 68, 95, 113, 120, 137
- Decided to semi automate ICA artifact rejection
    - Choices: FastICA or Extended Infomax
    - FastICA * Computational Efficiency and Speed
    - Extended Infomax * Very Robust, Widely Used and Slower but Safer
- ICA Component Selection Issue

    During ICA preparation, I initially attempted to use a variance-based threshold (n_components=0.95) to automatically determine the effective dimensionality of each subject’s data. However, this produced unstable component counts (as low as 5) because several subjects had many interpolated channels (2–12) and multiple channels with extremely low variance. This reduced the estimated data rank (e.g., covariance rank ≈ 50), which caused the .95 variance criterion to collapse to an unrealistically small number of ICA components.

    After inspecting the channel variance report and SVD-based rank estimate, I determined that the data were consistently rank-deficient relative to the original 60 channels. Because the practical rank across subjects clustered near ~50-59, I selected a fixed ICA dimensionality of 45 components. This avoids overfitting to noisy rank estimates and keeps ICA stable across the full cohort while still capturing the major neural and artifact subspaces.

    This decision standardizes ICA across subjects and prevents failures due to rank variability introduced by interpolation, missing channels, or tiny-variance channels.
- Planning on running ICA on all subjects over night
