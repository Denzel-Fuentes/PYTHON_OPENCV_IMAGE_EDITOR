import ttkbootstrap as tk

from filters.geometric_transformation.rotation import Rotation
from gui.filters import Filters
from func.image_manager import ImageEditorManager
from gui.kclusters_panel import KClustersPanel
from gui.morfology import Morfologia
from gui.right_panel import RightPanel

class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.right_panel = RightPanel.get_instance()
        self.image_editorManager = ImageEditorManager.get_instance()
        self.setup_menu()

    def setup_menu(self):
        fileMenu = tk.Menubutton(self, text='Archivo', style='Primary.Outline.Toolbutton')
        fileMenu.pack(side='left', padx=1)
        menu = tk.Menu(fileMenu, tearoff=0)
        fileMenu['menu'] = menu
        menu.add_command(label='Abrir', command=self.image_editorManager.open_image)
        menu.add_command(label='Salir', command=self.quit)
        
        toolsMenu = tk.Menubutton(self, text='Herramientas', style='Primary.Outline.Toolbutton')
        toolsMenu.pack(side='left', padx=1)
        menu2 = tk.Menu(toolsMenu, tearoff=0)
        toolsMenu['menu'] = menu2
        menu2.add_command(label='Filtros', command=lambda:self.right_panel.add_panel(Filters))
        menu2.add_command(label='Morfologia', command=lambda:self.right_panel.add_panel(Morfologia))
        menu2.add_command(label='K-Clusters ', command=lambda:self.right_panel.add_panel(KClustersPanel))
        menu2.add_command(label='Deteccion de Objetos', command=lambda:print("deteccion"))
 

        btn_before = tk.Button(self, text="<=", command=lambda:self.image_editorManager.current_editor.undo())
        btn_before.pack(side=tk.LEFT, padx=2, pady=2)

        btn_after = tk.Button(self, text="=>", command=lambda: self.image_editorManager.current_editor.redo())
        btn_after.pack(side=tk.LEFT, padx=2, pady=2)

        btn_rotate = tk.Button(self, text="🔄", command=lambda: self.image_editorManager.current_editor.set_filter(Rotation(90),apply = True))
        btn_rotate.pack(side=tk.LEFT, padx=2, pady=2)