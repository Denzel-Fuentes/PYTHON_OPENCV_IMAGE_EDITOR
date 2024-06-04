import tkinter as tk
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter
from func.image_editor import ImageEditor  # Asegúrate de que ImageEditor esté correctamente importado
from components.button import Button
from components.entry import Entry 

class PhotoshopTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Photoshop Style App")
        self.root.state('zoomed')
        self.setup_toolbar() 
        self.setup_panes()
        self.image_editor = ImageEditor(self.canvas)  
        self.setup_menu()
        self.create_undo_redo_buttons()

    def setup_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Abrir", command=self.image_editor.open_image)
        file_menu.add_command(label="Guardar", command=self.image_editor.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.root.quit)
        menu_bar.add_cascade(label="Archivo", menu=file_menu)

        self.root.config(menu=menu_bar)

    def setup_toolbar(self):
        self.toolbar = tk.Frame(self.root, bg='gray', height=60)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        btn_select = Button(self.toolbar, text="Seleccionar", command=lambda: print("Seleccionar"))
        btn_select.pack(side=tk.LEFT, padx=2, pady=2)

        btn_brush = Button(self.toolbar, text="Pincel", command=lambda: print("Pincel"))
        btn_brush.pack(side=tk.LEFT, padx=2, pady=2)
        
        btn_grayscale = Button(self.toolbar, text="Escala de Grises", command=lambda: self.set_filter(GrayscaleFilter()))
        btn_grayscale.pack(side=tk.LEFT, padx=2, pady=2)

    def setup_panes(self):
        paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=6)
        paned_window.pack(fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(paned_window, bg='grey')
        paned_window.add(self.canvas, stretch="always")

        right_panel = tk.Frame(paned_window, bg='lightblue', width=300)  # Aumentado el ancho y cambiado el color para debugging
        paned_window.add(right_panel, stretch="never", width=300)

        layer_panel = tk.LabelFrame(right_panel, text="Capas", bg='lightgray')
        layer_panel.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        property_panel = tk.LabelFrame(right_panel, text="Propiedades", bg='lightgray')
        property_panel.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    def create_undo_redo_buttons(self):
        btn_before = Button(self.toolbar, text="<=", command=self.image_editor.undo)
        btn_before.pack(side=tk.LEFT, padx=2, pady=2)

        btn_after = Button(self.toolbar, text="=>", command=self.image_editor.redo)
        btn_after.pack(side=tk.LEFT, padx=2, pady=2)
    
    def set_filter(self, filter_strategy):
        self.image_editor.set_filter(filter_strategy)
        self.image_editor.apply_filter()

root = tk.Tk()
app = PhotoshopTkinter(root)
root.mainloop()