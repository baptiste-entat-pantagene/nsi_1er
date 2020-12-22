import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets("Hello World\n(click me)", self.cm_print)

    def create_widgets(self, texte = None, command = None):
        self.widget = tk.Button(self)
        self.widget["text"] = texte
        self.widget["command"] = command
        self.widget.pack(side="top")

    def cm_print(self):
        print("hi there, everyone!")
        