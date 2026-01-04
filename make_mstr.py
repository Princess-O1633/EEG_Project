# # import os
# # import numpy as np
# # import pandas as pd

# # # -------------------------------
# # # Configuration
# # # -------------------------------
# # BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"
# # INPUT_MATRIX = "ML_Feature_Matrix.csv"
# # TARGET_CH = ['F3', 'F4', 'Fz', 'F5', 'F1', 'F2', 'AF3', 'AF4', 'AFz']
# # TARGET_UPPER = [ch.upper() for ch in TARGET_CH]
# # THETA_COL = 'theta_abs'

# # # -------------------------------
# # # Update ML Matrix
# # # -------------------------------
# # if not os.path.exists(INPUT_MATRIX):
# #     print(f"Error: {INPUT_MATRIX} not found.")
# # else:
# #     master_df = pd.read_csv(INPUT_MATRIX)
# #     frontal_theta_vals = []

# #     print(f"Extracting Frontal ROI Theta ({len(TARGET_CH)} channels)...")

# #     for subj in master_df['participant_id']:
# #         csv_file = os.path.join(BASE_DIR, subj, "data", f"{subj}_bandpowers_epoch.csv")
        
# #         if os.path.exists(csv_file):
# #             df = pd.read_csv(csv_file)
# #             df['channel_clean'] = df['channel'].str.strip().str.upper()
            
# #             # Filter for the specific Frontal ROI
# #             matched_chs = df.loc[df['channel_clean'].isin(TARGET_UPPER)]
            
# #             if not matched_chs.empty:
# #                 frontal_theta_vals.append(matched_chs[THETA_COL].mean())
# #             else:
# #                 frontal_theta_vals.append(np.nan)
# #         else:
# #             frontal_theta_vals.append(np.nan)

# #     # Append new feature
# #     master_df['Feature_Theta_Frontal_ROI_Abs'] = frontal_theta_vals

# #     # Save final matrix
# #     master_df.to_csv(INPUT_MATRIX, index=False)
# #     print("Done! Added Feature_Theta_Frontal_ROI_Abs.")
# import os
# import pandas as pd

# # -------------------------------
# # Configuration
# # -------------------------------
# BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"
# INPUT_MATRIX = "ML_Feature_Matrix.csv"
# PEAK_SUMMARY_CSV = os.path.join(BASE_DIR, "theta_alpha_peak_freq.csv")

# # -------------------------------
# # Update ML Matrix
# # -------------------------------
# if not os.path.exists(INPUT_MATRIX):
#     print(f"Error: {INPUT_MATRIX} not found.")
# elif not os.path.exists(PEAK_SUMMARY_CSV):
#     print(f"Error: {PEAK_SUMMARY_CSV} not found. Run the peak computation script first.")
# else:
#     # Load both dataframes
#     master_df = pd.read_csv(INPUT_MATRIX)
#     peak_df = pd.read_csv(PEAK_SUMMARY_CSV)

#     # Clean participant IDs just in case
#     master_df['participant_id'] = master_df['participant_id'].str.strip()
#     peak_df['participant_id'] = peak_df['participant_id'].str.strip()

#     # Merge the peak frequency column
#     # We use a left join to keep all subjects in the master matrix
#     master_df = master_df.merge(
#         peak_df[['participant_id', 'theta_alpha_peak_freq']], 
#         on='participant_id', 
#         how='left'
#     )

#     # Rename to follow our 'Feature_' naming convention
#     master_df.rename(columns={'theta_alpha_peak_freq': 'Feature_ThetaAlpha_Peak_Freq'}, inplace=True)

#     # Save final matrix
#     master_df.to_csv(INPUT_MATRIX, index=False)
#     print("Successfully added Feature_ThetaAlpha_Peak_Freq to the ML matrix.")
#     print(master_df[['participant_id', 'Feature_ThetaAlpha_Peak_Freq']].head())
# import os
# import numpy as np
# import pandas as pd

