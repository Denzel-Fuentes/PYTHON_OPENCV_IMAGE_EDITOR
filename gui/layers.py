from tkinter import LabelFrame, IntVar, Checkbutton, Button, Tk



class Layers(LabelFrame):
    _instance = None

    def __init__(self, parent):
        if Layers._instance is not None:
            raise Exception("Singleton ya creado!")
        else:
            super().__init__(parent)
            self.configure(text="Imagenes")
            self.check_vars = []
            self.checkbuttons = []
            self.create_buttons()
            Layers._instance = self

    def create_buttons(self):
       
        self.sumar_button = Button(self, text="Sumar", command=self.sum_selected)
        self.sumar_button.pack(fill='x', anchor='w', pady=2, padx=10) 
        self.restar_button = Button(self, text="Restar", command=self.sub_selected)
        self.restar_button.pack(fill='x', anchor='w', pady=2, padx=10) 

        self.sumar_button.pack(side='bottom', pady=5)
        self.restar_button.pack(side='bottom', pady=5)

    def add_checkbox(self, text, image_id):
        var = IntVar()
        text = text+" - " + str(image_id)
        checkbutton = Checkbutton(self, text=text, variable=var)
        checkbutton.pack(anchor='w', padx=20, pady=5)
        checkbutton.var = var
        checkbutton.image_id = image_id
        self.check_vars.append(var)
        self.checkbuttons.append(checkbutton)
        var.trace_add('write', self.limit_checkboxes)

    def limit_checkboxes(self, *args):
        selected = [cb for cb in self.checkbuttons if cb.var.get() == 1]
        if len(selected) > 2:
            for cb in selected[2:]:
                cb.var.set(0)

    def sum_selected(self):
        from func.image_manager import ImageEditorManager
        imageEditorManager = ImageEditorManager.get_instance()

        selected_ids = [cb.image_id for cb in self.checkbuttons if cb.var.get() == 1]
        imageEditorManager.sum_images(selected_ids)

    def sub_selected(self):
        from func.image_manager import ImageEditorManager
        imageEditorManager = ImageEditorManager.get_instance()

        selected_ids = [cb.image_id for cb in self.checkbuttons if cb.var.get() == 1]
        imageEditorManager.subtract_images(selected_ids)
    
    def remove(self, image_id):
        for idx, cb in enumerate(self.checkbuttons):
            if cb.image_id == image_id:
                cb.destroy()  
                del self.checkbuttons[idx]  
                del self.check_vars[idx]  
                break
    @staticmethod
    def get_instance(parent=None):
        if Layers._instance is None:
            if parent is None:
                raise ValueError("Se necesita un componente padre para crear la instancia de Layers.")
            Layers(parent)
        return Layers._instance