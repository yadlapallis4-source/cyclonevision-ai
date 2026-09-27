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

    file_path = files[0]
    with xr.open_dataset(file_path) as dataset:
        wind_speed = dataset["WindSpd"]
        related_global_attributes = {
            name: value
            for name, value in dataset.attrs.items()
            if any(term in name.lower() for term in ("wind", "intensity", "unit"))
        }

        print(f"File: {file_path.name}")
        print("\nWindSpd variable:")
        print(wind_speed)

        print("\nWindSpd attributes:")
        if wind_speed.attrs:
            for name, value in wind_speed.attrs.items():
                print(f"{name}: {value}")
        else:
            print("No attributes found.")

        print("\nRelevant dataset global attributes:")
        if related_global_attributes:
            for name, value in related_global_attributes.items():
                print(f"{name}: {value}")
        else:
            print("No wind-, intensity-, or unit-related global attributes found.")


if __name__ == "__main__":
    main()
