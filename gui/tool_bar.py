import ttkbootstrap as tk
from ttkbootstrap.constants import *
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter


class ToolbarWidget(tk.Frame):
    def __init__(self, parent, image_editor):
        super().__init__(parent)
        self.image_editor = image_editor
        self.setup_toolbar()

    def setup_toolbar(self):
        btn_select = tk.Button(self, text="Seleccionar", bootstyle="primary", command=lambda: print("Seleccionar"))
        btn_select.pack(side=tk.LEFT, padx=2, pady=2)

        btn_brush = tk.Button(self, text="Pincel", bootstyle="primary", command=lambda: print("Pincel"))
        btn_brush.pack(side=tk.LEFT, padx=2, pady=2)

        btn_grayscale = tk.Button(self, text="Escala de Grises", bootstyle="primary", command=lambda: self.set_filter(GrayscaleFilter()))
        btn_grayscale.pack(side=tk.LEFT, padx=2, pady=2)

    def set_filter(self, filter_strategy):
        self.image_editor.set_filter(filter_strategy)
        self.image_editor.apply_filter()
