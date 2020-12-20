"""
Baptiste Entat
20 dec 2020
"""

#class code
from classPile import *

print("--->> start <<---")
#main code

pile = Pile(5) #creation de la pile

pile.app(5)
pile.app(12)
pile.app(88)


pile.setSize(1, 1)


pile.app(72) #add
#pile.pop() #and supp



print("bloc utilisée ->", pile.get_ActualBloc(), "; sur ->", pile.get_Taille())
print("clean ->", pile.get_pile())
print("full ->", pile._pile)
