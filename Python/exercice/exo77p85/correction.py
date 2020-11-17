def concatenation(t1, t2):
    renvoie = t1[:] + t2[:] # [:] permet de créer un copier des tableaux, sinon ils ne sont que linker
    return renvoie

tab1 = [1, 2, 3]
tab2 = [10, 20, 30]

tabAdd = concatenation(tab1, tab2)
print(tabAdd)


listeX = [[0]*5]*2 #créer un tableau de 2 lignes, chacune remplie avec 5 zéros
listeY = [[0]*5,[0]*5] #Résultat identique qu'à la ligne du dessus

listeX[0][0] = 6 #Mets la valeur 6 dans la case du tableau, première ligne et première colonne
listeY[0][0] = 6 #Résultat identique qu'à la ligne du dessus