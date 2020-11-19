

class Tableau:

    def __init__(self, tailleX = 0, tailleY = 0):
        self.tailleX = tailleX
        self.tailleY = tailleY
        
        self.tableau = [[0]*tailleX, [0]*tailleY]
    

    def Reset(self, tailleX = 0, tailleY = 0):
        self.tailleX = tailleX
        self.tailleY = tailleY

        self.tableau = [[0]*tailleX, [0]*tailleY]

    def Set(self, X = 0, Y = 0, valeur = 0):
        """
        prend l'emplacement et le valeur a mettre en memoire
        """

        if X < self.tailleX and  Y < self.tailleY:
            self.tableau[X][Y] = valeur
        else: print("!--> index out of range <--!")

    def Get(self, X = 0, Y = 0):
        return self.tableau[X][Y]

    def AddColumn(self):
        self.tailleX += 1
        self.tailleX += 1