import ttkbootstrap as tk
from ttkbootstrap.constants import *
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter
from gui.canvas_panel import CanvasPanel
from gui.menu import Menu
from gui.right_panel import RightPanel
from gui.style.style_manager import StyleManager


class PhotoshopTkinter(tk.Window): 
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Photoshop Style App")
        self.state('zoomed')
        StyleManager('superhero')
        self.setup_panes()
        self.setup_menu()

    def setup_menu(self):
        menu = Menu(self)
        menu.pack(pady=10,anchor='w',side="top") 

    def setup_panes(self):
        paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True,side="bottom")
        self.canvasPanel = CanvasPanel.get_instance(parent=paned_window)
        paned_window.add(self.canvasPanel, weight=3)

        right_panel = RightPanel.get_instance(parent=paned_window)
        paned_window.add(right_panel, weight=1)


if __name__ == "__main__":
    app = PhotoshopTkinter()
    app.mainloop()