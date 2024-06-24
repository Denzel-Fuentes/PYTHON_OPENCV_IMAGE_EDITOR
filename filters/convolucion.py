from filters.baseFilter import ImageFilter
import cv2 as cv
import numpy as np


class ConvolutionFilter(ImageFilter):
    def apply(self, image):
        m = 55
        h1 = cv.getGaussianKernel(m, 7)
        filtered_image = cv.filter2D(image, -1, h1)
        return filtered_image