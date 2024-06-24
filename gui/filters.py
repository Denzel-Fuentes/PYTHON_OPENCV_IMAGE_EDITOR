from ttkbootstrap import LabelFrame, Button, Scale, Label, Frame, Notebook
from gui.image_manager import ImageEditorManager

from filters.blur import BlurFilter
from filters.gaussian_blur import GaussianBlurFilter
from filters.deteccionBordes import DeteccionBordesFilter
from filters.laplacian import LaplacianFilter
from filters.sobel import SobelFilter
from filters.canny import CannyFilter
from filters.segmentacion_color import SegmentacionColorFilter
from filters.histograma import HistogramaFilter
from filters.ecualizacion_histograma import EcualizacionHistogramaFilter
from filters.cuantizacion import CuantizacionFilter

class Filters(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.image_editor = ImageEditorManager.get_instance()
        self.configure(text="Filtros")
        self.num_colors = 8  # Número inicial de colores para la cuantización
        self.intensity = 50  # Intensidad inicial del filtro
        self.setup_ui()

    def setup_ui(self):
        notebook = Notebook(self)
        notebook.pack(fill='both', expand=True)

        basic_frame = Frame(notebook)
        notebook.add(basic_frame, text='Filtros básicos')
        self.setup_basic_filters(basic_frame)

        segment_frame = Frame(notebook)
        notebook.add(segment_frame, text='Segmentación')
        self.setup_segmentation_filters(segment_frame)

        hist_cuant_frame = Frame(notebook)
        notebook.add(hist_cuant_frame, text='Histograma y Cuantización')
        self.setup_hist_cuant_filters(hist_cuant_frame)

        self.set_scale(basic_frame)
        self.set_scale(segment_frame)
        self.set_scale(hist_cuant_frame)

    def setup_basic_filters(self, parent):
        self.pack_button(parent, text="Gauss", command=lambda: self.set_filter(GaussianBlurFilter()))
        self.pack_button(parent, text="Blurred", command=lambda: self.set_filter(BlurFilter()))
        self.pack_button(parent, text="Deteccion de Bordes", command=lambda: self.set_filter(DeteccionBordesFilter()))
        self.pack_button(parent, text="Laplacian", command=lambda: self.set_filter(LaplacianFilter()))
        self.pack_button(parent, text="X-y Sobel", command=lambda: self.set_filter(SobelFilter()))
        self.pack_button(parent, text="Canny", command=lambda: self.set_filter(CannyFilter()))

    def setup_segmentation_filters(self, parent):
        self.pack_button(parent, text="Segmentar Rojo", command=lambda: self.set_filter(SegmentacionColorFilter("red")))
        self.pack_button(parent, text="Segmentar Verde", command=lambda: self.set_filter(SegmentacionColorFilter("green")))
        self.pack_button(parent, text="Segmentar Azul", command=lambda: self.set_filter(SegmentacionColorFilter("blue")))

    def setup_hist_cuant_filters(self, parent):
        self.pack_button(parent, text="Histograma", command=self.apply_histograma)
        self.pack_button(parent, text="Ecualización de Histograma", command=self.apply_ecualizacion_histograma)
        self.pack_button(parent, text="Cuantización", command=self.apply_cuantizacion)

    def update_value_label(self, event):
        value = round(self.scale.get())
        self.label_value.config(text=f"{int(value)}")
        self.intensity = value

    def pack_button(self, parent, text, command):
        button = Button(parent, text=text, bootstyle="outline", command=command)
        button.pack(fill='x', anchor='w', pady=2, padx=10)  # Reducir el padding para que ocupen menos espacio

    def set_filter(self, filter_strategy):
        self.image_editor.current_editor.set_filter(filter_strategy)
        self.image_editor.current_editor.apply_filter()

    def apply_histograma(self):
        self.set_filter(HistogramaFilter())

    def apply_ecualizacion_histograma(self):
        self.set_filter(EcualizacionHistogramaFilter())

    def apply_cuantizacion(self):
        self.set_filter(CuantizacionFilter(self.num_colors))

    def set_scale(self, parent):
        self.frame = Frame(parent)
        self.frame.pack(pady=10)

        self.scale = Scale(self.frame, from_=0, to=100, orient="horizontal", length=300)
        self.scale.set(self.intensity)
        self.scale.pack(side="top")

        self.label_initial = Label(self.frame, text="0")
        self.label_initial.pack(side="left")

        self.label_final = Label(self.frame, text="100")
        self.label_final.pack(side="right")

        self.label_value = Label(self.frame, text=f"{self.intensity}", font=("Arial", 14, "bold"))
        self.label_value.pack(pady=0, side="top")

        self.scale.bind("<B1-Motion>", self.update_value_label)
