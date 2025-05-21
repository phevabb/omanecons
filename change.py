import os

# Set the path to your image folder
folder_path = '/home/ato/Desktop/django_projects/omane/photos/KKA Logistics'

# Get a sorted list of all files in the folder (filtering image files)
image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

# Loop through and rename each image
for index, filename in enumerate(image_files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_filename = f"{index}.jpg"
    new_path = os.path.join(folder_path, new_filename)
    
    os.rename(old_path, new_path)
    print(f"Renamed {filename} -> {new_filename}")

print("Renaming complete.")
