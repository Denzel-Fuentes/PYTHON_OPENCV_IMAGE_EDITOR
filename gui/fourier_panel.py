from filters.Fourier.fourier import Fourier
from filters.dilate import DilateMorfologia
from filters.erode import ErodeMorfologia
from func.image_manager import ImageEditorManager
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class FourierPanel(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="Fourier")

    def setup_filters(self):
        self.pack_button(text="Fourier", command=lambda: self.set_filter(Fourier()))

