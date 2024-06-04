import cv2
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk

class ImageEditor:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = None 
        self.image_tk = None  

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            original_height, original_width = self.image.shape[:2]
            # factor de escala
            scale_width = self.canvas.winfo_width() / (original_width+100)
            scale_height = self.canvas.winfo_height() / (original_height+100)
            scale = min(scale_width, scale_height)  
            new_width = int(original_width * scale) 
            new_height = int(original_height * scale)
           
            self.image = cv2.resize(self.image, (new_width, new_height))
            self.update_canvas()

    def save_image(self):
        if self.image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                cv2.imwrite(file_path, self.image)

    def apply_filter(self, filter_type):
        if self.image is not None:
            if filter_type == 'BLUR':
                self.image = cv2.GaussianBlur(self.image, (5, 5), cv2.BORDER_DEFAULT)
            elif filter_type == 'GRAYSCALE':
                self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.update_canvas()

    def update_canvas(self):
        if self.image is not None:
            image_cv = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGBA)  # Convert the image to RGBA
            self.image_pil = Image.fromarray(image_cv)  # Convert the image to PIL format
            self.image_tk = ImageTk.PhotoImage(image=self.image_pil)  # Convert to PhotoImage
            self.canvas.create_image(self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2, image=self.image_tk, anchor='center')
