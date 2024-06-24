import cv2
from matplotlib import pyplot as plt

class HistogramaFilter:
    def apply(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        
        plt.figure()
        plt.title("Histograma")
        plt.xlabel("Intensidad")
        plt.ylabel("Número de píxeles")
        plt.plot(hist)
        plt.xlim([0, 256])
        plt.show()
        return image
