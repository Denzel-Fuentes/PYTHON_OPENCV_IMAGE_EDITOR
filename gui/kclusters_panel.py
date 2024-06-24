from filters.KclusteresSegmentation import KClustersSegmentation
from filters.dilate import DilateMorfologia
from filters.erode import ErodeMorfologia
from func.image_manager import ImageEditorManager
from gui.common.funtionsbase_panel import BaseFunctionsPanel

class KClustersPanel(BaseFunctionsPanel):
    def __init__(self, parent):
        super().__init__(parent, title="K-Clusteres Segmentacion")
        self.set_filter(KClustersSegmentation(0))
    def setup_filters(self):
        self.set_scale(from_=0,to=5)

