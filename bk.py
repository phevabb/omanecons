import os
from django.core.files import File
from appone.models import Logistic  # Replace 'yourapp' with the actual app name

# Path to the folder with images
image_folder = "/home/ato/Desktop/django_projects/omane/photos/KKA_Logistics"

# Loop through each file in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_folder, filename)
        with open(image_path, 'rb') as f:
            # Create Handyman object with image file
            L = Logistic()
            L.image.save(filename, File(f), save=True)
            print(f"Uploaded: {filename}")
