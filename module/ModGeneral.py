"""Module generale"""

class Liste:
    """classe pour le gestion facile des listes"""

    def ___init___(self): #constructeur
        self.liste = [0,1,2,3]


    def affiche(self):
        print(self.liste)
        print("work or not")

    def ajout(self, elmt):
        self.liste[len(self.liste)] = elmt

    

    def Bool(self, elmt):
        """prends un element et une liste et renvoie s'il y est présent"""

        if elmt in self.liste:
            if __name__ == "__main__":
                print("True")
            return True
        else:
            if __name__ == "__main__":
                print("False")
            return False