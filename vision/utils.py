import cv2 as cv

def load_image(path):
    """
    Loads image from given path
    """
    img = cv.imread(path)
    if img is None:
        raise FileNotFoundError(path)
    return img

def resize_image(img, size):
    """
    Resizes image to a given size
    """
    return cv.resize(img, size, interpolation=cv.INTER_AREA)
