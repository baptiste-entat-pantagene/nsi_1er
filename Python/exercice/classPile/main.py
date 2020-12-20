"""
Baptiste Entat
20 dec 2020
"""

#class code
class Pile:
    """
    class pour la gestion d'une pile
    """
    def __init__(self, taillePile:int):
        self._TAILLE = taillePile
        self._pile = [0]* (taillePile + 1)
    
    def app(self, value) -> None:
        """
        ajoute une valeur dans la pile
        """
        if (self._pile[0] + 1) > self._TAILLE:
            print("!-> erreur debordement de la pile <-!")
            return None
        self._pile[self._pile[0] + 1] = value
        self._pile[0] += 1
    
    def pop(self) -> None:
        """
        supprime la derniere valeur de la pile
        """
        if (self._pile[0] + 1) < self._TAILLE:
            print("!-> erreur pile vide <-!")
            return None
        self._pile[self._pile[0]] = 0
        self._pile[0] -= 1

    def reset(self) -> None:
        print("!-> reset not implemented <-!")

    def get_ActualBloc(self) -> int:
        """
        renvoie le nombre de bloc actuellement utilisé dans la pile
        """
        return self._pile[0]
    
    def get_Taille(self) -> int:
        """
        renvoie la taille maximal de la pile
        """
        return self._TAILLE
    
    def printClean(self) -> None:
        """
        affiche evec 'print()' la pile sans l'index
        """
        buff = []
        for i in range(0, self._TAILLE):
            buff.append(self._pile[i + 1])
        print("print clean ->", buff)



#main code

pile = Pile(5) #creation de la pile

pile.app(5)
pile.app(12)
pile.app(88)

pile.app(99) #add
pile.pop() #and supp

pile.reset()

print("bloc utilisée ->", pile.get_ActualBloc(), "; sur ->", pile.get_Taille())
pile.printClean()
print(pile._pile)
