import ttkbootstrap as tk
from ttkbootstrap.constants import *
from filters.blur import BlurFilter
from filters.grayScale import GrayscaleFilter
from func.image_editor import ImageEditor
from gui.menu import Menu
from gui.right_panel import RightPanel
from gui.style.style_manager import StyleManager
from gui.tool_bar import ToolbarWidget


class PhotoshopTkinter(tk.Window): 
    def __init__(self):
        super().__init__(themename="litera")
        self.title("Photoshop Style App")
        self.state('zoomed')
        StyleManager('superhero')
        self.image_editor = ImageEditor(self)
        self.setup_panes()
        self.setup_menu()
        self.image_editor.canvas = self.canvas

    def setup_menu(self):
        menu = Menu(self,image_editor=self.image_editor)
        menu.pack(pady=10,anchor='w',side="top") 

    def setup_panes(self):
        paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        paned_window.pack(fill=tk.BOTH, expand=True,side="bottom")

        self.canvas = tk.Canvas(paned_window, bg='grey',relief=tk.GROOVE,borderwidth=2)
        paned_window.add(self.canvas, weight=3)

        right_panel = RightPanel.get_instance(parent=paned_window)
        paned_window.add(right_panel, weight=1)


if __name__ == "__main__":
    app = PhotoshopTkinter()
    app.mainloop()