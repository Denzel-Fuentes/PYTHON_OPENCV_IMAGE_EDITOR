import ttkbootstrap as tk

from gui.filters import Filters
from gui.right_panel import RightPanel

class Menu(tk.Frame):
    def __init__(self, parent,image_editor):
        super().__init__(parent)
        self.right_panel = RightPanel.get_instance()
        self.image_editor = image_editor
        self.setup_menu()

    def setup_menu(self):
        fileMenu = tk.Menubutton(self, text='Archivo', style='Primary.Outline.Toolbutton')
        fileMenu.pack(side='left', padx=1)
        menu = tk.Menu(fileMenu, tearoff=0)
        fileMenu['menu'] = menu
        menu.add_command(label='Abrir', command=self.image_editor.open_image)
        menu.add_command(label='Guardar Imagen', command=self.image_editor.save_image)
        menu.add_command(label='Salir', command=self.quit)
        
        toolsMenu = tk.Menubutton(self, text='Herramientas', style='Primary.Outline.Toolbutton')
        toolsMenu.pack(side='left', padx=1)
        menu2 = tk.Menu(toolsMenu, tearoff=0)
        toolsMenu['menu'] = menu2
        menu2.add_command(label='Filtros', command=lambda:self.right_panel.add_panel(Filters,image_editor =  self.image_editor))
        menu2.add_command(label='Deteccion de Objetos', command=self.image_editor.save_image)
        menu2.add_command(label='Morfologia', command=self.quit)

        btn_before = tk.Button(self, text="<=", command=self.image_editor.undo)
        btn_before.pack(side=tk.LEFT, padx=2, pady=2)

        btn_after = tk.Button(self, text="=>", command=self.image_editor.redo)
        btn_after.pack(side=tk.LEFT, padx=2, pady=2)