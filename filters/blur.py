import cv2
from .baseFilter import ImageFilter

class BlurFilter(ImageFilter):
    def apply(self, image):
        return cv2.GaussianBlur(image, (5, 5), cv2.BORDER_DEFAULT)