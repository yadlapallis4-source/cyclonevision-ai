from pathlib import Path

import matplotlib.pyplot as plt
import xarray as xr


DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "raw" / "hursat"
OUTPUT_PATH = Path(__file__).resolve().parent.parent / "screenshots" / "hursat_irwin_example.png"


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
        irwin = dataset["IRWIN"].isel(htime=0)
        cyclone_name = dataset.attrs.get("TC_name", "Unknown cyclone")
        observation_time = str(dataset["htime"].values[0])

        figure, axis = plt.subplots(figsize=(8, 6))
        irwin.plot(ax=axis, x="lon", y="lat", cmap="gray")
        axis.set_xlabel("Longitude")
        axis.set_ylabel("Latitude")
        axis.set_title(f"{cyclone_name} IRWIN brightness temperature - {observation_time}")
        figure.tight_layout()
        figure.savefig(OUTPUT_PATH, dpi=150)
        plt.close(figure)


if __name__ == "__main__":
    main()
