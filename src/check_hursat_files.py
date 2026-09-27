from pathlib import Path
import xarray as xr

data_dir = Path("data/raw/hursat")
files = sorted(data_dir.glob("*.NC"))

print(f"Found {len(files)} HURSAT files\n")

for file in files:
    with xr.open_dataset(file) as ds:
        print("=" * 60)
        print("File:", file.name)
        print("Storm:", ds.attrs.get("TC_name"))
        print("Time:", ds.htime.values)
        print("IRWIN shape:", ds["IRWIN"].shape)
        print("Wind speed:", ds["WindSpd"].values)