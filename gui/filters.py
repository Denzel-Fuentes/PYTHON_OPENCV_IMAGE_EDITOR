from ttkbootstrap import LabelFrame, Button, Scale, Label, Frame
from gui.image_manager import ImageEditorManager

from filters.blur import BlurFilter
from filters.gaussian_blur import GaussianBlurFilter
from filters.deteccionBordes import DeteccionBordesFilter
from filters.laplacian import LaplacianFilter
from filters.sobel import SobelFilter
from filters.canny import CannyFilter

class Filters(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.image_editor = ImageEditorManager.get_instance().current_editor
        self.configure(text="Filtros")

    def setup_filters(self):
        self.pack_button(text="Gauss", command=lambda: self.set_filter(GaussianBlurFilter()))
        self.pack_button(text="Blurred", command=lambda: self.set_filter(BlurFilter()))
        self.pack_button(text="Deteccion de Bordes", command=lambda: self.set_filter(DeteccionBordesFilter()))
        self.pack_button(text="Laplacian", command=lambda: self.set_filter(LaplacianFilter()))
        self.pack_button(text="X-y Sobel", command=lambda: self.set_filter(SobelFilter()))
        self.pack_button(text="Canny", command=lambda: self.set_filter(CannyFilter()))
        self.set_scale()

    def update_value_label(self, event):
        value = round(self.scale.get())
        self.label_value.config(text=f"{int(value)}")

    def pack_button(self, text, command):
        button = Button(self, text=text, bootstyle="outline", style="LeftAlign.TButton", command=command)
        button.pack(fill='x', anchor='w', pady=4)

    def set_filter(self, filter_strategy):
        self.image_editor.set_filter(filter_strategy)
        self.image_editor.apply_filter()

    def set_scale(self):
        self.frame = Frame(self)
        self.frame.pack(pady=20)

        self.scale = Scale(self.frame, from_=0, to=100, orient="horizontal", length=400)
        self.scale.pack(side="top")

        self.label_initial = Label(self.frame, text="0")
        self.label_initial.pack(side="left")

        self.label_final = Label(self.frame, text="100")
        self.label_final.pack(side="right")

        self.label_value = Label(self.frame, text=f"{self.scale.get()}", font=("Arial", 14, "bold"))
        self.label_value.pack(pady=0, side="top")

        self.scale.bind("<B1-Motion>", self.update_value_label)
