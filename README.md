
# IRESA: Icon Resizer and Export Script

IRESA (Icon Resizer and Export Script) is a Python application designed for resizing images and creating icons in ICO and PNG formats for various sizes.

## Features

- Resize images to standard icon sizes.
- Generate ICO and PNG files for each resized image.

## Pre-compiled Release

A compiled release for MacOS can be found under releases. These are built usig a Intel based Mac running the latest version of MacOS Sonoma.

## Prerequisites

- Python 3
- OpenCV (`pip3 install opencv-python`)
- Pillow (`pip3 install Pillow`)

## Usage

1. **Clone the repository:**

   ```bash
   git https://github.com/MasonicTombomb/IRESA.git
   cd IRESA
   ```

2. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

3. **Place your source image file in the project directory.**

4. **Run the application:**

   The application does support all the standard file types.
   (PNG, JPG, WEBP, AVIF, PBM, SR, RAS, TIFF, HDR, PIC)


   - To resize images with default settings (Source file must be named Source.png):
     ```bash
     python iresa.py
     ```

   - To specify the input file:
     
     ```bash
     python3 iresa.py -I input_image.png
     ```
     
   - To specify the output image name:
     
     ```bash
     python3 iresa.py -I -O output_file_name
     ```

   - To display the current version of the application:
     
     ```bash
     python3 iresa.py -V
     ```

   - Example using default settings:
     
     ```bash
     python3 iresa.py
     ```

   - Example specifying input file and output directory:
     
     ```bash
     python3 iresa.py -I input_image.png -O output_directory
     ```

   Ensure that the source image file is placed in the project directory before running the application.
   if no output name is specified it will be the same as the input file name with the addition of the 
   size at the end.


5. **Check the "ICOs" and "PNGs" directories for the generated icons.**

## Configuration

The default Icon sizes set within IRESA are:
16x16, 24x24, 32x32, 48x48, 64x64, 72x72, 96x96, 144x144, 152x152, 180x180, 192x192, 256x256, 310x310

 You can customize the sizes in the `sizes` array in `iresa.py` to fit your icon size requirements.

## Error Handling

The application includes basic error handling for loading the source file, resizing the image, converting to PIL, and saving the images. Adjustments can be made based on specific requirements and potential error scenarios.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
