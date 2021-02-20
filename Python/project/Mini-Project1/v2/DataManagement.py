"""
Baptiste
Entat
"""

import os
import csv


class DataManagement():
    def __init__(self, ProjectName:str) -> None:
        self.basePath = os.getcwd() #base path
        self.dataPath = os.path.join(self.basePath, "data") #paht to data folder
        self.checkingPathIntegrity(ProjectName, repair=True) #check l'arborescence des fichier
        
        print(self.dataPath)
        

    def checkingPathIntegrity(self, ProjectName:str, repair=True) -> bool:
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
        if ProjectName not in dirList_DataPath:
            if repair == True:
                self.createNewProject(ProjectName)
            else:
                return False
        
        return True
            
    
    def createNewProject(self, ProjectName:str) -> None:
        """
        get the "ProjectName" and create the Paht and require files
        """
        dirList_DataPath = os.listdir(self.dataPath)
        if ProjectName not in dirList_DataPath: #check si le dossier du projet existe
            path = os.path.join(self.dataPath, ProjectName)
            os.mkdir(path)
            print("succesfull -> repare path intergrity to", ProjectName)
        
