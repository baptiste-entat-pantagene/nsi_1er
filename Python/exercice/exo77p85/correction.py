def concatenation(t1, t2):
    renvoie = t1[:] + t2[:] # [:] permet de créer un copier des tableaux, sinon ils ne sont que linker
    return renvoie

tab1 = [1, 2, 3]
tab2 = [10, 20, 30]

tabAdd = concatenation(tab1, tab2)
print(tabAdd)
