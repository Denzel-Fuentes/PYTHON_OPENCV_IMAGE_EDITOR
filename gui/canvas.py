from ttkbootstrap import Canvas, LabelFrame, GROOVE, Button, Label, Frame

class ImageCanvas(LabelFrame):    
    def __init__(self, parent):
        super().__init__(parent)
        self.image_name = "Imagen"
        self.config(borderwidth=2, relief=GROOVE)
        self.setup_controls()
        self.canvas = Canvas(self, bg='grey', relief=GROOVE, borderwidth=2)
        self.canvas.pack(fill="both", expand=True)

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
        print(f"Clicked at x={event.x}, y={event.y}")
