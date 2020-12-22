"""
Baptiste Entat
20 dec 2020
"""

from classPile import *

#fx code
def statPile(pile):
    print("--->> stats de la pile<<---")
    print("bloc utilisée ->", pile.get_ActualBloc(), "; sur ->", pile.get_Taille())
    print("pile clean ->", pile.get_pile())
    print("pile full ->", pile._pile)



print("--->> start <<---")
#main code

listeDep = [1, 5, 2, 3]
pile = ClassPile(sizePile=None, listIn=listeDep) #creation de la pile
pileWork1 = ClassPile(pile.get_Taille())
pileWork2 = ClassPile(pile.get_Taille())




statPile(pile)

