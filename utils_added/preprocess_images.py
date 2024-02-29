import os
from PIL import Image

def centercrop_images(source_folder, destination_folder, size=(256, 256)):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through all subfolders in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Check if the file is an image
            if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                # Open the image
                image_path = os.path.join(root, file)
                image = Image.open(image_path)

                # Perform center cropping
                width, height = image.size
                left = (width - size[0]) // 2
                top = (height - size[1]) // 2
                right = left + size[0]
                bottom = top + size[1]
                cropped_image = image.crop((left, top, right, bottom))

                # Save the cropped image to the destination folder
                destination_path = os.path.join(destination_folder, file)
                cropped_image.save(destination_path)

                # Close the image
                image.close()

# Example usage
source_folder = '/mnt/d/Data/dtd/images'
img_size = 32
destination_folder = f'/mnt/d/Data/dtd-{img_size}'
centercrop_images(source_folder, destination_folder, size=(img_size, img_size))
