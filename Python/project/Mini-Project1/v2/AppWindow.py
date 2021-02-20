"""
Baptiste
Entat
"""

from tkinter import *
import tkinter
from functools import partial #passe des arguments aux fonctions
import tkinter.font as tkFont #police d'écriture

from DataManagement import *


class AppWindow(tkinter.Tk):
    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        """
        self ==> main widows/widget
        """
        self.addMenu() #add menu to widget
        Label(self, text="salut bg").grid(column=0, row=0)

    def addMenu(self):
        #menu (base)
        mainMenu = Menu(self)

        #menu 1
        fileMenu = Menu(mainMenu, tearoff = 0)
        fileMenu.add_command(label="Accueil") #,comand=
        fileMenu.add_command(label="Visualise")
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command= self.destroy)
        mainMenu.add_cascade(label="File", menu=fileMenu)


        self.config(menu = mainMenu)