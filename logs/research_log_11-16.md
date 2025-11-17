Research Log – 11/16/2025

Tasks Completed

- Finalized full preprocessing pseudocode for the EEG pipeline.
- Verified the final order of preprocessing steps (filter → notch → 
common average reference → resample → bad channels → ICA → epoching → rejection).
- Wrote out the full Methods pseudocode for the project.
- Designed the complete methods workflow structure for the future figure (methods_flowchart.png).
- Built simple box structures for modeling and XAI sections.
- Cleaned and aligned feature extraction + feature selection text with pseudocode.
- Prepared the modeling task breakdown (PD vs HC, CI vs non-CI, PD-CI vs PD-NCI).

Progress Notes

- The pseudocode is now fully aligned with the written methods text and ready to convert into implementation.
- The flowchart will directly plug into the paper, science fair poster, and slides.
- Preprocessing implementation for the first subject is queued next.

Next Steps

- Implement full preprocessing on one subject end-to-end.
- Verify each step visually (PSD before/after, 
ICA components, epoch distributions).
- Once validated, scale to all subjects.