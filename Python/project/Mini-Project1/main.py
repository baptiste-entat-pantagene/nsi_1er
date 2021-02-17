from tkinter import *
from functools import partial
import tkinter
import csv
from typing import DefaultDict

class App(tkinter.Tk):
    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        
        self.mainFrame = Frame(self, borderwidth=10, relief=GROOVE)
        self.mainFrame.grid(column=0, row=0)
        self.mainFrame.pack()
        self.createMenu()

        graph = self.createGraph(self.csvToGraphPts("id-1-notes.csv"))
        graph.pack()
    
    def createMenu(self):
        #menu 0
        mainMenu = Menu(self.mainFrame)

        #menu 1
        fileMenu = Menu(mainMenu, tearoff = 0)
        fileMenu.add_command(label = "Open", command = self.load)
        fileMenu.add_command(label = "Save", command = self.save)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command = self.destroy)
        mainMenu.add_cascade(label="File", menu=fileMenu)

        #menu 2
        configMenu = Menu(mainMenu, tearoff= 0)
        configMenu.add_command(label="???")
        mainMenu.add_cascade(label="???", menu=configMenu)
        #final config
        self.config(menu = mainMenu)

    def save(self):
        print("save...")

    def load(self):
        print("load...")

    def createGraph(self, pts):
        w = 500
        h = 500
        graph = Canvas(self, width=w, height=h, background="#E4E4E4")
        graph.create_line(pts, fill="#535353", smooth= False)

        return graph
    
    def csvToGraphPts(self, fileLocation:str):
        reader = csv.DictReader(open(fileLocation), delimiter=";")
        pts = []
        cout = 0
        y = 0
        for raw in reader:
            pts.append(0)
            pts[cout] = (y, int(raw["math"])*3)
            cout += 1
            y += 50
        return pts



app = App()


app.mainloop()
