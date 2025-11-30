Research Log – 11/26/2025

Tasks Completed
- Reviewed paper "rEEG measures cognitive impairment in PD
- Understood Pz as an ONLINE reference
- Online reference -> single electrode for REAL-TIME recording, alr in the data. Reference signal is NOT displayed in the final data
- Explains why I can't find Pz electrode
- Removed Re-referencing of EEG to common average
- Redownloaded and organized all ".set" files from Subject 86-149 because of Runtime error w/ EEGLAB / file type
- Added code
    "if len(raw.annotations):
            mask = raw.annotations.description == 'boundary'
            if mask.any():
                raw.annotations.delete(mask)"
- Despite the data stated to be continous I wanted to be safe an adress MNE warning
    "RuntimeWarning: The data contains 'boundary' events, indicating data discontinuities. Be cautious of filtering and epoching around these events."
- Replied to Dr. Cavanagh's email