# -------------------------------
# Configuration
# -------------------------------
# BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"
# INPUT_MATRIX = "ML_Feature_Matrix.csv"
# GAMMA_CH = ['P3','P4','Oz','O2','O1','POz','PO7','PO8']
# GAMMA_UPPER = [ch.upper() for ch in GAMMA_CH]
# GAMMA_COL = 'high_beta_low_gamma_abs'

# # -------------------------------
# # Update ML Matrix
# # -------------------------------
# if not os.path.exists(INPUT_MATRIX):
#     print(f"Error: {INPUT_MATRIX} not found.")
# else:
#     master_df = pd.read_csv(INPUT_MATRIX)
#     gamma_vals = []

#     print(f"Extracting Posterior High Beta/Low Gamma ({len(GAMMA_CH)} channels)...")

#     for subj in master_df['participant_id']:
#         csv_file = os.path.join(BASE_DIR, subj, "data", f"{subj}_bandpowers_epoch.csv")
        
#         if os.path.exists(csv_file):
#             df = pd.read_csv(csv_file)
#             df['channel_clean'] = df['channel'].str.strip().str.upper()
            
#             # Filter for the Posterior ROI
#             matched_chs = df.loc[df['channel_clean'].isin(GAMMA_UPPER)]
            
#             if not matched_chs.empty and GAMMA_COL in matched_chs.columns:
#                 gamma_vals.append(matched_chs[GAMMA_COL].mean())
#             else:
#                 gamma_vals.append(np.nan)
#         else:
#             gamma_vals.append(np.nan)

# #     # Append new feature
# #     master_df['Feature_Gamma_Posterior_Abs'] = gamma_vals

# #     # Save final matrix
# #     master_df.to_csv(INPUT_MATRIX, index=False)
# #     print("Done! Added Feature_Gamma_Posterior_Abs.")
# #     print(master_df[['participant_id', 'Feature_Gamma_Posterior_Abs']].head())
# import os
# import pandas as pd
# import numpy as np

# # -------------------------------
# # Configuration
# # -------------------------------
# BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"
# INPUT_MATRIX = "ML_Feature_Matrix.csv"
# WINDOW_FOLDER = "data"

# # -------------------------------
# # Feature Extraction (Theta Temporal Corr Only)
# # -------------------------------
# def compute_temporal_corr(pli_windows):
#     n_win = pli_windows.shape[0]
#     if n_win < 2:
#         return np.nan
#     corrs = []
#     for i in range(n_win - 1):
#         v1 = pli_windows[i].flatten()
#         v2 = pli_windows[i + 1].flatten()
#         if np.std(v1) == 0 or np.std(v2) == 0:
#             continue
#         corrs.append(np.corrcoef(v1, v2)[0, 1])
#     return np.mean(corrs) if corrs else np.nan

# # -------------------------------
# # Update ML Matrix
# # -------------------------------
# if not os.path.exists(INPUT_MATRIX):
#     print(f"Error: {INPUT_MATRIX} not found.")
# else:
#     master_df = pd.read_csv(INPUT_MATRIX)
#     theta_temp_corr_vals = []

#     print("Extracting Theta Temporal Correlation (Dynamic Connectivity)...")

#     for subj in master_df['participant_id']:
#         pli_file = os.path.join(BASE_DIR, subj, WINDOW_FOLDER, f"{subj}_theta_pli_windows.npy")
        
#         if os.path.exists(pli_file):
#             try:
#                 pli_windows = np.load(pli_file)
#                 val = compute_temporal_corr(pli_windows)
#                 theta_temp_corr_vals.append(val)
#             except Exception as e:
#                 theta_temp_corr_vals.append(np.nan)
#         else:
#             theta_temp_corr_vals.append(np.nan)

#     # Append to matrix
#     master_df['Feature_Theta_Temporal_Correlation'] = theta_temp_corr_vals

