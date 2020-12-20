

class DataBase:
    def __init__(self):
        
        self.FLuxdata = ""
        self.data = ""
        self.itt = 0
        self.ligneWork = ""
        self.ligneKey = ""

        self.dictData = {}
        self.listEleve = []
        self.listProf = []
        self.listNote = []
    
    def load(self, cheminFichier:str):
        self.Fluxdata = open(cheminFichier, 'r')
        self.data = self.Fluxdata.read()
        print("*->", self.data)
        self.itt = 0
        self.ligneWork = ""
        self.ligneKey = ""
        while self.ligneKey != "$exit": #boucle principale
            print("curent char ->", self.data[self.itt])
            print("ln ->", self.ligneKey)
            if self.data[self.itt] == '$': #cherche une clee
                self.ligneKey = ""
                while self.data[self.itt] != '%':
                    print("curent char ->", self.data[self.itt])
                    print("ln ->", self.ligneKey)
                    self.ligneKey += self.data[self.itt]
                    self.itt +=1

            while self.data[self.itt] != '$': #cherche une donnee
                if self.ligneKey == "$eleve": #pour $eleve
                    self.ReadLigne(self.listEleve) 
                elif self.ligneKey == "$prof": #pour $prof
                    self.ReadLigne(self.listProf) 
#                elif self.ligneKey == "$note": #pour $note
#                    ligneKeyNd = ""
#                    self.ReadLigne()
#                    self.ReadLigne()
#                    if self.ligneWork[0] == '&':
#                        ligneKeyNd = self.ligneWork
#
#                    while self.ligneWork != '%':
#                        self.ReadLigne()




                elif self.ligneKey == "$exit": #si la clee est "$exit" -> sortie du programme
                    break
                else: #gestion de fichier mort
                    print("!!-> erreur dans la base de donnee --> '", cheminFichier, "' <-!!")
                    self.ligneKey = "$exit"
                    break

    def ReadLigne(self, listX = None):
        self.ligneWork = ""
        self.itt += 1
        while self.data[self.itt] != '\n' and self.data[self.itt] != '$':
            print("curent char ->", self.data[self.itt])
            print("ln ->", self.ligneWork)
            self.ligneWork += self.data[self.itt]
            self.itt +=1
        if listX != None and self.ligneWork != '':
            listX.append(self.ligneWork)
        if listX == None and self.ligneWork != '':
            pass #return not implemented
    