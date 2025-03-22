# Downloads Management

This project is a Python script for organizing files in a specified directory. It moves image files and executable files into separate folders (`img` and `executable`, respectively).

## Features
- Automatically detects and organizes image files and `.exe` files.
- Verifies if a file is a valid image before moving it.
- Creates target directories (`img` and `executable`) if they do not exist.

## Prerequisites
- Python 3.6 or higher
- `Pillow` library for image verification

## Installation
1. Clone this repository or copy the script to your local machine.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt