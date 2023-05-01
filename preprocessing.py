from PIL import Image
import os

def preprocess_image(file_path):
    # Open the image file using the PIL library
    with Image.open(file_path) as img:
        # Convert the image to raw format to remove any metadata or identifying information
        img = img.convert('RGB')
        raw_img = img.tobytes()

    # Write the raw image to a new file
    new_file_path = os.path.splitext(file_path)[0] + '_raw.png'
    with open(new_file_path, 'wb') as f:
        f.write(raw_img)

    return new_file_path
