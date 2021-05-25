import tkinter as tk
from systemeMonetaire import *


class Application(tk.Tk):  # delete master
    def __init__(self):
        tk.Tk.__init__(self)

        self.gestM = GestionMonetaire()
        self.gestM.set_compte_exemple()

        self.frame_compte = tk.Frame(self)
        self.frame_compte.grid(column=1, row=1)

        self.frame_rendu = tk.Frame(self)
        self.frame_rendu.grid(column=2, row=1)
        
        self.entry_var = tk.StringVar()

        self.create_base()
        self.update_widget_compte()


    def create_base(self):
        self.entry = tk.Entry(self, textvariable=self.entry_var)
        self.entry.grid(column=1, row=0)

        self.button_calc = tk.Button(self, text="calc", command=self.calculate)
        self.button_calc.grid(column=0, row=0)

    def update_widget_compte(self):
        col = 0
        ro = 0

        label = tk.Label(self.frame_compte, text="monnaies dans le compte: ")
        label.grid(column=col, row=ro)
        ro += 1

        compte:dict = self.gestM.get_compte()
        for key, val in compte.items():
            label = tk.Label(self.frame_compte, text=str(str(key) + "€ -> il en reste :" + str(val)))
            label.grid(column=col, row=ro)
            ro += 1

    def update_widget_rendu(self):
        lstRendu:dict = self.gestM.renduMonnaies(float(self.entry_var.get()))

        ro = 0
        label = tk.Label(self.frame_compte, text="pieces à rendre: ")
        label.grid(column=1, row=ro)
        ro += 1
        for key, val in lstRendu.items():
            label = tk.Label(self.frame_compte, text=str(str(key) + "€ -> il en faut :" + str(val)))
            label.grid(column=1, row=ro)
            ro += 1
        
    def resetFrame(self):
        self.frame_rendu.destroy()
        self.frame_rendu = tk.Frame(self)
        self.frame_rendu.grid(column=2, row=1)

        self.frame_compte.destroy()
        self.frame_compte = tk.Frame(self)
        self.frame_compte.grid(column=1, row=1)


    def calculate(self):
        self.resetFrame()
        self.update_widget_rendu()
        self.update_widget_compte()
        
