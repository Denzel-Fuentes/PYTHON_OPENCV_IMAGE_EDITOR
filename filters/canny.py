import cv2
from .baseFilter import ImageFilter

class CannyFilter(ImageFilter):
    def apply(self, image):
        return cv2.Canny(image, 100, 200)
