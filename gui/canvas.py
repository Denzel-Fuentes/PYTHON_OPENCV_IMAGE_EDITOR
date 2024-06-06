from ttkbootstrap import Canvas, LabelFrame, GROOVE, Button, Label, Frame

class ImageCanvas(LabelFrame):    
    def __init__(self, parent,id):
        super().__init__(parent)
        self.id = id
        self.image_name = "Imagen"
        self.config(borderwidth=2, relief=GROOVE)
        self.setup_controls()
        self.canvas = Canvas(self, bg='grey', relief=GROOVE, borderwidth=2)
        self.canvas.pack(fill="both", expand=True)
        self.bind_canvas_click(self.on_canvas_click)

    def setup_controls(self):
        control_frame = Frame(self)
        control_frame.pack(side="top", fill="x")

        close_button = Button(control_frame, text="X", command=self.close_canvas)
        close_button.pack(side="right", padx=5, pady=1)

        label = Label(control_frame, text=self.image_name)
        label.pack(side="left", padx=5, pady=1)

    def close_canvas(self):
        self.destroy()

    def bind_canvas_click(self, callback):
        self.canvas.bind('<Button-1>', callback)

    def on_canvas_click(self, event):
        from gui.image_manager import ImageEditorManager  
        ImageEditorManager.get_instance().set_current_editor(self.id)

