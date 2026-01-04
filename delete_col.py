import pandas as pd

df = pd.read_csv("ML_Feature_Matrix.csv")

# Drop the last two columns (the empty sync features)
df = df.iloc[:, :-2]

df.to_csv("PD_features_clean.csv", index=False)

print("New shape:", df.shape)
print("Remaining columns:")
print(df.columns.tolist())
