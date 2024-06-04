import ttkbootstrap as tk
from ttkbootstrap.constants import *
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter
from func.image_editor import ImageEditor
from gui.right_panel import RightPanel
from gui.tool_bar import ToolbarWidget


class PhotoshopTkinter(tk.Window): 
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Photoshop Style App")
        self.state('zoomed')
        
        self.image_editor = ImageEditor(self)
        self.setup_panes()
        self.image_editor.canvas = self.canvas
        self.setup_menu()
        self.create_undo_redo_buttons()

    def setup_menu(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label="Abrir", command=self.image_editor.open_image)
        file_menu.add_command(label="Guardar", command=self.image_editor.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)

    def setup_panes(self):
        self.toolbar = ToolbarWidget(self, self.image_editor)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(paned_window, bg='grey')
        paned_window.add(self.canvas, weight=2)

        right_panel = RightPanel(paned_window)
        paned_window.add(right_panel, weight=1)

    def create_undo_redo_buttons(self):
        btn_before = tk.Button(self.toolbar, text="<=", command=self.image_editor.undo)
        btn_before.pack(side=tk.LEFT, padx=2, pady=2)

        btn_after = tk.Button(self.toolbar, text="=>", command=self.image_editor.redo)
        btn_after.pack(side=tk.LEFT, padx=2, pady=2)

if __name__ == "__main__":
    app = PhotoshopTkinter()
    app.mainloop()