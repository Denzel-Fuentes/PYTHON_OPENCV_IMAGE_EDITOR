import cv2
import numpy as np
from filters.baseFilter import ImageFilter
class Thresh(ImageFilter):
    def __init__(self,nKernel) -> None:
       super().__init__()
       if nKernel % 2 == 0:
          nKernel+=1  
       self.nKernel = max(1, nKernel)
    def apply(self, image):
        gris = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gris, (21,21), 0)
        (T2,threshInv2) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
        blurred2 = cv2.GaussianBlur(image, (99,99), 0)
        mascara = cv2.bitwise_and(image,image,mask=threshInv2)
        fil,col,_ = image.shape
        for i in range(fil):
            for j in range(col):
                if mascara[i,j].any():
                    image[i,j] = blurred2[i,j] 
        return image
     