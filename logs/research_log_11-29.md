Research Log – 11/29/2025

Tasks Completed
- Checked ICA after running overnight ~ 10 hours
- Found RuntimeWarning with fixed 45 components decided yesterday
- Noted variance and rank issues --
 {RuntimeWarning: Using n_components=45 (resulting in n_components_=45) may lead to an unstable mixing matrix estimation because the ratio between the largest (59) and smallest (4.5e-06) variances is too large (> 1e6); consider setting n_components=0.999999 or an integer <= 34}
- Reran ICA objects: Subject 11-149
- Pending 1-10
- Saved ICA objects for later inspection and application
- Switched from components to variance based selection again. This differs from yesterday because I'm using n_components = 0.9999 rather than .95

Progress Notes
- Checked to see if the saved objects can be loaded and inspected
- Gathered papers to study for the theory driven approach confirmed by Dr Cavanagh

Next Steps
- Study ICA component interpretation resources (videos, papers, methods tutorials) to formalize criteria for blink/muscle/noise rejection.
- Run ICA for subject 001-010
- Update methods
- Do artifact rejection for 3 subjects

