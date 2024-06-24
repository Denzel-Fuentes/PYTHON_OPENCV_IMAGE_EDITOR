import cv2
import numpy as np

class BlancoYNegroFilter:
    def __init__(self, r_factor=0.299, g_factor=0.587, b_factor=0.114):
        self.r_factor = r_factor
        self.g_factor = g_factor
        self.b_factor = b_factor

    def apply(self, image):
        b, g, r = cv2.split(image)
        gray_image = (self.r_factor * r + self.g_factor * g + self.b_factor * b).astype(np.uint8)
        
        return gray_image
