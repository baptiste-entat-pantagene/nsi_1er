"""liste.py"""

liste = [] #--> liste vide
liste = [1, 3, "cafet"]
print(liste)


variableGet = liste [0]
print(liste [0])
#--> Récupère la valeur stockée dans la première case préciser entre les crochets

print("len liste = ", len(liste))

liste.append("new") #--> Insert un élément à la fin de la liste
print(liste)

liste.insert(0, "first") #--> Insert un élément a la position donnée, donc en 1er
print(liste)