import cv2
import numpy as np
from .baseFilter import ImageFilter

class DilateMorfologia(ImageFilter):
    def __init__(self,nKernel) -> None:
       super().__init__()
       self.nKernel = nKernel

    def apply(self, image):
     _, thresholded = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
     kernel = np.ones((self.nKernel,self.nKernel), np.uint8)
     return cv2.dilate(thresholded, kernel, iterations=2)
