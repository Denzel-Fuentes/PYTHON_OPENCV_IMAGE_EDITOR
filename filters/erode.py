import cv2
from .baseFilter import ImageFilter
import numpy as np
class ErodeMorfologia(ImageFilter):
    def apply(self, image):
     img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
     _, thresholded = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
     kernel = np.ones((3,3), np.uint8)
     return cv2.erode(thresholded, kernel, iterations=2)
     