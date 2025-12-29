import pandas as pd

for i in range (1,150):
    df = pd.read_csv(f"rEEG\sub-{i:03d}\data\sub-{i:03d}_DWT_band_energy.csv")

    # Group by band and compute mean and std
    bands = ["delta_energy", "theta_energy", "alpha_energy", "beta_energy"]
    summary = df[bands].agg(['mean','std'])
    print(summary)
