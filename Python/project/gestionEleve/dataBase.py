from os import getlogin


class DataBase:
    def __init__(self):
        
        self.FLuxdata = ""
        self.data = ""

        self.listEleve = []
        self.listProf = []
    
    def load(self, cheminFichier:str):
        self.Fluxdata = open(cheminFichier, 'r')
        data = self.Fluxdata.read()
        print("*->", data)
        itt = 0
        ligneWork = ""
        ligneKey = ""
        while ligneKey != "$exit":
            print("curent char ->", data[itt])
            print("ln ->", ligneKey)
            if data[itt] == '$':
                ligneKey = ""
                while data[itt] != '%':
                    print("curent char ->", data[itt])
                    print("ln ->", ligneKey)
                    ligneKey += data[itt]
                    itt +=1
            while data[itt] != '$':
                if ligneKey == "$eleve":
                    ligneWork = ""
                    itt += 1
                    while data[itt] != '\n' and data[itt] != '$':
                        print("curent char ->", data[itt])
                        print("ln ->", ligneWork)
                        ligneWork += data[itt]
                        itt +=1
                    if ligneWork != '':
                        self.listEleve.append(ligneWork)
                elif ligneKey == "$prof":
                    ligneWork = ""
                    itt += 1
                    while data[itt] != '\n' and data[itt] != '$':
                        print("curent char ->", data[itt])
                        print("ln ->", ligneWork)
                        ligneWork += data[itt]
                        itt +=1
                    if ligneWork != '':
                        self.listProf.append(ligneWork)
                elif ligneKey == "$exit":
                    break
