import os
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "A_sys.settings")  # change to your project name
django.setup()


from django.core.files import File
from appone.models import Logistic

# Path to your local image folder
folder_path = 'l_images/'  # adjust this if needed

# Loop through files and create Engine instances
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.png', '.jpeg', '.webp')):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'rb') as f:
            hm = Logistic(
                image=File(f, name=filename),
                image_alt=f"Alt for {filename}"
            )
            hm.save()
