BEGIN
    LOAD raw EEG for each subject
    RE-REFERENCE to common average
    APPLY bandpass filter (1–45 Hz)
    APPLY notch filter (60 Hz)
    RESAMPLE to 250 Hz
    REMOVE bad channels (automatic + manual)
    RUN ICA or artifact subspace removal for EOG/EMG artifacts
    EPOCH data into 2-second segments with 50% overlap
    DISCARD epochs with amplitude > threshold

    FOR each epoch:
        COMPUTE FFT power in delta, theta, alpha, beta, gamma bands
        COMPUTE relative band power
        COMPUTE PSD features
        COMPUTE DWT coefficients (db4) up to level 5
        COMPUTE DWT energy + entropy
        COMPUTE connectivity measures (coherence/PLI) for ROI pairs
    END FOR

    AGGREGATE features per subject (mean/median across epochs)
    NORMALIZE features (z-score)

    PERFORM feature selection:
        univariate tests (ANOVA)
        recursive feature elimination
        LASSO to finalize feature set

    SPLIT dataset using stratified 5-fold CV
    FOR each model (LR, SVM, RF, XGBoost):
        TRAIN using inner hyperparameter search
        EVALUATE on outer fold
        SAVE metrics (AUC, F1, BA)
    END FOR

    APPLY explainable-AI analyses:
        CALCULATE permutation feature importance
        COMPUTE SHAP values for top models
        GENERATE global summaries + subject-level explanations

    COMPUTE permutation test (1000 perm)
    COMPUTE bootstrap CI
    PRODUCE plots (ROC, confusion matrix, feature importance)
END
