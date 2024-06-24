from ttkbootstrap import LabelFrame, Button, Scale, Label, Frame
from func.image_manager import ImageEditorManager

class BaseFunctionsPanel(LabelFrame):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.image_editor = ImageEditorManager.get_instance()
        self.configure(text=title)
        self.filter_current = None

    def setup_filters(self):
        raise NotImplementedError("Debe implementar el método setup_filters en la clase derivada.")

    def update_value_label(self, event):
        value = round(self.scale.get())
        self.label_value.config(text=f"{int(value)}")
        value = round(self.scale.get())
        filterClass = type(self.filter_current)
        self.image_editor.current_editor.set_filter(filterClass(value))
        self.image_editor.current_editor.apply_filter(intensity = value)


    def pack_button(self, text, command):
        button = Button(self, text=text, bootstyle="outline", style="LeftAlign.TButton", command=command)
        button.pack(fill='x', anchor='w', pady=4)

    def set_filter(self, filter_strategy):
        self.image_editor.current_editor.set_filter(filter_strategy)
        self.filter_current = filter_strategy
        self.image_editor.current_editor.apply_filter()

    def set_scale(self, from_=0, to=100):
        self.frame = Frame(self)
        self.frame.pack(pady=20)

        self.scale = Scale(self.frame, from_=from_, to=to, orient="horizontal", length=400)
        self.scale.pack(side="top")

        self.label_initial = Label(self.frame, text=f"{from_}")
        self.label_initial.pack(side="left")

        self.label_final = Label(self.frame, text=f"{to}")
        self.label_final.pack(side="right")

        self.label_value = Label(self.frame, text=f"{self.scale.get()}", font=("Arial", 14, "bold"))
        self.label_value.pack(pady=0, side="top")

        self.scale.bind("<B1-Motion>", self.update_value_label)
