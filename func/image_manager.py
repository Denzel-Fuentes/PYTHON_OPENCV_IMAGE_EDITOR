from ttkbootstrap import Canvas
from func.image_editor import ImageEditor
from tkinter import filedialog
from gui.canvas import ImageCanvas
from gui.canvas_panel import CanvasPanel
from gui.layers import Layers
import cv2
import numpy as np
class ImageEditorManager:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls._instance.editors = {}  
            cls._instance.current_id = 0  
            cls._instance.current_editor = None
        return cls._instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ImageEditorManager, cls).__new__(cls)
        return cls._instance

    def open_image(self):
        self.current_id += 1
        image_canvas = ImageCanvas(CanvasPanel.get_instance(),id=self.current_id)
        image_canvas.pack(side='left', fill="both", expand=True)  # Usar side='top'
        file_path = filedialog.askopenfilename()
        if file_path:
            editor = ImageEditor(file_path=file_path, panel=image_canvas)
            self.editors[self.current_id] = editor
            self.set_current_editor(self.current_id)
            self.layers = Layers.get_instance()
            self.layers.add_checkbox("imagen",image_id=self.current_id)
            self.updateAllCanvas()
    def get_editor(self, editor_id):
        return self.editors.get(editor_id, None)

    def close_editor(self, editor_id):
        if editor_id in self.editors:
            self.editors[editor_id].panel.close_panel()
            Layers.get_instance().remove(editor_id)
            del self.editors[editor_id]
        for editor in self.editors.values():
            editor.update_canvas()

    def set_current_editor(self, editor_id):
        for editor in self.editors.values():
            editor.remove_border()
        self.current_editor = self.get_editor(editor_id)
        if self.current_editor is not None:
            self.current_editor.add_border()

    def updateAllCanvas(self):
        for editor in self.editors.values():
            editor.update_canvas()

    def sum_images(self, image_ids):
        images_to_sum = [self.get_editor(image_id).image_original for image_id in image_ids if self.get_editor(image_id) is not None]
        min_width = min(image.shape[1] for image in images_to_sum)
        min_height = min(image.shape[0] for image in images_to_sum)
        target_size = (min_width, min_height)
        resized_images = [cv2.resize(image, target_size) for image in images_to_sum]
        sum_image = np.zeros_like(resized_images[0], dtype=np.uint8)
        for image in resized_images:
            sum_image = cv2.add(sum_image, image)
        if isinstance(sum_image, np.ndarray):
            sum_canvas = ImageCanvas(CanvasPanel.get_instance(), id=self.current_id + 1)
            sum_canvas.pack(side='left', fill="both", expand=True)
            sum_canvas.update_idletasks()
            sum_editor = ImageEditor(file_path=None, panel = sum_canvas,image=sum_image)
            self.editors[self.current_id + 1] = sum_editor
            self.set_current_editor(self.current_id + 1)
            self.layers.add_checkbox("imagen", image_id=self.current_id + 1)
            self.current_id += 1
            sum_canvas.update_idletasks()
        else:
            print("Error: La suma de las imágenes no generó un objeto ndarray válido.")

    def subtract_images(self, image_ids):
        images_to_subtract = [self.get_editor(image_id).image_original for image_id in image_ids if self.get_editor(image_id) is not None]
        image1 = images_to_subtract[0]
        image2 = images_to_subtract[1]
        min_width = min(image1.shape[1], image2.shape[1])
        min_height = min(image1.shape[0], image2.shape[0])
        image1 = cv2.resize(image1, (min_width, min_height))
        image2 = cv2.resize(image2, (min_width, min_height))
        diff_image = cv2.subtract(image1, image2)
        if isinstance(diff_image, np.ndarray):
            diff_canvas = ImageCanvas(CanvasPanel.get_instance(), id=self.current_id + 1)
            diff_canvas.pack(side='left', fill="both", expand=True)
            diff_canvas.update_idletasks()
            diff_editor = ImageEditor(file_path=None, panel=diff_canvas, image=diff_image)
            self.editors[self.current_id + 1] = diff_editor
            self.set_current_editor(self.current_id + 1)
            self.layers.add_checkbox("imagen", image_id=self.current_id + 1)
            self.current_id += 1
            diff_canvas.update_idletasks()
        else:
            print("Error: La resta de las imágenes no generó un objeto ndarray válido.")

