import cv2
import numpy as np

class CuantizacionFilter:
    def __init__(self, num_colors):
        self.num_colors = num_colors

    def apply(self, image):
        data = image.reshape((-1, 3))
        data = np.float32(data)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(data, self.num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        segmented_data = centers[labels.flatten()]

        segmented_image = segmented_data.reshape(image.shape)
        return segmented_image
