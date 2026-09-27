# CNN PoC Labeling Plan

## Current Dataset

- NOAA HURSAT-B1 Version 6
- 3 storms: IAN, ONE, SONAMU
- 30 total observations/files
- Available metadata includes `WindSpd`, `CentPrs`, observation time, satellite/source, and `eye_prob`.

## Important Decision

Do not use storm names (IAN, ONE, SONAMU) as CNN class labels. Doing so would make the model learn storm identity rather than cyclone characteristics.

## Candidate Label

Wind speed could be used as a basis for an initial intensity-related classification experiment. Appropriate meteorological thresholds must be verified before assigning intensity classes. The current project has not assigned final classes.

### Verified Wind Speed Metadata

The NOAA HURSAT-B1 NetCDF files define `WindSpd` as:

- **Variable:** `WindSpd`
- **Long name:** Wind Speed
- **Units:** knots
- **Valid range:** 0–200 knots

The current PoC dataset has observed `WindSpd` values from 13.2 to 20.0 knots. Final intensity classes have not been assigned.

The current dataset is too small for reliable model training or evaluation. No CNN training results or accuracy should be reported.

## Future Dataset Requirement

Additional tropical cyclone observations from multiple storms will be needed before a meaningful CNN classification experiment.

## Data Leakage Consideration

Multiple satellite files can represent the same storm at the same observation time. They must not be treated as independent storm states when creating training, validation, and test splits.

Storm-level splitting should be considered to evaluate generalization to unseen storms.
