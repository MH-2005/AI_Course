# Image Overlay Editor

A Python script for Jupyter Notebook to overlay a foreground image onto a background with automatic background color removal and rotation.

## Features
- **Auto Background Removal**: Detects and removes dominant background color in RGB.
- **Rotation**: Rotates foreground and mask without interpolation (`INTER_NEAREST`).
- **Overlay**: Places foreground at user-defined coordinates with blending.
- **Visualization**: Displays result using Matplotlib.

## Prerequisites
- Python 3.8+
- Libraries: `pip install opencv-python numpy matplotlib`
- Images: Background (e.g., `background.jpg`), foreground with uniform background (e.g., `foreground.png`)

## Usage
1. Run in Jupyter Notebook.
2. Enter background and foreground image paths.
3. Input tolerance (e.g., `30`), x/y coordinates, and rotation angle (degrees).
4. View the overlaid image.

## Notes
- Foreground needs uniform background color.
- Coordinates are clamped to fit background.
- Adjust tolerance for variable backgrounds.

## License
MIT License