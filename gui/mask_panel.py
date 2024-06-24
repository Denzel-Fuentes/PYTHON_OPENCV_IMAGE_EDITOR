from filters.dilate import DilateMorfologia
from filters.erode import ErodeMorfologia
from filters.mask.Thresh import Thresh
from filters.mask.ThreshInv import ThreshInv
from func.image_manager import ImageEditorManager
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class MaskPanel(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="Morfologia")

    def setup_filters(self):
        self.pack_button(text="Thresh Binary Inv", command=lambda: self.set_filter(ThreshInv(0)))
        self.pack_button(text="Thresh Binary", command=lambda: self.set_filter(Thresh(0)))
        self.set_scale()