#     # Save
#     master_df.to_csv(INPUT_MATRIX, index=False)
#     print("Done! Added Feature_Theta_Temporal_Correlation.")
#     print(master_df[['participant_id', 'Feature_Theta_Temporal_Correlation']].head())

# import os
# import numpy as np
# import pandas as pd
# import mne

# # =========================
# # CONFIGURATION
# # =========================
# BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"
# INPUT_MATRIX = r"C:\Users\User\Documents\EEG_Project\ML_Feature_Matrix.csv"
# TEMPLATE_PATH = os.path.join(BASE_DIR, "microstate_templates.npy")

# # These are your "Discovery" features with the highest statistical significance
# TEST_CASES = [
#     {
#         'label': 'Sync_Delta_ClassA_Frontal', 
#         'class_idx': 0, 
#         'freq': (1, 4), 
#         'electrodes': ['FZ', 'F3', 'F4', 'FP1', 'FP2']
#     },
#     {
#         'label': 'Sync_Theta_ClassD_Central', 
#         'class_idx': 3, 
#         'freq': (4, 8), 
#         'electrodes': ['CZ', 'C3', 'C4']
#     }
# ]

# # =========================
# # EXECUTION
# # =========================
# if not os.path.exists(TEMPLATE_PATH):
#     print(f"ERROR: {TEMPLATE_PATH} not found. Ensure you saved your templates in the previous step.")
# elif not os.path.exists(INPUT_MATRIX):
#     print(f"ERROR: {INPUT_MATRIX} not found. Ensure your master matrix exists.")
# else:
#     # 1. Load the Brain State Templates (Maps)
#     global_templates = np.load(TEMPLATE_PATH)
#     # Pre-normalize templates for faster spatial correlation
#     norm_templates = global_templates / (np.linalg.norm(global_templates, axis=1, keepdims=True) + 1e-12)
    
#     # 2. Load the Master Matrix
#     master_df = pd.read_csv(INPUT_MATRIX)
    
#     # Initialize lists to hold our new features
#     feature_data = {f"Feature_{test['label']}": [] for test in TEST_CASES}

#     print("Starting Subject-by-Subject Synchronization Extraction...")

#     for subj in master_df['participant_id']:
#         # Construct path using the sub-XXX naming convention
#         subj_num = subj.split('-')[-1]
#         epo_path = os.path.join(BASE_DIR, subj, f"epo_{subj_num}_raw.fif")
        
#         if not os.path.exists(epo_path):
#             for test in TEST_CASES:
#                 feature_data[f"Feature_{test['label']}"].append(np.nan)
#             continue

#         try:
#             # Load subject epochs
#             epochs = mne.read_epochs(epo_path, preload=True, verbose=False)
#             ch_names = [c.upper() for c in epochs.ch_names]
            
#             for test in TEST_CASES:
#                 # A. Filter data for the specific band
#                 filt_data = epochs.copy().filter(test['freq'][0], test['freq'][1], verbose=False).get_data(copy=False)
#                 # Flatten to (n_channels, n_timepoints)
#                 flat_data = filt_data.transpose(1, 0, 2).reshape(len(ch_names), -1)
                
#                 # B. Spatial Backfitting (assign each timepoint to a class)
#                 data_zero = flat_data - flat_data.mean(axis=0, keepdims=True)
#                 data_norm = data_zero / (np.linalg.norm(data_zero, axis=0, keepdims=True) + 1e-12)
#                 labels = np.argmax(np.abs(np.dot(norm_templates, data_norm)), axis=0)
                
#                 # C. Calculate Synchronization (Regional GFP during that class)
#                 target_mask = (labels == test['class_idx'])
#                 region_idx = [ch_names.index(c) for c in test['electrodes'] if c in ch_names]
                
