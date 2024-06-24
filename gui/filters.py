from filters.blur import BlurFilter
from filters.gaussian_blur import GaussianBlurFilter
from filters.deteccionBordes import DeteccionBordesFilter
from filters.laplacian import LaplacianFilter
from filters.sobel import SobelFilter
from filters.canny import CannyFilter
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class Filters(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="Filtros")

    def setup_filters(self):
        self.pack_button(text="Gauss", command=lambda: self.set_filter(GaussianBlurFilter(0)))
        self.pack_button(text="Blurred", command=lambda: self.set_filter(BlurFilter(0)))
        self.pack_button(text="Deteccion de Bordes", command=lambda: self.set_filter(DeteccionBordesFilter()))
        self.pack_button(text="Laplacian", command=lambda: self.set_filter(LaplacianFilter()))
        self.pack_button(text="X-y Sobel", command=lambda: self.set_filter(SobelFilter()))
        self.pack_button(text="Canny", command=lambda: self.set_filter(CannyFilter()))
        self.set_scale()
