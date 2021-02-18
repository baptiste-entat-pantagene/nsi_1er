from tkinter import *
from functools import partial
import tkinter
import csv
from typing import DefaultDict #tu set à quoi ?

class App(tkinter.Tk):
    def __init__(self) -> None:
        tkinter.Tk.__init__(self)

        self.csvGest = csvGestion() #gestionnaire de csv


        self.mainFrame = Frame(self, borderwidth=2, relief=GROOVE)
        #self.mainFrame.grid(column=0, row=0)
        self.mainFrame.pack()
        self.createMenu(self.mainFrame)#créer le menu
        
        
        self.accueilFrame = Frame(self.mainFrame)
        self.accueilFrame.grid(column=0, row=0)
        self.createAccueil(self.accueilFrame)
        

        self.VisualiseFrame = Frame(self.mainFrame)
        self.VisualiseFrame.grid(column=0, row=1)
        #self.VisualiseFrame.pack()
        self.CreateVisualise()
        self.VisualiseFrame.grid_remove()

    
    def createMenu(self, frame):
        #menu 0
        mainMenu = Menu(frame)

        #menu 1
        fileMenu = Menu(mainMenu, tearoff = 0)
        fileMenu.add_command(label="Accueil", command= self.goToAccueil)
        fileMenu.add_command(label="Visualise", command=self.goToVisualise)
        fileMenu.add_separator()
        fileMenu.add_command(label = "Exit", command= self.destroy)
        mainMenu.add_cascade(label="File", menu=fileMenu)


        self.config(menu = mainMenu)

    def save(self):
        print("save...")

    def load(self, projectPath):
        print("load...", projectPath.get())
        self.csvGest.set(projectPath)
        self.goToVisualise()
    
    def createAccueil(self, frame):
        projectPath = StringVar()
        projectPath.set("proj.csv")
        
        Label(frame, text="Accueil").grid(column=0, row=0)
        Entry(frame, textvariable=projectPath).grid(column=0, row=1)
        Label(frame, text="Project Path").grid(column=1, row=1)
        Button(frame, text="Open Project", command=partial(self.load, projectPath)).grid(column=0, row=2)


    
    def CreateVisualise(self):
        #self.VisualiseFrame #use me
        Label(self.VisualiseFrame, text="Visualise").grid(column=0, row=0) #title
        optionList = self.csvGest.getValueProj("Prenom") #get with csvGest(class csvGestion) list of name in proj
        self.v = StringVar()
        self.v.set(optionList[0])
        self.om = OptionMenu(self.VisualiseFrame, self.v, *optionList).grid(column=0, row=1)

        #graph
        graph = Graph(self.VisualiseFrame)
        graph.createGraph(csvToGraphPts("id-1-notes.csv"))
        graph.m_graph.grid(column=1, row=1)


    def goToAccueil(self):
        self.VisualiseFrame.grid_remove()
        self.accueilFrame.grid()

    def goToVisualise(self):
        self.accueilFrame.grid_remove()
        self.VisualiseFrame.grid()
        

    def createProjTree(self):
        pass



class Graph():
    def __init__(self, frame) -> None:
        self.m_w = 500
        self.m_h = 500
        self.m_graph = Canvas(frame, width=self.m_w, height=self.m_h, background="#E4E4E4")

    def createGraph(self, pts) -> Canvas:
        print(pts)
        multX = self.m_w/len(pts)
        multY = self.m_h/len(pts)
        autoPts = [(x*multX, y*2) for x, y in pts]
        self.m_graph.create_line(autoPts, fill="#535353", smooth= False)
        #axe
        self.m_graph.create_text((15, 50), text="notes")

        return self.m_graph

#fx solo -> move
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
    def __init__(self) -> None:
        self.ProjPath = ""
        self.reader = csv.DictReader(open("proj.csv"), delimiter=";")

    def set(self, pathToProject) -> None:
        self.ProjPath = pathToProject
        self.reader = csv.DictReader(open(self.ProjPath.get()), delimiter=";")

    def getValueProj(self, key:str) -> list:
        buff = []
        for row in self.reader:
            buff.append(row[key])
        return buff

app = App()


app.mainloop()
