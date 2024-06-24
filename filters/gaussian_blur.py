import cv2
from .baseFilter import ImageFilter

class GaussianBlurFilter(ImageFilter):
    def __init__(self,nKernel) -> None:
        super().__init__()
        if nKernel % 2 == 0:
          nKernel+=1  
        self.nKernel = max(1, nKernel)
    def apply(self, image):
        return cv2.GaussianBlur(image, (self.nKernel, self.nKernel), 0)
