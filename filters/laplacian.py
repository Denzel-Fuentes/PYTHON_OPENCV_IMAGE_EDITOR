import cv2
from .baseFilter import ImageFilter

class LaplacianFilter(ImageFilter):
     def apply(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
        return cv2.convertScaleAbs(laplacian)
