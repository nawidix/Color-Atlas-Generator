# PNG/PSD Color Atlas Generator

- This project generates a color atlas in PNG format using hex color values specified in a text file. 
- For use, Clone this repository first to get the "Colors.txt" file: https://github.com/nawidix/ColorExtractor.git .
- The atlas consists of a grid of rectangles, each filled with a specified color.

## Project Structure

```
psd-color-atlas
├── src
│   ├── main.py
│   ├── color_parser.py
│   └── atlas_generator.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/nawidix/Color-Atlas-Generator.git
   cd psd-color-atlas
   ```

2. **Install dependencies:**
   Install the required packages directly:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To generate the color atlas, run the following command:

```
python src/main.py
```

This will read the hex colors from an Open File, create a 128x128px (or custom number) PNG, and fill it with rectangles in a grid layout.

## Dependencies

- `psd-tools`: A library for creating and manipulating PSD files.
- Any other libraries specified in `requirements.txt`.

## Future Updates

- Support for PSD format will be added in the next update.

## License

Free LICENSE.

Made by: @NAWIDX
