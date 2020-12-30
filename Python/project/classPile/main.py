"""
Baptiste Entat
20 dec 2020
"""

from classPile import *

#fx code




print("\n--->> start main.py <<---")
#main code

listeDep = (1, 5, 2, 3)

pile = ClassPile(sizePile=4, listIn=None, debugLevel= 1) #creation de la pile


pile.pushList(listeDep)
pile.debug_statPile()


print("--->> exit main.py <<---\n")