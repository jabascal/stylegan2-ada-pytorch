import os
import random
from PIL import Image

def preprocess_images_random_crop(source_folder, destination_folder, image_size, num_crops):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through the subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the full path of the image file
            image_path = os.path.join(root, file)

            # Open the image using PIL
            image = Image.open(image_path)

            # Generate random crops
            for i in range(num_crops):
                try:
                    # Generate random coordinates for the crop
                    left = random.randint(0, image.width - image_size)
                    upper = random.randint(0, image.height - image_size)
                    right = left + image_size
                    lower = upper + image_size

                    # Crop the image
                    cropped_image = image.crop((left, upper, right, lower))

                    # Save the cropped image to the destination folder
                    # Modify the filename, removing first format extension, add _crop_{i} to the end, and then add the format extension back
                    cropped_image_filename = file.split('.')[0] + f'_crop_{i}.' + file.split('.')[1]
                    cropped_image.save(os.path.join(destination_folder, cropped_image_filename)) 
                except:
                    print(f'Error processing file: {image_path}. Skipping.')                                               

            # Close the image
            image.close()

# Example usage

#source_folder = "/mnt/d/Data/dtd/images"
source_folder = "/mnt/d/Data/dtd-selec"
image_size = 256
num_crops = 10
destination_folder = f'/mnt/d/Data/dtd-{image_size}-selec-rc{num_crops}'

preprocess_images_random_crop(source_folder, destination_folder, image_size, num_crops)
