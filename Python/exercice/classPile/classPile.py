"""
Baptiste Entat
20 dec 2020
"""
class Pile:
    """
    class pour la gestion d'une pile
    """
    def __init__(self, sizePile:int):
        """
        please complete me
        """
        self._pile = [0]* (sizePile + 1)
        #self._pile[0] = 0 
        self._size = sizePile

    def setSize(self, sizePile:int, dataMod:int = 0) -> None:
        """
        change la taille de la pile;
        dataMod: 0->suppression, 1->mode conservation, 2->conservation partiel
        """
        if dataMod == 0: #dataMod: 0->suppression
            self._pile = [0] * (sizePile + 1)
            self._size = sizePile
        elif dataMod == 1: #dataMod: 1->mode conservation, 2->conservation partiel
            if sizePile < self._size:
                raise Warning("Perte de donnee possible")
            else:
                for i in range(0, sizePile - self._size + 1):
                    self._pile.append(0)
                self._size = sizePile
        elif dataMod == 2: #dataMod: 2->conservation partiel
            buff = self._pile[:]
            self._pile = [0] * (sizePile + 1)
            for i in range(0, sizePile):
                self.app(buff[i+1])
            self._size = sizePile
        else:
            raise ValueError("fatal error, class 'Pile.setSize'")

    def clear(self) -> None:
        for i in range(0, self._size):
            self._pile[i] = 0


    def app(self, value) -> None:
        """
        ajoute une valeur dans la pile
        """
        if (self._pile[0] + 1) > self._size:
            print("!-> erreur debordement de la pile <-!")
            return None
        else:
            self._pile[self._pile[0] + 1] = value
            self._pile[0] += 1
    
    def pop(self) -> None:
        """
        supprime la derniere valeur de la pile
        """
        if (self._pile[0] + 1) < self._size:
            print("!-> erreur pile vide <-!")
            return None
        else:
            self._pile[self._pile[0]] = 0
            self._pile[0] -= 1


    def get_ActualBloc(self) -> int:
        """
        renvoie le nombre de bloc actuellement utilisé dans la pile
        """
        return self._pile[0]
    
    def get_Taille(self) -> int:
        """
        renvoie la taille maximal de la pile
        """
        return self._size
    

    def get_pile(self) -> list:
        """
        renvoie la pile sans l'index sous forme de liste
        """
        buff = []
        for i in range(0, self._size):
            buff.append(self._pile[i + 1])
        return buff
    