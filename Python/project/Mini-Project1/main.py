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
        self.mainFrame.grid()
        self.createMenu(self.mainFrame)#créer le menu
        
        
        self.accueilFrame = Frame(self.mainFrame)
        self.accueilFrame.grid(column=0, row=0)
        self.createAccueil(self.accueilFrame)
        

        self.VisualiseFrame = Frame(self.mainFrame)
        self.VisualiseFrame
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


    
    def CreateVisualise(self):#self.VisualiseFrame #use me
        #self.controlFrame = Frame(self.VisualiseFrame).grid(column=0, row=0)
        Label(self.VisualiseFrame, text="Visualise", font=("Courier", 24, "italic")).grid(column=0, row=0) #title
        optionList = self.csvGest.getValueProj("Prenom") #get with csvGest(class csvGestion) list of name in proj
        print("optionlIST", optionList)
        self.nameStringVar = StringVar()
        self.nameStringVar.set(optionList[0])
        self.om = OptionMenu(self.VisualiseFrame, self.nameStringVar, *optionList).grid(column=0, row=2)
        Button(self.VisualiseFrame, text="execute", command=partial(self.changeVisualise, self.nameStringVar)).grid(column=1, row=2)

        #graph
        self.graph = Graph(self.VisualiseFrame)
        #graph.createGraph(csvToGraphPts("id-1-notes.csv")) #old
        self.graph.createGraph(self.csvGest.getValue(0, "math"))
        self.graph.m_graph.grid(column=0, row=1)


    def goToAccueil(self):
        self.VisualiseFrame.grid_remove()
        self.accueilFrame.grid()

    def goToVisualise(self):
        self.accueilFrame.grid_remove()
        self.VisualiseFrame.grid()
        
    def changeVisualise(self, nameVar):
        newName = nameVar.get()
        print("newName->", newName)

        self.graph.createGraph(self.csvGest.getValue(self.csvGest.dictNametoId[newName], "math"))
        self.graph.m_graph.grid(column=0, row=1)

    def createProjTree(self): #future
        pass



class Graph():
    def __init__(self, frame) -> None:
        self.m_w = 500
        self.m_h = 500
        self.m_graph = Canvas(frame, width=self.m_w, height=self.m_h, background="#E4E4E4")

    def createGraph(self, pts) -> Canvas:
        multX = self.m_w/len(pts) #scale
        multY = self.m_h/20 #scale
        autoPts = []
        for i in range(len(pts)):
            buffX = i*(multX) #base
            buffY = float(pts[i])*(multY) #base
            #buffX = self.m_w - buffX
            #buffY = self.m_h - buffY
            autoPts.append((buffY, buffX))
        

        self.m_graph.create_line(autoPts, fill="#535353", smooth= True) #ligne
        
        #axe && annotation
        self.m_graph.create_text((15, 50), text="notes") #text

        return self.m_graph


def csvToGraphPts(fileLocation:str): #depreced!
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
        
        buffReader = csv.DictReader(open("proj.csv"), delimiter=";")
        self.dictNametoId = {} #by pass
        self.dictIdToName = {} #by pass
        for row in buffReader:
            self.dictIdToName[row["id"]] = row["Prenom"]
            self.dictNametoId[row["Prenom"]] = int(row["id"])
        print(self.dictNametoId, "<-->" , self.dictIdToName)
        

    def set(self, pathToProject) -> None:
        self.ProjPath = pathToProject
        self.reader = csv.DictReader(open(self.ProjPath.get()), delimiter=";")

    def getValueProj(self, key) -> list:
        buff = []
        for row in self.reader:
            buff.append(row[key])
        return buff
    
    def getSubLocation(self, id):
        return "id-"+ str(id)+ "-notes"+ ".csv"

    def getValue(self,id, key) -> list:
        buffreader = csv.DictReader(open(self.getSubLocation(id)), delimiter=";")
        buffList = []
        for row in buffreader:
            buffList.append(row[key])
        return buffList
    

app = App()


app.mainloop()
