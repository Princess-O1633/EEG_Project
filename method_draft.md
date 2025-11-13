# Methods Draft
Date: October 23,2025
Author: Princess Otegbulu
_________________________
1. Dataset

This study uses the OpenNeuro dataset ds004584 (version 1.0.0), which contains 64-channel EEG recordings collected during resting-state sessions under both eyes-open and eyes-closed conditions. The sampling rate is 500 Hz.
Subjects include individuals diagnosed with Parkinson’s disease (PD) and age-matched healthy controls, with both cognitively normal and cognitively impaired participants. The eyes-open resting-state condition is used as the primary analysis focus.

2. Experimental Groups

Participants are divided into four groups based on disease and cognitive status:

HC: Healthy controls without cognitive impairment

HC+CI: Healthy controls with cognitive impairment

PD: Parkinson’s disease without cognitive impairment

PD+CI: Parkinson’s disease with cognitive impairment

The primary classification task compares PD vs. HC, while a secondary stratified analysis considers all four groups to assess the impact of cognitive impairment on EEG patterns.

3. Preprocessing Pipeline

All preprocessing is conducted in MNE-Python. EEG signals are bandpass filtered from 1–45 Hz using a zero-phase FIR filter and a 60 Hz notch filter is applied to remove line noise. The data are resampled to 250 Hz to standardize frequency across participants.

The continuous data are segmented into 2-second epochs with 50% overlap to enhance feature stability. Epochs with amplitudes exceeding ±150 μV are rejected as artifacts. Channels exhibiting abnormal variance or flat signals are interpolated based on neighboring electrodes.

When needed, Independent Component Analysis (FastICA) retaining 95% of variance is applied to remove ocular or muscle artifacts. All EEG data are re-referenced to a common average before further analysis.

4. Feature Extraction

Two complementary feature domains are used to characterize EEG activity:

a. Frequency-domain analysis (FFT):
For each 2-second epoch, the Fast Fourier Transform (FFT) is computed to extract absolute and relative band powers across canonical frequency ranges:

Delta (1–4 Hz)

Theta (4–8 Hz)

Alpha (8–13 Hz)

Beta (13–30 Hz)

Gamma (30–45 Hz)

Features include total power, normalized power ratios, and band-power asymmetries across hemispheric electrode pairs. These are later averaged within regions of interest (frontal, temporal, parietal, occipital).

b. Time–frequency analysis (DWT):
The Discrete Wavelet Transform (DWT) provides temporal localization of oscillatory activity. Using a Daubechies (db4) mother wavelet, EEG signals are decomposed into five levels corresponding approximately to the traditional EEG bands. From each level, statistical descriptors (mean, variance, entropy, and energy) are extracted.

Both FFT- and DWT-based features are standardized (z-scored) and combined into a single feature matrix for downstream modeling.