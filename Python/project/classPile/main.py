"""
Baptiste Entat
20 dec 2020
"""

from classPile import *

#fx code




print("\n--->> start main.py <<---")
#main code

dictDepartement = {84: "Vaucluse", 4: "Alpes-de-Haute-Provence", 6: "Alpes-Maritimes", 5: "Hautes-Alpes",  13: "Bouches-du-Rhône", 83: "Var"}


pile = ClassPile(sizePile=None, listIn=list(dictDepartement.keys()), debugLevel= 1) #creation de la pile

pile.fx_sort() #ordre croisant
pile.fx_reverse() #-> passer en ordre decroisant

for i in range(0, len(dictDepartement)):
    print(pile.get_last(), "->", dictDepartement[pile.get_lastAndPop()])


pile.debug_statPile()
print("--->> exit main.py <<---\n")