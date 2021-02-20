"""
Baptiste
Entat
"""

from tkinter import *
import tkinter
from functools import partial #passe des arguments aux fonctions
import tkinter.font as tkFont #police d'écriture


class AppWindow(tkinter.Tk):
    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        Label(self, text="salut bg").grid(column=0, row=0)