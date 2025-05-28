import os
import uuid
import cv2
from datetime import datetime

def generate_unique_filename(extension=".jpg"):
    """Generates a unique filename using UUID and timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_id = uuid.uuid4().hex[:6]
    return f"{timestamp}_{unique_id}{extension}"

def resize_image(image_path, size=(224, 224)):
    """Reads and resizes an image to the given size."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image not found at {image_path}")
    resized = cv2.resize(image, size)
    return resized

def cleanup_folder(folder_path, keep_recent=10):
    """Keeps only the most recent 'keep_recent' files in a folder."""
    files = sorted(
        [os.path.join(folder_path, f) for f in os.listdir(folder_path)],
        key=os.path.getmtime,
        reverse=True
    )
    for file in files[keep_recent:]:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error removing file {file}: {e}")