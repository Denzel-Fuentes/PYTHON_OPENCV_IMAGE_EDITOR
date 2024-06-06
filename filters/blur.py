import cv2
from .baseFilter import ImageFilter

class BlurFilter(ImageFilter):
    def apply(self, image):
        return cv2.GaussianBlur(image, (15, 15), cv2.BORDER_DEFAULT)