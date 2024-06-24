import cv2
from .baseFilter import ImageFilter
import numpy as np
class ErodeMorfologia(ImageFilter):
    def __init__(self,nKernel) -> None:
       super().__init__()
       self.nKernel = nKernel
    
    def apply(self, image):
     _, thresholded = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY)
     kernel = np.ones((self.nKernel,self.nKernel), np.uint8)
     return cv2.erode(thresholded, kernel, iterations=2)
     