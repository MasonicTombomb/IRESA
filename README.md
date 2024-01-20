# IRESA: Icon Resizer and Export Script

IRESA (Icon Resizer and Export Script) is a Python application designed for resizing images and creating icons in ICO and PNG formats for various sizes.

## Features

- Resize images to different sizes.
- Generate ICO and PNG files for each resized image.

## Prerequisites

- Python 3
- OpenCV (`pip install opencv-python`)
- Pillow (`pip install Pillow`)

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/iresa-icon-resizer.git
   cd iresa-icon-resizer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place your source image file named `Source.png` in the project directory.

4. Run the application:

   ```bash
   python iresa.py
   ```

5. Check the "ICOs" and "PNGs" directories for the generated icons.

## Configuration

- Customize the sizes in the `sizes` array in `main.py` to fit your icon size requirements.

## Error Handling

The application includes basic error handling for loading the source file, resizing the image, converting to PIL, and saving the images. Adjustments can be made based on specific requirements and potential error scenarios.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Feel free to customize the content further based on your specific project details and requirements.