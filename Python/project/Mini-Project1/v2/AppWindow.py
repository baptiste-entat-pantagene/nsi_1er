"""
Baptiste
Entat
"""
import functools
import tkinter as tk
from functools import partial #passe des arguments aux fonctions
import tkinter.font as tkFont
from typing import Text #police d'écriture

from DataManagement import *


class AppWindow(tk.Tk):
    def __init__(self) -> None:
        tk.Tk.__init__(self)
        """
        self ==> main widows/widget
        """
        
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        

        self.menuFrame = tk.Frame(self, background="#00ffff")
        self.stripFrame = tk.Frame(self, background="#00ffff")
        self.viewFrame = tk.Frame(self, background="#00ffff")

        self.viewSys = ViewSys(self.viewFrame)

        #menuFrame
        self.addMenu(self.menuFrame) #add menu to frame
        self.menuFrame.grid(column=0, row=0, sticky='N W')
        self.menuFrame.columnconfigure(0, weight=1)
        self.menuFrame.rowconfigure(0, weight=1)

        #stripFrame
        self.addStrip(self.stripFrame)
        self.stripFrame.grid(column=1, row=0, sticky='N')
        self.stripFrame.columnconfigure(0, weight=1)
        self.stripFrame.rowconfigure(0, weight=1)

        #viewFrmae
        self.viewFrame.grid(column=1, row=1)
        self.viewFrame.columnconfigure(0, weight=2)
        self.viewFrame.rowconfigure(0, weight=2)
        

    def addMenu(self, rootFrame):
        pathToIcon = os.path.join(os.getcwd(), "icon") # path To Icon

        path = os.path.join(pathToIcon, "services.gif")
        self.imgObjBuff = tk.PhotoImage(name="services", file="services.gif", width=20)
        self.imgObj = self.imgObjBuff.zoom(2) #not zomm !
        #tk.Button(rootFrame, image=self.imgObj).grid(column=0, row=0)
        tk.Button(rootFrame, text="home", command=partial(self.setView, 0)).grid(column=0, row=0)
        tk.Button(rootFrame, text="visualise", command=partial(self.setView, 2)).grid(column=0, row=1)
        tk.Button(rootFrame, text="project Parm..", command=partial(self.setView, 1)).grid(column=0, row=2)
    
    def addStrip(self, rootFrame):
        tk.Button(rootFrame, text="action 1").grid(column=0, row=0)
        tk.Button(rootFrame, text="action 2").grid(column=1, row=0)
        tk.Button(rootFrame, text="action 3").grid(column=2, row=0)
        tk.Button(rootFrame, text="action 4").grid(column=3, row=0)
    
    def resize(self):
        print("(main) winfo_screenmmwidth -->", self.winfo_screenmmwidth())
        print("(main) winfo_screenmmheight -->", self.winfo_screenmmheight())
    
    def setView(self, id:int):
        self.viewSys.setView(id)
    


class ViewSys():
    def __init__(self, p_rootFrame) -> None:
        self.rootFrame = p_rootFrame
        self.frame = tk.Frame(self.rootFrame)


        self.setView(0)

    
    def setView(self, viewId:int):
        """
        0-> home
        1-> param
        2-> visualise
        """
        self.cleanFrame()

        if viewId == 0:
            self.addHome()
            print("view set to home")
        if viewId == 1:
            self.addParam()
            print("view set to projectParam")
        
        if viewId == 2:
            tk.Label(self.frame, text="salut visualise").grid(column=0, row=0)
            print("view set to visualise")
    
    def cleanFrame(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.rootFrame, background="#00ffff")
        self.frame.grid(column=1, row=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
    
    def addHome(self):
        pass
    
    def addParam(self):
        self.headerIndex = ['id', 'surname', 'firstName', 'alias']
        self.listEntryVar = [tk.StringVar()]*len(self.headerIndex)
        for i in range(len(self.headerIndex)):
            self.listEntryVar[i].set(self.headerIndex[i])
            tk.Entry(self.frame, textvariable=self.listEntryVar[i]).grid(column=0, row=i)
            print(".", self.listEntryVar[i].get())