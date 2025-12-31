import glob
import os

# files = glob.glob(r"C:\Users\User\Documents\EEG_Project\rEEG\sub-*\data\*_pli.npy")
# print(f"Deleting {len(files)} files")

# for f in files:
#     os.remove(f)


BASE_DIR = r"C:\Users\User\Documents\EEG_Project\rEEG"

# Find all DPBF CSV files across subjects
files = glob.glob(os.path.join(BASE_DIR, "sub-*", "*_DPBF.csv"))
print(f"Deleting {len(files)} files")

for f in files:
    os.remove(f)


for f in files:
    os.remove(f)