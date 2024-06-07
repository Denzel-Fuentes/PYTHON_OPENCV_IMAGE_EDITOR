from ttkbootstrap import Canvas
from func.image_editor import ImageEditor
from tkinter import filedialog
from gui.canvas import ImageCanvas
from gui.canvas_panel import CanvasPanel

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
            editor = ImageEditor(file_path=file_path, canvas=image_canvas.canvas)
            self.editors[self.current_id] = editor
            if self.current_id == 1:
                self.set_current_editor(1)
            return editor

    def get_editor(self, editor_id):
        return self.editors.get(editor_id, None)

    def close_editor(self, editor_id):
        if editor_id in self.editors:
            self.editors[editor_id].canvas.destroy()
            del self.editors[editor_id]

    def set_current_editor(self, editor_id):
        for editor in self.editors.values():
            editor.remove_border()
        self.current_editor = self.get_editor(editor_id)
        if self.current_editor is not None:
            self.current_editor.add_border()
    