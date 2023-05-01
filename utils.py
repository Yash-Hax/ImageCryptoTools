import cv2

def load_image(filepath):
    """Load image from file path"""
    img = cv2.imread(filepath, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Failed to load image from file: {filepath}")
    return img

def save_image(filepath, img):
    """Save image to file path"""
    cv2.imwrite(filepath, img)
# You can add any other utility functions you may need to this file as well.
