class Personnage:
    
    def __init__(self, nomPersonnage = "", degatPersonnage= 10, vitessePersonnage= 10):
        self.nom= nomPersonnage
        self.degat = degatPersonnage
        self.vitesse= vitessePersonnage
    
    def AfficheStat(self):
        print(self.nom)
        print(self.degat)
        print(self.vitesse)


