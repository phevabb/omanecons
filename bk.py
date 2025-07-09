import os
import django

# Set the Django settings module (replace 'yourproject' with your actual project name)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A_sys.settings')
django.setup()

# Now import models AFTER setup
from appone.models import Engine
from django.core.files import File

# Path to the folder with images
image_folder = r"C:\Users\ato\Desktop\dj\cious\KKA_Engineering"


# Loop through each file in the folder
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_folder, filename)
        with open(image_path, 'rb') as f:
            E = Engine()
            E.image.save(filename, File(f), save=True)
            print(f"Uploaded: {filename}")
