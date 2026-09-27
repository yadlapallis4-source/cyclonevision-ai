from pathlib import Path

import xarray as xr


DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw" / "hursat"


def main() -> None:
    files = sorted(
        file_path
        for file_path in DATA_DIR.iterdir()
        if file_path.is_file() and file_path.suffix.lower() == ".nc"
    )

    if not files:
        raise FileNotFoundError(f"No NetCDF files found in {DATA_DIR}")

    file_path = files[0]

    with xr.open_dataset(file_path) as dataset:
        print(f"File name: {file_path.name}")
        print(f"Dataset dimensions: {dict(dataset.sizes)}")
        print(f"Variable names: {list(dataset.data_vars)}")
        print(f"Coordinate names: {list(dataset.coords)}")
        print("Basic dataset information:")
        print(dataset)


if __name__ == "__main__":
    main()
