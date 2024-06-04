import ttkbootstrap as tk
from ttkbootstrap.constants import *
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter
from func.image_editor import ImageEditor

class RightPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.setup_right_panel()

    def setup_right_panel(self):
        layer_panel = tk.LabelFrame(self, text="Capas")
        layer_panel.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        filters_panel = tk.LabelFrame(self,text="Filtros")
        filters_panel.pack(fill=tk.BOTH,expand=True, padx=5,pady=5 )




 