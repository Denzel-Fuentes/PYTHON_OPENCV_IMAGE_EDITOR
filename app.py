import tkinter as tk
from ui import setup_menu, setup_canvas

class PhotoshopApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Photoshop en Tkinter")
        self.root.attributes('-fullscreen', True)
        self.canvas = setup_canvas(self.root)
        setup_menu(self.root, self.canvas)

    def run(self):
        self.root.mainloop()
