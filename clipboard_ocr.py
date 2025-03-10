import subprocess
from PIL import Image
import pytesseract
import io

def get_clipboard_image():
    process = subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-o'],
                             capture_output=True)
    if process.returncode != 0 or not process.stdout:
        return None
    return Image.open(io.BytesIO(process.stdout))

def extract_text_from_image(image):
    try:
        return pytesseract.image_to_string(image)
    except pytesseract.TesseractError as e:
        print(f"OCR failed: {e}")
        return ""

def set_clipboard_text(text):
    process = subprocess.run(['xclip', '-selection', 'clipboard'],
                             input=text.encode('utf-8'))
    if process.returncode != 0:
        print("Failed to set clipboard text")

def main():
    image = get_clipboard_image()
    if image is None:
        print("No image in clipboard")
        return
    text = extract_text_from_image(image)
    set_clipboard_text(text)
    print("Text extracted and copied to clipboard")

if __name__ == "__main__":
    main()
