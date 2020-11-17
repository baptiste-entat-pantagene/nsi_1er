def concatenation(t1, t2):
    renvoie = t1[:] + t2[:]
    return renvoie

tab1 = [1, 2]
tab2 = [3, 4]

tab1ET2 = concatenation(tab1, tab2)
print(tab1ET2)