import tkinter as tk

class Entry(tk.Entry):
    def __init__(self, parent, placeholder, font=("Helvetica", 12), placeholder_color="grey", text_color="black", **kwargs):
        super().__init__(parent, font=font, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.text_color = text_color
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)
        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color and self.get() == self.placeholder:
            self.delete(0, "end")
            self['fg'] = self.text_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()
