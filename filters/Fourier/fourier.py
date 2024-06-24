import cv2
import numpy as np
from filters.baseFilter import ImageFilter
import matplotlib.pyplot as plt
class Fourier(ImageFilter):
    def __init__(self) -> None:
        super().__init__()
    
    def apply(self, image):
        if len(image.shape) == 3 and image.shape[2] == 3:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            image_gray = image
        f = np.fft.fft2(image_gray)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift))
        plt.imshow(magnitude_spectrum)
        plt.xlim([480,520])
        plt.ylim([520,480])
        plt.show()
        return image