from pathlib import Path

import xarray as xr

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw" / "Hursat"


def main() -> None:
    files = sorted(
        file_path
        for file_path in DATA_DIR.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".nc"
    )

    if not files:
        print(f"No NetCDF files found in {DATA_DIR}")
        return

    storms = {}
    all_wind_speeds = []

    for file_path in files:
        with xr.open_dataset(file_path) as dataset:
            storm_name = dataset.attrs.get("TC_name", "Unknown")
            wind_speeds = dataset["WindSpd"].values.reshape(-1).tolist()

        storm = storms.setdefault(storm_name, {"file_count": 0, "wind_speeds": []})
        storm["file_count"] += 1
        storm["wind_speeds"].extend(wind_speeds)
        all_wind_speeds.extend(wind_speeds)

    print("Wind Speed Ranges")
    print("=" * 40)

    for storm_name, storm in sorted(storms.items()):
        wind_speeds = storm["wind_speeds"]
        unique_wind_speeds = sorted(set(wind_speeds))
        mean_wind_speed = sum(wind_speeds) / len(wind_speeds)

        print(f"\nStorm: {storm_name}")
        print(f"Files: {storm['file_count']}")
        print(f"Minimum wind speed: {min(wind_speeds)}")
        print(f"Maximum wind speed: {max(wind_speeds)}")
        print(f"Mean wind speed: {mean_wind_speed}")
        print(f"Unique wind speeds: {unique_wind_speeds}")

    print("\nOverall Wind Speed Range")
    print(f"Minimum: {min(all_wind_speeds)}")
    print(f"Maximum: {max(all_wind_speeds)}")


if __name__ == "__main__":
    main()
