#from tkinter import *
from functools import partial
import tkinter as tk

class Application(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)

        self.create_widgets("Hello World\n(click me)", self.cm_print)

    def create_widgets(self, texte = None, command = None):
        self.widget = tk.Button(self)
        self.widget["text"] = texte
        self.widget["command"] = command
        self.widget.pack(side="top")

    def cm_print(self):
        print("hi there, everyone!")
        