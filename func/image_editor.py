import cv2
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk
from func.imageMemento import ImageCaretaker, ImageMemento

class ImageEditor:
    def __init__(self,file_path ,canvas):
        self.canvas = canvas
        self.file_path = file_path
        self.image = None 
        self.image_tk = None 
        self.caretaker = ImageCaretaker()
        self.filter_strategy = None
        self.open_image() 

    def open_image(self):
        self.image = cv2.imread(self.file_path)
        if self.image is not None:
            original_height, original_width = self.image.shape[:2]
            
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height() 

            scale_width = canvas_width / (original_width+100)  # Evitar división por cero
            scale_height = canvas_height / (original_height+100)  # Evitar división por cero
            scale = min(scale_width, scale_height)

            new_width = max(1, int(original_width * scale))  #  Asegurar mínimo tamaño de 1
            new_height = max(1, int(original_height * scale))  # Asegurar mínimo tamaño de 1

            self.image = cv2.resize(self.image, (new_width, new_height))
            self.update_canvas()
        else:
            print("Error: No se pudo cargar la imagen.")

    def save_image(self):
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.image)
    
    def set_filter(self, filter_strategy):
        self.filter_strategy = filter_strategy
    
    def apply_filter(self):
        if self.image is not None:
            self.add_memento(f"applied filter: {self.filter_strategy.__class__.__name__}")
            self.image = self.filter_strategy.apply(self.image)
            self.update_canvas()

    def update_canvas(self):
        if self.image is not None:
            image_cv = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)  # Convert the image to RGBA
            self.image_pil = Image.fromarray(image_cv)  # Convert the image to PIL format
            self.image_tk = ImageTk.PhotoImage(image=self.image_pil)  # Convert to PhotoImage
            self.canvas.create_image(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, image=self.image_tk, anchor='center')
   
    def add_memento(self, description):
        memento = ImageMemento(self.image, description)
        self.caretaker.add_memento(memento)

    def undo(self):
        print('hello from undo')
        memento = self.caretaker.get_undo()
        if memento:
            self.image = memento.get_image()
            self.update_canvas()

    def redo(self):
        print('hello from redo')
        memento = self.caretaker.get_redo()
        if memento:
            self.image = memento.get_image()
            self.update_canvas()
    
    def add_border(self):
        self.canvas.config(highlightbackground="#7DC3E0", highlightthickness=2)
    
    def remove_border(self):
        self.canvas.config(highlightthickness=0)