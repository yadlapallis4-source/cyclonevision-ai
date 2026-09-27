from pathlib import Path

import xarray as xr

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw" / "Hursat"


def get_value(dataset: xr.Dataset, variable_name: str) -> object:
    values = dataset[variable_name].values
    if values.size == 1:
        return values[0]
    return values


def main() -> None:
    files = sorted(
        file_path
        for file_path in DATA_DIR.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".nc"
    )

    storms = {}

    for file_path in files:
        with xr.open_dataset(file_path) as dataset:
            storm_name = dataset.attrs.get("TC_name", "Unknown")
            filename_parts = file_path.stem.split(".")
            source = filename_parts[7] if len(filename_parts) > 7 else "Unknown"

            observation = {
                "file_name": file_path.name,
                "source": source,
                "time": get_value(dataset, "htime"),
                "wind_speed": get_value(dataset, "WindSpd"),
                "central_pressure": get_value(dataset, "CentPrs"),
                "eye_probability": (
                    get_value(dataset, "eye_prob")
                    if "eye_prob" in dataset
                    else "Not available"
                ),
            }
            storms.setdefault(storm_name, []).append(observation)

    print("HURSAT Label Metadata")
    print("=" * 60)

    if not files:
        print(f"No NetCDF files found in {DATA_DIR}")
        return

    for storm_name, observations in sorted(storms.items()):
        print(f"\nStorm: {storm_name}")
        print("-" * 60)

        for observation in observations:
            print(f"File: {observation['file_name']}")
            print(f"  Observation time: {observation['time']}")
            print(f"  Wind speed: {observation['wind_speed']}")
            print(f"  Central pressure: {observation['central_pressure']}")
            print(f"  Eye probability: {observation['eye_probability']}")
            print(f"  Satellite/source: {observation['source']}")


if __name__ == "__main__":
    main()
