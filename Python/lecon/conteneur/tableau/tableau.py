"""tableau en python un premier conteneur"""
"""un tableaupeut contenir n'importe qu'elle type de variable python il est possible de les mélanger"""


tableauVide = [] #Déclaration d'un tableau avec [] --> vide puisqu'il n'y a rien entre les crochets
tableauNombre = [4, 8, 7, 6] #Le tableau est rempli avec les valeurs --> 4, 8, 7, et 6


"""acces au tableau"""
variableGet = tableauNombre[0] #--> Récupère la valeur stockée dans la première case de tableau, donc 4 dans notre exemple
#les cases en mémoire sont numéroté à partir de 0 et non 1 


"""declaration de tableau par comprehension"""
tableauNbPair = [x for x in range(0, 11) if x%2==0] #Remplie le tableau de 0 à 11 et seulement si les valeurs sont paires
print(tableauNbPair)


"""tableau multidimensionnel"""
tableau2D = [[0, 1, 2], [3, 4, 5]]
tableau3D = [[0, 1], [0, 1], [0, 1]]

buff = tableau2D[1][1]
print(buff)