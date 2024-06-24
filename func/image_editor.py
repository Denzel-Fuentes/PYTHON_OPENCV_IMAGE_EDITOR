import cv2
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk
from func.imageMemento import ImageCaretaker, ImageMemento
import numpy as np
class ImageEditor:
    def __init__(self,file_path,panel,image = None):
        self.canvas = panel.canvas
        self.panel = panel
        self.file_path = file_path
        self.image = image 
        self.image_tk = None 
        self.caretaker = ImageCaretaker()
        self.filter_strategy = None
        self.intensity = 0
        self.open_image()
        self.image_original = self.image 
        self.selected_area = None

    def open_image(self):
        if self.file_path != None:
            self.image = cv2.imread(self.file_path)
            original_height, original_width = self.image.shape[:2]
            print(self.image.shape)
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
            if self.image is not None and np.any(self.image):
                print(self.image)
                original_height, original_width = self.image.shape[:2]
                print(self.image.shape)
                canvas_width = self.canvas.winfo_width()
                canvas_height = self.canvas.winfo_height() 
                scale_width = canvas_width / (original_width+100) 
                scale_height = canvas_height / (original_height+100) 
                scale = min(scale_width, scale_height)
                new_width = max(1, int(original_width * scale)) 
                new_height = max(1, int(original_height * scale)) 

                self.image = cv2.resize(self.image, (new_width, new_height))
                self.update_canvas()
            else:
                print("Error: No se pudo cargar la imagen.")


    def save_image(self):
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.image)
    
    def set_filter(self, filter_strategy,apply = False):
        self.filter_strategy = filter_strategy
        if apply:
            self.apply_filter()
    
    def apply_filter(self,intensity = 0):
        if intensity > 0: 
            if intensity < self.intensity:
                self.image = self.filter_strategy.apply(self.image_original)
                self.update_canvas()    
            elif intensity > self.intensity:
                self.image = self.filter_strategy.apply(image=self.image_original)
                self.update_canvas()
            self.intensity = intensity     
        elif self.image is not None:
            self.add_memento(f"applied filter: {self.filter_strategy.__class__.__name__}")
            self.image = self.filter_strategy.apply(self.image)
            self.update_canvas()

    def update_canvas(self):
        if self.image is not None:
            image_cv = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA) 
            self.image_pil = Image.fromarray(image_cv) 
            self.image_tk = ImageTk.PhotoImage(image=self.image_pil)  
            self.canvas.create_image(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, image=self.image_tk, anchor='center')
   
    def add_memento(self, description):
        memento = ImageMemento(self.image, description)
        self.caretaker.add_memento(memento)

    def undo(self):
        memento = self.caretaker.get_undo()
        if memento:
            self.image = memento.get_image()
            self.update_canvas()

    def redo(self):
        memento = self.caretaker.get_redo()
        if memento:
            self.image = memento.get_image()
            self.update_canvas()
    
    def add_border(self):
        self.canvas.config(highlightbackground="#7DC3E0", highlightthickness=2)
    
    def remove_border(self):
        self.canvas.config(highlightthickness=0)
    
    def paint_selected_area(self, rect):
        if self.image is not None and rect is not None:
            x1, y1, x2, y2 = self.canvas.coords(rect)
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            image_width, image_height = self.image.shape[1], self.image.shape[0]
            x1_img = int(x1 * (image_width / canvas_width))
            y1_img = int(y1 * (image_height / canvas_height))
            x2_img = int(x2 * (image_width / canvas_width))
            y2_img = int(y2 * (image_height / canvas_height))
            self.image[y1_img:y1_img+2, x1_img:x2_img] = [0, 0, 255]  # Bordes superiores e inferiores
            self.image[y2_img-2:y2_img, x1_img:x2_img] = [0, 0, 255]  # Bordes superiores e inferiores
            self.image[y1_img:y2_img, x1_img:x1_img+2] = [0, 0, 255]  # Bordes izquierdos y derechos
            self.image[y1_img:y2_img, x2_img-2:x2_img] = [0, 0, 255]  # Bordes izquierdos y derechos
            self.update_canvas()