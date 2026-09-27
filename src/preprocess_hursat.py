from pathlib import Path
import numpy as np
import xarray as xr

data_dir = Path("data/raw/Hursat")
output_dir = Path("data/processed/hursat")
output_dir.mkdir(parents=True, exist_ok=True)

files = sorted(data_dir.glob("*.NC"))

print(f"Found {len(files)} HURSAT files")

for file in files:
    with xr.open_dataset(file) as ds:
        storm_name = ds.attrs.get("TC_name")
        storm_dir = output_dir / storm_name
        storm_dir.mkdir(parents=True, exist_ok=True)

        image = ds["IRWIN"].values[0]
        nan_mask = np.isnan(image)
        nan_count = int(np.count_nonzero(nan_mask))

        if nan_count == image.size:
            print(f"NaN values found: {nan_count}; replaced: 0 ({file.name})")
            print(f"Warning: Skipping {file.name}; all {nan_count} pixels are NaN.")
            continue

        if nan_count > 0:
            median_value = np.median(image[~nan_mask])
            image = np.where(nan_mask, median_value, image)

        print(f"NaN values found and replaced: {nan_count} ({file.name})")

        # Normalize brightness-temperature values to 0-1
        min_value = np.min(image)
        max_value = np.max(image)

        normalized = (image - min_value) / (max_value - min_value)

        output_file = storm_dir / f"{file.stem}.npy"
        np.save(output_file, normalized)

        print(f"Storm: {storm_name}")
        print(f"Input: {file.name}")
        print(f"Image shape: {normalized.shape}")
        print(f"Output: {output_file}")

    print("\nHURSAT preprocessing completed.")