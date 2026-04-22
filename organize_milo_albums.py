import os

# Get all image files in the milo folder
milo_folder = 'images/milo'
image_files = []

# Supported image extensions
extensions = ['.jpg', '.jpeg', '.JPG', '.JPEG', '.png', '.PNG']

# Get all image files and sort them
for filename in os.listdir(milo_folder):
    if any(filename.endswith(ext) for ext in extensions):
        image_files.append(filename)

# Sort files alphabetically
image_files.sort()

print(f"Found {len(image_files)} images in milo folder:")
print("=" * 50)

# Display files in groups for easier organization
for i, filename in enumerate(image_files, 1):
    print(f"{i:3d}. {filename}")

print("=" * 50)
print("\nPlease tell me how to organize these images:")
print("1. Which images should go in the 'milo' album?")
print("2. Which images should go in the 'stitch' album?") 
print("3. Which images should go in the 'milo + stitch' album?")
print("\nYou can specify by:")
print("- File numbers (e.g., '1-50, 100-150')")
print("- File patterns (e.g., 'IMG_*', '*stitch*')")
print("- Specific filenames")
