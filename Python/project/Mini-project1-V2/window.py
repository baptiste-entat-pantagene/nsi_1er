import Gateway
from functools import partial
import tkinter as tk

class Application(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        self.gateway = Gateway.Gateway(requestMethod=1)

        self.selectFrame = tk.Frame(self).grid(row=0, column=0)
        self.infoFrame = tk.Frame(self)


        self.add_selectFrame()

    def add_selectFrame(self):
        self.productName = tk.StringVar()

        tk.Label(self.selectFrame, text="nom de produit").grid(row=0, column=0)
        tk.Entry(self.selectFrame, textvariable=self.productName).grid(row=1, column=0)
        tk.Button(self.selectFrame,text="validate", command=self.validateSelect).grid(row=2, column=0)

    def validateSelect(self):
        #self.infoFrame.grid(row=0, column=0)

        name = self.productName.get()
        #name = "nutella" #debug var
        dump = self.gateway.requestName(productName=name)
        dump = self.gateway.cleanDump(dump=dump)
        self.productN = self.gateway.getProductInDump(dump=dump, number=0)
        print(self.gateway.getProductFacts(self.productN, option=("name")))
        self.add_infoFrame()
    
    def add_infoFrame(self):
        tk.Label(self.selectFrame, text=str(self.gateway.getProductFacts(self.productN, option=("name")))).grid(row=0, column=1)



    def create_widgets(self, texte = None, command = None):
        self.widget = tk.Button(self)
        self.widget["text"] = texte
        self.widget["command"] = command
        self.widget.pack(side="top")

    def cm_print(self):
        print("hi there, everyone!")
