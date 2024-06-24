import cv2
from .baseFilter import ImageFilter
import numpy as np
class Convolution(ImageFilter):
    def __init__(self, nKernel) -> None:
        super().__init__()
        self.nKernel = nKernel
    
    def apply(self, image):
        m = 55
        N, M, C = image.shape 
        Y2 = np.zeros((N, M, C))
        h1 = cv2.getGaussianKernel(m, self.nKernel)
        for i in range(C): 
            for j in range(N): 
                Y2[j, :, i] = np.convolve(image[j, :, i], h1[:, 0].flatten(), "same")
        
        Y2 = np.clip(Y2, 0, 255) 
        Y2 = Y2.astype(np.uint8) 
        return Y2
