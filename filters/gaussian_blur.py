import cv2
from .baseFilter import ImageFilter

class GaussianBlurFilter(ImageFilter):
    def apply(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)
