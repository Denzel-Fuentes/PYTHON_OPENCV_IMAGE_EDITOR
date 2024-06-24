from ttkbootstrap import Canvas, LabelFrame, GROOVE, Button, Label, Frame

class ImageCanvas(LabelFrame):    
    def __init__(self, parent,id):
        super().__init__(parent)
        self.id = id
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.drawing = False
        self.image_name = "Imagen"
        self.config(borderwidth=2, relief=GROOVE)
        self.setup_controls()
        self.canvas = Canvas(self, bg='grey', relief=GROOVE, borderwidth=2)
        self.canvas.pack(fill="both", expand=True)
        self.bind_canvas_click()

    def setup_controls(self):
        control_frame = Frame(self)
        control_frame.pack(side="top", fill="x")

        close_button = Button(control_frame, text="X", command=self.close_canvas)
        close_button.pack(side="right", padx=5, pady=1)

        label = Label(control_frame, text=self.image_name)
        label.pack(side="left", padx=5, pady=1)
        control_frame.bind('<Button-1>', self.on_canvas_click)

    def close_canvas(self):
        from func.image_manager import ImageEditorManager  
        ImageEditorManager.get_instance().close_editor(self.id)

    def close_panel(self):
        self.destroy()
    def bind_canvas_click(self):
        self.canvas.bind('<Button-1>', self.start_rect)
        self.canvas.bind('<B1-Motion>', self.draw_rect)
        self.canvas.bind('<ButtonRelease-1>', self.end_rect)

    def on_canvas_click(self, event):
        from func.image_manager import ImageEditorManager  
        ImageEditorManager.get_instance().set_current_editor(self.id)

    def start_rect(self, event):
        if self.rect:
            self.canvas.delete(self.rect)

        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        self.rect = self.canvas.create_rectangle(
            self.start_x, self.start_y, self.start_x, self.start_y, 
            outline='red', width=2
        )
        self.drawing = True

    def draw_rect(self, event):
        if self.drawing:
            cur_x = self.canvas.canvasx(event.x)
            cur_y = self.canvas.canvasy(event.y)
            self.canvas.coords(self.rect, self.start_x, self.start_y,   cur_x, cur_y)

    def end_rect(self, event):
        self.drawing = False
        from func.image_manager import ImageEditorManager
        editor = ImageEditorManager.get_instance().current_editor
        if editor:
            rect_coords = self.canvas.coords(self.rect)
            x1 = rect_coords[0]
            y1 = rect_coords[1]
            x2 = rect_coords[2]
            y2 = rect_coords[3]

    # Imprimir las coordenadas del rectángulo
            print(f"Coordenadas del rectángulo: ({x1}, {y1}), ({x2}, {y2})")
            editor.paint_selected_area(self.rect)