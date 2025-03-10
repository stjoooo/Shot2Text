# Clipboard Image to Text Converter

This Python script extracts text from screenshots in your clipboard using OCR and replaces the clipboard content with the extracted text. I made it for my Ubuntu setup, where I take screenshots with `Fn + F8` and extract text with `Fn + F9`.

## Requirements

- Ubuntu (tested on 24.04; may work on other Linux distros)
- Python 3.12.3+
- System packages: `xclip`, `tesseract-ocr`
- Python libraries: `Pillow`, `pytesseract`

## Installation

Follow these steps to set it up:

1. Install system dependencies: 
   ```
   sudo apt-get install xclip tesseract-ocr
   ```

2. Create a virtual environment: 
   ```
   python3 -m venv ~/myenv
   source ~/myenv/bin/activate
   ```
3. Install Python libraries:
   ```
   pip install pytesseract Pillow
   ```

4. Save the script: Grab [`clipboard_ocr.py`](./clipboard_ocr.py) and save it to `~/clipboard_ocr.py`.

5. Set up the keyboard shortcut:
    - Open Settings > Keyboard > Shortcuts.
    - Click + to add a new shortcut.
    - Enter:
      - Name: "Clipboard OCR"
      - Command: `/home/yourusername/myenv/bin/python /home/yourusername/clipboard_ocr.py`
  - Set it to `Fn + F9` (or another key if needed).
  - Save it.  
  **Note**: Replace `yourusername` with your actual username.

## Usage

1. Take a screenshot with `Fn + F8`.
2. Press `Fn + F9` to extract the text.
3. Paste it with `Ctrl + V`.

## License

This project is licensed under the [MIT License](./LICENSE). See the LICENSE file for details.


