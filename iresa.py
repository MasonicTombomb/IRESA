#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IRESA: Icon Resizer and Export Script.

IRESA (Icon Resizer and Export Script) is a Python application designed for resizing
images and creating icons in ICO and PNG formats for various sizes.

Example:
    The script can be executed as follows::

        $ python3 iresa.py -I Source.png

Attributes:
    __author__ (str): The author of the script.
    __copyright__ (str): Copyright information for the script.
    __credits__ (list): List of credits for the script.
    __license__ (str): License information for the script.
    __version__ (str): Version number of the script.
    __maintainer__ (str): Maintainer of the script.
    __email__ (str): Contact email for the script.
    __status__ (str): Current status or release status of the script.

Usage:
    The script can be run from the command line. It supports command-line arguments for
    specifying input and output filenames.

    Example:
        $ python3 iresa_icon_resizer.py -I Source.png -O MyIcon

Dependencies:
    - OpenCV: Image processing library (install with `pip install opencv-python`)
    - Pillow: Python Imaging Library (install with `pip install Pillow`)

Todo:
    * Implement more advanced error handling.
    * Implement batch processing from list of inputs. (-B?)
    * Implement batch processing from a given Dir. (-D?)
    * Implement file type filtering. (-F?)
    * Image format conversion. (-C?)
    * Custom image sizes inputted by the user. (-S?)
    * Implement a GUI to the application.

"""

# Standard Library Imports
import os
import warnings
import argparse

# Third-Party Imports
import cv2 as cv
from PIL import Image

# Local Imports (None for now)

__author__ = "Thomas Scott"
__copyright__ = "Copyright 2024, The IRESA Project"
__credits__ = ["Thomas Scott"]
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Thomas Scott"
__email__ = "tom@secdev.info"
__status__ = "Release"

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
        save_path = os.path.join(folder, filename)  # Path to save image too
        image_pil.save(save_path, format=image_format)  # The PIL.Image.Image object
    except Exception as e:
        print(f"Error saving image: {e}")


def main():
    """
    Main function to resize images and save in ICO and PNG formats.
    """
    parser = argparse.ArgumentParser(description='''IRESA 
        IRESA (Icon Resizer and Export Script) is a Python application
        designed for resizing images and creating icons in ICO and PNG
        formats for various sizes.
        IMPORTANT: Please ensure your source image is in the same directory as this application!

        Please note the default input image name is Source.png.
        Supported input file types include:
        PNG, JPG, WEBP, AVIF, PBM (and variants), SR and RAS, TIFF, HDR, PIC
        ''', formatter_class=argparse.RawTextHelpFormatter)

    # Define the input file path argument
    parser.add_argument('-I', '--input', default='Source.png', action='store', type=str, help='Input file name, -I '
                                                                                              'followed by the name.')
    # Define the output file path argument
    parser.add_argument('-O', '--output', action='store', type=str, help='Output file name, -O followed by the name.')

    # Returns the application version
    parser.add_argument('-V', '--version', action='store_true', help='Display the current version of the application.')

    # Creates a dictionary of arguments
    args = parser.parse_args()

    if args.version:
        print(f"IRESA Version: {__version__}")
        print(f"Under: {__license__} license")
        print(f"{__copyright__}")
        exit(0)

    # If output file path is not provided, use the default
    if not args.output:
        # Extracting the file name from the input path
        input_file_name = args.input.split('.')[0]
        args.output = f"{input_file_name}"

    print(f"Input file path: {args.input}")
    print(f"Output file path: {args.output}")

    # Default if no input file specified
    source_file = args.input  # The name and location fo the source ONG. (Relative path)
    if not os.path.exists(source_file):
        print(f"Source file '{source_file}' not found.")
        return

    # Load the source image
    image = cv.imread(source_file)  # The CV object of the image
    if image is None:
        print(f"Error loading source image '{source_file}'.")
        return

    sizes = [16, 24, 32, 48, 64, 72, 96, 144, 152, 180, 192, 256, 310]  # The sizing's of the image

    # Create directories if they don't exist
    for folder in ["PNGs", "ICOs"]:
        os.makedirs(folder, exist_ok=True)

    for size in sizes:
        # Resize image
        resized_image = resize_image(image, (size, size))  # The resized image
        if resized_image is None:
            continue

        # Convert to a PIL object
        image_pil = convert_to_pil(resized_image)  # The PIL.Image.Image object
        if image_pil is None:
            continue

        # Save images in ICO format
        save_image(image_pil, f"{args.output}{size}.ico", "ICO", "ICOs")

        # Save images in PNG format
        save_image(image_pil, f"{args.output}{size}.png", "PNG", "PNGs")


if __name__ == '__main__':
    main()
