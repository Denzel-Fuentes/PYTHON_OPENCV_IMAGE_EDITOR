import ttkbootstrap as tk
from ttkbootstrap.constants import *

class StyleManager:
    def __init__(self, theme='superhero'):
        self.style = tk.Style()
        self.style.theme_use(theme)
        self.configure_styles()

    def configure_styles(self):
        
        self.style.configure('Custom.TButton', font=('Helvetica', 12, 'bold'), foreground='white', background='blue')
        
        self.style.configure('LeftAlign.TButton', 
                        padding =(40,3),
                        font=('Heveltica',10,
                        'bold'),                       anchor='w',
                        relief = 'raise',
                        borderwidth = 1,
                        )
 
        self.style.configure('Custom.TFrame', background='lightgray', relief=tk.RAISED, borderwidth=1)

        # Puedes agregar más configuraciones de estilo aquí
