import Gateway
from functools import partial
import tkinter as tk


class Application(tk.Tk):
    def __init__(self, dataMethod) -> None:
        tk.Tk.__init__(self)
        self.dataMethod = dataMethod
        self.gateway = Gateway.Gateway(requestMethod=dataMethod)

        self.selectFrame = tk.Frame(self)
        self.selectFrame.grid(row=0, column=0)
        self.infoFrame = tk.Frame(self)

        self.add_selectFrame()

    def add_selectFrame(self):
        self.productName = tk.StringVar()

        tk.Label(self.selectFrame, text="nom du produit").grid(row=0, column=0)
        tk.Entry(self.selectFrame,
                 textvariable=self.productName).grid(row=1, column=0)
        tk.Button(self.selectFrame,
                  text="valider",
                  command=self.validateSelect).grid(row=2, column=0)

    def validateSelect(self):
        #self.infoFrame.grid(row=0, column=0)
        name = self.productName.get()
        self.dump = self.gateway.requestName(productName=name)
        self.dump = self.gateway.cleanDump(dump=self.dump)
        tk.Label(text="select one product").grid(row=0, column=2)
        for n in range(3):
            productN = self.gateway.getProductInDump(dump=self.dump, number=n)
            tk.Button(self.selectFrame,
                      text=str(
                          self.gateway.getProductFacts(productN,
                                                       option=("name"))),
                      command=partial(self.chooseProduct, n)).grid(row=n,
                                                                   column=1)

    def chooseProduct(self, n):
        self.productSelected = self.gateway.getProductInDump(dump=self.dump,
                                                             number=n)
        self.switch_infoFrame()

    def switch_infoFrame(self):
        self.selectFrame.destroy()
        self.infoFrame.grid(row=0, column=0)

        buffvar: str = "fiche info de :" + str(
            self.gateway.getProductFacts(self.productSelected,
                                         ("name"))["name"])
        #productName = tk.StringVar().set(buffvar)
        tk.Label(self.infoFrame, text=buffvar).grid(row=0, column=0)

        optionInside = ()
        if self.dataMethod == 0:
            optionInside = ("name", "ingredients", "code", "ecoscore_score",
                            "ecoscore_grade", "nutriscore_grade", "stores",
                            "packaging", "quantity", "brands", "labels")
        elif self.dataMethod == 1:
            optionInside = ("name", "ingredients", "code")

        else:
            raise NotImplementedError("optionInside != 0 and 1 ")

        for i in range(len(optionInside)):
            try:
                msgBuff: str = str(
                    optionInside[i]) + " --> " + self.gateway.getProductFacts(
                        self.productSelected,
                        option=(optionInside[i]))[optionInside[i]]
            except:
                msgBuff: str = str(
                    optionInside[i]) + " --> " + "information inconnu"

            tk.Label(text=msgBuff).grid(row=(i + 2), column=0)
        
        if self.dataMethod == 1:
            tk.Label(text="(if you want more facts, please use online request method)").grid(row=6, column=0)
