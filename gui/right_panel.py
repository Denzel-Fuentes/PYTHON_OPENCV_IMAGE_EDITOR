import ttkbootstrap as tk
from ttkbootstrap.constants import *

from gui.layers import Layers

class RightPanel(tk.Frame):
    _instance = None
    
    def __init__(self, parent):
        if RightPanel._instance != None:
            raise Exception("Singleton already created!")
        else:
            super().__init__(parent)
            self.config(relief=tk.GROOVE, borderwidth=1)
            self.setup_right_panel()
            RightPanel._instance = self

    def setup_right_panel(self):
        self.layer_panel = Layers(self)
        self.layer_panel.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        self.filters_panel = tk.LabelFrame(self, text="Detalles")
        self.filters_panel.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def add_panel(self, panel_class,**arg):
        custom_panel = panel_class(self,**arg)
        if hasattr(custom_panel, 'setup_filters'):
            custom_panel.setup_filters()
        custom_panel.pack(before=self.filters_panel, fill=tk.BOTH, expand=True, padx=5, pady=5)
    
    @staticmethod
    def get_instance(parent=None):
        if RightPanel._instance == None:
            if parent is None:
                raise ValueError("Se necesita un componente padre para crear la instancia de RightPanel.")
            RightPanel(parent)
        return RightPanel._instance
