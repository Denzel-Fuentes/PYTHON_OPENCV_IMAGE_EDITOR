from filters.dilate import DilateMorfologia
from filters.erode import ErodeMorfologia
from func.image_manager import ImageEditorManager
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class Morfologia(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="Morfologia")

    def setup_filters(self):
        self.pack_button(text="Erosion", command=lambda: self.set_filter(ErodeMorfologia(1)))
        self.pack_button(text="Dilatacion", command=lambda: self.set_filter(DilateMorfologia(1)))
        self.set_scale()

