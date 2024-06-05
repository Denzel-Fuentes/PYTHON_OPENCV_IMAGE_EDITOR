from ttkbootstrap import LabelFrame,Button

from filters.blur import BlurFilter

class Filters(LabelFrame):
    def __init__(self,parent,image_editor):
        super().__init__(parent)
        self.image_editor = image_editor
        self.configure(text="Filtros")
     
    def setup_filters(self):
       self.pack_button( text="Gauss", command=lambda:self.set_filter(BlurFilter()))
       self.pack_button( text="Blurred",command=lambda: self.set_filter(BlurFilter()))
       self.pack_button( text="Deteccion de Bordes",command=lambda:self.set_filter(BlurFilter()))
       self.pack_button( text="Lapalce",command=lambda :print("seleccionar"))
       self.pack_button( text="x-y sobel",command=lambda :print("seleccionar"))
       self.pack_button( text="Canny",command=lambda :print("seleccionar"))
    
    def pack_button(self,text,command):
        button = Button(self, text=text,bootstyle="outline", style="LeftAlign.TButton", command=command)
        button.pack(fill='x', anchor='w', pady=4)
    
    def set_filter(self, filter_strategy):
        self.image_editor.set_filter(filter_strategy)
        self.image_editor.apply_filter()