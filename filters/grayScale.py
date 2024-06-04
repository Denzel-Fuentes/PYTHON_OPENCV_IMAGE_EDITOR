import cv2
from filters.baseFilter import ImageFilter


class GrayscaleFilter(ImageFilter):
    def apply(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)