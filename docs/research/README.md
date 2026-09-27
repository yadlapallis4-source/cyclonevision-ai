## Initial HURSAT PoC Dataset Analysis

- **Dataset:** NOAA HURSAT-B1 Version 6
- **Storms:** IAN, ONE, SONAMU
- **Total files:** 30

| Storm | Wind speed | Central pressure |
| --- | --- | --- |
| IAN | 18.8–20.0 | 1002.0–1004.5 hPa |
| ONE | 13.2–17.6 | 1007.0–1010.0 hPa |
| SONAMU | 15.4–18.0 | 1006.67–1007.33 hPa |

Multiple satellite observations can exist at the same observation time.

The current dataset is a small proof-of-concept dataset and is not sufficient to claim reliable model performance.

### Labeling Consideration

For the initial CNN experiment, cyclone pattern/intensity labels must be defined using appropriate meteorological criteria rather than using storm names as class labels.
