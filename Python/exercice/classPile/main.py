"""
Baptiste Entat
20 dec 2020
"""

from classPile import *

#fx code
def tri(pileIn:ClassPile):
    """
    tri de la pile avec des Pile(ClassPile)
    """
    pileW1 = ClassPile(pileIn.get_Taille())
    pileW2 = ClassPile(pileIn.get_Taille())

    raise NotImplementedError("!-> not implemented fx() <-!")


print("--->> start <<---")
#main code

listeDep = [9, 1, 2, 3, 4]
pile = ClassPile(sizePile=None, listIn=listeDep) #creation de la pile


print("id ->", id(pile))

print("bloc utilisée ->", pile.get_ActualBloc(), "; sur ->", pile.get_Taille())
print("pile clean ->", pile.get_pile())
print("pile full ->", pile._pile)
