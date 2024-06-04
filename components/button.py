import tkinter as tk

class Button(tk.Button):
    def __init__(self, parent, text, command, bg="blue", fg="white", font=("Helvetica", 12), **kwargs):
        super().__init__(parent, text=text, command=command, bg=bg, fg=fg, font=font, **kwargs)
        self.default_bg = bg
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground'] if 'activebackground' in self.keys() else "lightgray"

    def on_leave(self, e):
        self['background'] = self.default_bg
