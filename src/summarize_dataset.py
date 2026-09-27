from pathlib import Path
import numpy as np

data_dir = Path("data/processed/hursat")
total_images = 0

print("Dataset Summary")
print("=" * 24)

for storm_dir in sorted(data_dir.iterdir()):
    if not storm_dir.is_dir():
        continue

    files = sorted(storm_dir.glob("*.npy"))
    if not files:
        continue

    image_shape = None
    minimum_value = None
    maximum_value = None

    for file in files:
        image = np.load(file)

        if image_shape is None:
            image_shape = image.shape

        image_minimum = float(np.min(image))
        image_maximum = float(np.max(image))

        if minimum_value is None or image_minimum < minimum_value:
            minimum_value = image_minimum
        if maximum_value is None or image_maximum > maximum_value:
            maximum_value = image_maximum

    print()
    print(f"Storm: {storm_dir.name}")
    print(f"Images: {len(files)}")
    print(f"Shape: {image_shape}")
    print(f"Value range: {minimum_value} - {maximum_value}")

    total_images += len(files)

print(f"\nTotal images: {total_images}")