import os
from tkinter import Tk, filedialog
from PIL import Image

def resize_images(directory, target_size):
    for filename in os.listdir(directory):
        if filename.endswith((".jpg", ".jpeg", ".png", ".bmp")):
            img_path = os.path.join(directory, filename)
            with Image.open(img_path) as img:
                img = img.resize(target_size, Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
                img.save(img_path)
            print(f"Resized and saved: {filename}")

# Create a file browser dialog
root = Tk()
root.withdraw()  # Hide the root window
directory_path = filedialog.askdirectory(title="Select Directory with Images")

if directory_path:
    target_size = (800, 600)  # Adjust the target size as needed
    resize_images(directory_path, target_size)
else:
    print("No directory selected, exiting.")
