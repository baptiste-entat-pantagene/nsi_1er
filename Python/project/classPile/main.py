"""
Baptiste Entat
20 dec 2020
"""

from classPile import *

#fx code



print("--->> start <<---")
#main code

listeDep = [2, 13, 22, 33, 44]
pile = ClassPile(sizePile=None, listIn=listeDep) #creation de la pile


pile.fx_reverse()


print("--->> stats <<---")
print("bloc utilisée ->", pile.get_ActualBloc(), "; sur ->", pile.get_Taille())
print("pile clean ->", pile.get_pile())
print("pile full ->", pile._pile)
