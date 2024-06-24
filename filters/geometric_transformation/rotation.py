import cv2

from filters.baseFilter import ImageFilter

class Rotation(ImageFilter):
    def __init__(self,angle) -> None:
        super().__init__()
        self.angle = angle
    def apply(self, image):
        center = (image.shape[1] // 2, image.shape[0] // 2)
        M = cv2.getRotationMatrix2D(center,  self. angle, 1.0)
        rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
        return rotated
