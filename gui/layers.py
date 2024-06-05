from ttkbootstrap import LabelFrame,Treeview,BOTH

class Layers(LabelFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(text="Capas")
        self.setup_layers()
    
    def setup_layers(self):
        tree = Treeview(self,padding=(20,0))
        tree.pack(fill=BOTH,padx=0)

        parent1 = tree.insert('', 'end', text='parent 1', open=True) 
        parent2 = tree.insert('', 'end', text='parent 2')
        
        tree.insert(parent1, 'end', text='child 1')
        tree.insert(parent1, 'end', text='child 2')
        tree.insert(parent2, 'end', text='child 1')
        tree.column('#0', width=0)