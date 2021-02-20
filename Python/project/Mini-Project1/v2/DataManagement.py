"""
Baptiste
Entat
"""

import os
import csv


class DataManagement():
    def __init__(self, projectName:str) -> None:
        self.projectName = projectName
        self.basePath = os.getcwd() #base path
        self.dataPath = os.path.join(self.basePath, "data") #data path
        self.projectPath = os.path.join(self.dataPath, projectName) #project path
        self.checkingPathIntegrity(repair=True) #check l'arborescence des fichier

        #print("self.projectPath -->", self.projectPath)
        

    def checkingPathIntegrity(self, repair=True) -> bool:
        """
        return only True if repair == True -> because repare !\n
        if return True -> nice path,
        if return False -> error in path
        """
        #check si le dossier "data" existe
        dirList_BasePath = os.listdir(self.basePath)
        if "data" not in dirList_BasePath:
            if repair == True:
                path = os.path.join(self.basePath, "data")
                os.mkdir(path)
            else:
                return False

        #check si le projet existe
        dirList_DataPath = os.listdir(self.dataPath)
        if self.projectName not in dirList_DataPath:
            if repair == True:
                self.createNewProject()
            else:
                return False

        #check require files
        dirList_ProjectPath = os.listdir(self.projectPath)
        if "index.csv" not in dirList_ProjectPath:
            if repair == True:
                self.createRequireFiles()
            else:
                return False
        
        return True
            
    
    def createNewProject(self) -> None:
        """
        get the "projectName" and create the Paht and require files
        """
        dirList_DataPath = os.listdir(self.dataPath)
        if self.projectName not in dirList_DataPath: #check si le dossier du projet existe
            path = os.path.join(self.dataPath, self.projectName)
            os.mkdir(path)
            print("succesfull -> repare path intergrity to", self.projectName)
        self.createRequireFiles()
        

    def createRequireFiles(self) -> None:
        #create index.csv
        indexFlow = open(os.path.join(self.projectPath, "index.csv"), 'w')
        headerList = ["id", "surname", "firstName", "alias"]
        writerFlow = csv.DictWriter(indexFlow, fieldnames=headerList)    
        writerFlow.writeheader()

        #create I don't know
        #future