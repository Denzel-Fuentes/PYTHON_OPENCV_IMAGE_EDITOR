import cv2
import numpy as np

class SegmentacionColorFilter:
    def __init__(self, color):
        self.color = color

    def apply(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        if self.color == "red":

            lower_red1 = np.array([0, 150, 100])
            upper_red1 = np.array([10, 255, 255])
            lower_red2 = np.array([170, 150, 100])
            upper_red2 = np.array([180, 255, 255])
            mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
            mask = cv2.bitwise_or(mask1, mask2)
        elif self.color == "green":
            lower_bound = np.array([35, 150, 100])
            upper_bound = np.array([85, 255, 255])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
        elif self.color == "blue":
            lower_bound = np.array([90, 150, 100])
            upper_bound = np.array([130, 255, 255])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
        else:
            return image
        
        segmented_image = cv2.bitwise_and(image, image, mask=mask)
        
        return segmented_image
