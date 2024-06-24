from filters.convolucion import Convolution
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class ConvolutionPanel(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="Convolucion")
        self.set_filter(Convolution(0))
    def setup_filters(self):
        self.set_scale()

