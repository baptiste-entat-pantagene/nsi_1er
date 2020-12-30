"""
Baptiste Entat
20 dec 2020
https://github.com/bapt800/nsi_1er
"""
from classPile import *
print("\n--->> start main.py <<---")
#main code


dictDepartement = {84: "Vaucluse", 4: "Alpes-de-Haute-Provence", 6: "Alpes-Maritimes", 5: "Hautes-Alpes",  13: "Bouches-du-Rhône", 83: "Var"} #dict de base


pile = ClassPile(sizePile=None, listIn=list(dictDepartement.keys()), debugLevel= 1) #creation de la pile -> copie des cles du dict

pile.fx_sort() #tri par ordre croissant
pile.fx_reverse() #passe en ordre décroisant


for i in range(0, pile.get_Taille()): #boucle toute la pile
    print(pile.get_last(), "->", dictDepartement[pile.get_lastAndPop()]) #affiche la cle et le departement puis supprime la cle de la pile



pile.debug_statPile() #stats pour le debug
print("--->> exit main.py <<---\n")