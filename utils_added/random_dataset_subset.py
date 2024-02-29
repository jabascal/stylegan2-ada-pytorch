import os
import random
import shutil

def random_copy_images(source_folder, target_folder, num_images):
    # Get a list of all image files in the source folder
    image_files = [file for file in os.listdir(source_folder) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # Randomly select the specified number of images
    selected_images = random.sample(image_files, num_images)

    # Copy the selected images to the target folder
    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        target_path = os.path.join(target_folder, image)
        shutil.copy2(source_path, target_path)

# Example usage
source_folder = '/mnt/d/Data/dtd/dtd-256-selec-rc50/'
target_folder = '/mnt/d/Data/dtd/dtd-256-selec-rc50-sub25k/'
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
num_images = 25000

random_copy_images(source_folder, target_folder, num_images)