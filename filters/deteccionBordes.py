import cv2
from .baseFilter import ImageFilter
import numpy as np

class DeteccionBordesFilter(ImageFilter):
     def apply(self, image):
        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Aplicar un desenfoque para reducir el ruido
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Aplicar el detector de bordes Canny
        edges = cv2.Canny(blurred, 50, 150)
        
        # Dilatar los bordes para hacerlos más gruesos
        kernel = np.ones((3, 3), np.uint8)
        dilated_edges = cv2.dilate(edges, kernel, iterations=1)
        
        # Crear una imagen en blanco con las mismas dimensiones que la imagen original
        edges_colored = np.zeros_like(image)
        
        # Resaltar los bordes en color rojo (R, G, B)
        edges_colored[dilated_edges != 0] = [255, 0, 0]
        
        # Fusionar la imagen original con los bordes en color
        result = cv2.addWeighted(image, 0.8, edges_colored, 1, 0)
        
        return result