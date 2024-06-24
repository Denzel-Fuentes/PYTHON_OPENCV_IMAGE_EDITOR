import cv2
from .baseFilter import ImageFilter
import numpy as np

class KClustersSegmentation(ImageFilter):
    def __init__(self, nKernel):
        super().__init__()
        self.nKernel = nKernel
    
    def apply(self, image):
        if self.nKernel == 0:
            return image.copy()  # Devuelve una copia de la imagen original si nKernel es 0

        # Redimensionamos para trabajar con las 3 capas
        pixel = image.reshape((-1, 3))
        pixel = np.float32(pixel)

        # Criterios de convergencia para k-means
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        # Ejecutamos k-means
        compactness, labels, centers = cv2.kmeans(pixel, self.nKernel, None, criteria, 100, cv2.KMEANS_RANDOM_CENTERS)

        centers = np.uint8(centers)
        labels = labels.flatten()

        segmented = centers[labels]
        segmented = segmented.reshape(image.shape)

        return cv2.cvtColor(segmented, cv2.COLOR_BGR2RGB)
