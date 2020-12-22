"""
Baptiste Entat
20 dec 2020
"""
from typing import List


class ClassPile:
    """
    class pour la gestion d'une pile
    """
    def __init__(self, sizePile:int = None, listIn:list = None):
        """
        sizePile = Int, listIn = None -> pile de la taille de sizePile;
        sizePile = None, listIn = lst -> copie de la liste dans la pile
        """
        if sizePile != None and listIn == None:
            self._pile = [0]* (sizePile + 1)
            #self._pile[0] = 0 
            self._size = sizePile
        elif sizePile == None and listIn != None:
            self._pile = []
            self._pile.append(len(listIn))
            for i in listIn:
                self._pile.append(i)
            self._size = len(listIn)
        else:
            raise NotImplementedError("!-> not implemented param <-!")


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
        self._pile = [0] * (self._size + 1)

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

    def appList(self, listIn):
        if listIn is list == False and listIn is tuple == False:
            raise NotImplementedError("!-> not implemented type ", type(listIn), " <-!")
        elif (self._pile[0] + len(listIn)) > self._size:
            print("!-> erreur debordement de la pile <-!")
            return None
        iList = 0
        for i in range(self._pile[0], self._pile[0] + len(listIn)):
            self._pile[i + 1] = listIn[iList]
            self._pile[0] += 1
            iList += 1
            
    
    def pop(self) -> None:
        """
        supprime la derniere valeur de la pile
        """
        if (self._pile[0]) < 0:
            print("!-> erreur pile vide <-!")
            return None
        else:
            self._pile[self._pile[0]] = 0
            self._pile[0] -= 1
    

    #section get
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

    def get_last(self):
        """
        renvoie le dernier element la pile
        """
        return self._pile[self._pile[0]]
    
    def get_lastAndPop(self):
        """
        renvoie le dernier element la pile et le supp
        """
        buff = self.get_last()
        self.pop()
        return buff
    

    #section Fx
    def fx_reverse(self) -> None:
        """
        inverse la pile
        """
        pileWork:list = self.get_pile()
        pileWork.reverse()
        self.clear()

        for i in range(0, len(pileWork)):
            print("index ->", i)
            print("cont ->", pileWork[i])
            self.app(pileWork[i])
            


#raise NotImplementedError("!-> not implemented <-!")
