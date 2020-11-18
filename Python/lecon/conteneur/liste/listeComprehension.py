"""listeComprehension"""

listeBasic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste = [x for x in range(11)]
print(listeBasic)
print(liste)

listeDeNbPair = [x for x in range(0, 11) if x%2==0] #Remplie le tableau de 0 à 10 et seulement si les valeurs sont paires
print(listeDeNbPair)