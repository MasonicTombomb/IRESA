import os
import cv2 as cv
from PIL import Image
import warnings

# Suppress the specific warning
warnings.filterwarnings("ignore", message=".*iCCP.*")


def resize_image(image, size):
    """
    Resize the input image to the specified size.

    Parameters:
    - image: numpy.ndarray
        The input image as a NumPy array.
    - size: tuple
        A tuple representing the target size (width, height) for resizing.

    Returns:
    - numpy.ndarray
        The resized image.
    """
    try:
        return cv.resize(image, size)
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None


def convert_to_pil(image):
    """
    Convert the input image (in BGR format) to a PIL Image.

    Parameters:
    - image: numpy.ndarray
        The input image as a NumPy array in BGR format.

    Returns:
    - PIL.Image.Image
        The converted PIL Image.
    """
    try:
        return Image.fromarray(cv.cvtColor(image, cv.COLOR_BGR2RGB))
    except Exception as e:
        print(f"Error converting to PIL Image: {e}")
        return None


def save_image(image_pil, filename, image_format, folder):
    """
    Save the PIL Image to a file with the specified filename and format in the specified folder.

    Parameters:
    - image_pil: PIL.Image.Image
        The PIL Image to be saved.
    - filename: str
        The name of the output file.
    - image_format: str
        The format for saving the image (e.g., 'ICO', 'PNG').
    - folder: str
        The name of the folder to save the image in.
    """
    try:
        save_path = os.path.join(folder, filename)
        image_pil.save(save_path, format=image_format)
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    """
    Main function to resize images and save in ICO and PNG formats.
    """
    # Check if the source file exists
    source_file = "Source.png"
    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' not found.")
        return

    # Load the source image
    image = cv.imread(source_file)
    if image is None:
        print(f"Error loading source image '{source_file}'.")
        return

    sizes = [16, 24, 32, 48, 64, 72, 96, 144, 152, 180, 192, 256, 310]

    # Create directories if they don't exist
    for folder in ["PNGs", "ICOs"]:
        os.makedirs(folder, exist_ok=True)

    for size in sizes:
        # Resize image
        resized_image = resize_image(image, (size, size))
        if resized_image is None:
            continue

        # Convert to a PIL object
        image_pil = convert_to_pil(resized_image)
        if image_pil is None:
            continue

        # Save images in ICO format
        save_image(image_pil, f"output{size}.ico", "ICO", "ICOs")

        # Save images in PNG format
        save_image(image_pil, f"output{size}.png", "PNG", "PNGs")


if __name__ == '__main__':
    main()
