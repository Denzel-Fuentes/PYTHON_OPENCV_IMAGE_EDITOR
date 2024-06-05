from ttkbootstrap import HORIZONTAL,GROOVE,PanedWindow,VERTICAL

class CanvasPanel(PanedWindow):
    _instance = None  
    def __init__(self, parent):
        super().__init__(parent,orient=HORIZONTAL)
        if not hasattr(self, 'is_initialized'):
            self.canvas = None
            self.is_initialized = True
            self._instance = self
            
    @classmethod
    def get_instance(cls, parent = None):
        if not cls._instance:
            cls._instance = cls(parent)
        return cls._instance