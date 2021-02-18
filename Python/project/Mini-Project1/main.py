from tkinter import *
from functools import partial
import tkinter
import csv
from typing import DefaultDict #tu set à quoi ?

class App(tkinter.Tk):
    def __init__(self) -> None:
        tkinter.Tk.__init__(self)
        
        self.mainFrame = Frame(self, borderwidth=2, relief=GROOVE)
        #self.mainFrame.grid(column=0, row=0)
        self.mainFrame.pack()
        
        #créer le menu
        self.createMenu(self.mainFrame)
        self.accueilFrame = Frame(self.mainFrame)
        self.accueilFrame.grid(column=0, row=0)
        self.accueilFrame.pack
        self.createAccueil(self.accueilFrame)
        
        


        """
        self.graphFrame = Frame(self.mainFrame)
        #self.graphFrame.grid(column=0, row=1)
        self.graphFrame.pack()
        
        graph = Graph(self.graphFrame)
        graph.createGraph(csvToGraphPts("id-1-notes.csv"))
        graph.m_graph.pack()
        """
    
    def createMenu(self, frame):
        #menu 0
        mainMenu = Menu(frame)

        #menu 1
        fileMenu = Menu(mainMenu, tearoff = 0)
        fileMenu.add_command(label = "Open", command= self.load)
        fileMenu.add_command(label = "Save", command= self.save)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command= self.destroy)
        mainMenu.add_cascade(label="File", menu=fileMenu)

        #menu 2
        configMenu = Menu(mainMenu, tearoff= 0)
        configMenu.add_command(label="Accueil", command= self.goToAccueil)
        configMenu.add_command(label="Parametres", command=self.goToParametres)
        mainMenu.add_cascade(label="Panel", menu=configMenu)
        #final config
        self.config(menu = mainMenu)

    def save(self):
        print("save...")

    def load(self, projectPath):
        print("load...", projectPath.get())
        self.csvGest = csvGestion(projectPath)
    
    def createAccueil(self, frame):
        projectPath = StringVar()
        projectPath.set("proj.csv")
        
        Label(frame, text="Accueil").grid(column=0, row=0)
        Entry(frame, textvariable=projectPath).grid(column=0, row=1)
        Label(frame, text="Project Path").grid(column=1, row=1)
        Button(frame, text="Open Project", command=partial(self.load, projectPath)).grid(column=0, row=2)


    def goToAccueil(self):
        self.accueilFrame.grid(column=0, row=0)

    def goToParametres(self):
        self.accueilFrame.grid_forget()

    def createProjTree(self):
        pass



class Graph():
    def __init__(self, frame) -> None:
        self.m_w = 500
        self.m_h = 500
        self.m_graph = Canvas(frame, width=self.m_w, height=self.m_h, background="#E4E4E4")

    def createGraph(self, pts):
        print(pts)
        multX = self.m_w/len(pts)
        multY = self.m_h/len(pts)
        autoPts = [(x*multX, y*2) for x, y in pts]
        self.m_graph.create_line(autoPts, fill="#535353", smooth= False)
        #axe
        self.m_graph.create_text((15, 50), text="notes")

        return self.m_graph

#fx solo
def csvToGraphPts(fileLocation:str):
    reader = csv.DictReader(open(fileLocation), delimiter=";")
    pts = []
    cout = 0
    y = 0
    for raw in reader:
        pts.append(0)
        pts[cout] = (y, int(raw["math"]))
        cout += 1
        y += 1
    return pts

class csvGestion():
    def __init__(self, PathToProject) -> None:
        self.reader = csv.DictReader(open(PathToProject.get()), delimiter=";")
        for row in self.reader:
            print(row)

app = App()


app.mainloop()