#                 if np.any(target_mask) and region_idx:
#                     # Regional GFP is the standard deviation across selected electrodes
#                     regional_sync = np.mean(np.std(flat_data[region_idx, :][:, target_mask], axis=0))
#                     feature_data[f"Feature_{test['label']}"].append(regional_sync)
#                 else:
#                     feature_data[f"Feature_{test['label']}"].append(np.nan)
                    
#         except Exception as e:
#             print(f"Error processing {subj}: {e}")
#             for test in TEST_CASES:
#                 feature_data[f"Feature_{test['label']}"].append(np.nan)

#     # 3. Append new columns to the matrix
#     for feat_name, values in feature_data.items():
#         master_df[feat_name] = values

#     # 4. Save Final Matrix
#     master_df.to_csv(INPUT_MATRIX, index=False)
#     print("\nSUCCESS: Significant Microstate Features added to ML_Feature_Matrix.csv")
#     print(f"Added: {list(feature_data.keys())}")
import os
import pandas as pd
import numpy as np

# =========================
# CONFIGURATION
# =========================
BASE_DIR = r"C:\Users\User\Documents\EEG_Project"
INPUT_MATRIX = os.path.join(BASE_DIR, "ML_Feature_Matrix.csv")
INSTABILITY_FILE = os.path.join(BASE_DIR, "microstate_temporal_instability.csv")

# The features you want to include
FEATURES_TO_ADD = ["MS_duration_variance", "MS_occurrence_variance", "MS_coverage_CV"]
BANDS_TO_ADD = ["delta", "theta", "alpha"]

# =========================
# PROCESSING
# =========================
if not os.path.exists(INSTABILITY_FILE):
    print(f"Error: {INSTABILITY_FILE} not found. Please ensure the CSV exists.")
elif not os.path.exists(INPUT_MATRIX):
    print(f"Error: {INPUT_MATRIX} not found.")
else:
    # 1. Load data
    master_df = pd.read_csv(INPUT_MATRIX)
    instab_df = pd.read_csv(INSTABILITY_FILE)

    # Standardize subject IDs for a clean merge
    master_df['participant_id'] = master_df['participant_id'].astype(str).str.strip()
    instab_df['subject'] = instab_df['subject'].astype(str).str.strip()

    # 2. Pivot the instability data
    # This transforms the data from "long" (one row per band) to "wide" (one row per subject)
    pivot_df = instab_df.pivot(index='subject', columns='band', values=FEATURES_TO_ADD)
    
    # Flatten multi-level columns: e.g., ('MS_duration_variance', 'delta') -> 'Feature_Instability_Delta_DurVar'
    new_cols = []
    for feat, band in pivot_df.columns:
        if band in BANDS_TO_ADD:
            # Shorten names for the ML matrix
            short_feat = feat.replace("MS_", "").replace("variance", "Var")
            new_cols.append(f"Feature_Instab_{band.capitalize()}_{short_feat}")
        else:
            new_cols.append(f"DROP_{feat}_{band}") # Mark for removal
            
    pivot_df.columns = new_cols
    pivot_df = pivot_df[[c for c in pivot_df.columns if not c.startswith("DROP")]]
    pivot_df.reset_index(inplace=True)

    # 3. Merge into Master Matrix
    final_df = master_df.merge(pivot_df, left_on='participant_id', right_on='subject', how='left')
    
    # Drop redundant subject column from merge
    if 'subject' in final_df.columns:
        final_df.drop(columns=['subject'], inplace=True)

    # 4. Final Cleanup (Fill missing values with median if necessary)
    # Random Forest can handle NaNs, but it's good practice to check
    # final_df.fillna(final_df.median(), inplace=True)

    # 5. Save
    final_df.to_csv(INPUT_MATRIX, index=False)
    
    print("SUCCESS: Microstate Instability features added.")
    print(f"New features integrated: {[c for c in final_df.columns if 'Instab' in c]}")
    print(f"Final Matrix Shape: {final_df.shape}")