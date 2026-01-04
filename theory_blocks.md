THEORY_BLOCKS = {

    # Executive hub breakdown in frontal cortex
    "Frontal_Control": [
        "Feature_HubPLI_Beta_Frontal",
        "Feature_Theta_Asymmetry_Idx",
        "Feature_Theta_Frontal_ROI_Abs",
        "Feature_PLI_Beta_F3P4"
    ],

    # Posterior compensatory recruitment
    "Posterior_Compensation": [
        "Feature_Gamma_Posterior_Abs",
        "Feature_HubPLI_Alpha_Posterior",
        "Feature_HubPLI_Beta_Posterior",
        "Feature_Delta_Functional_Strength_Posterior"
    ],

    # Cross-frequency coordination failure
    "CrossFreq_Dysregulation": [
        "Feature_ThetaAlpha_Global",
        "Feature_DeltaBeta_Global",
        "Feature_DPBF_Alpha",
        "Feature_ThetaAlpha_Peak_Freq",
        "Feature_DWT_Theta_over_alpha_frac"
    ],

    # Long-range network fragmentation
    "Network_Fragmentation": [
        "Feature_Network_FrontPost_Beta_PLI",
        "Feature_PLI_Beta_C3P3",
        "Feature_Sync_Delta_ClassA_Frontal",
        "Feature_Sync_Theta_ClassD_Central",
        "Feature_Theta_Temporal_Correlation"
    ],

    # Cognitive state instability (microstate / DWT dynamics)
    "Microstate_Instability": [
        "Feature_Instab_Alpha_duration_Var",
        "Feature_Instab_Delta_duration_Var",
        "Feature_Instab_Theta_duration_Var",
        "Feature_Instab_Alpha_occurrence_Var",
        "Feature_Instab_Delta_occurrence_Var",
        "Feature_Instab_Theta_occurrence_Var",
        "Feature_Instab_Alpha_coverage_CV",
        "Feature_Instab_Delta_coverage_CV",
        "Feature_Instab_Theta_coverage_CV",
        "Feature_DWT_Theta_energy_var"
    ]
}
