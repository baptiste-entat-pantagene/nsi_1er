def maxi(tab):
    m = tab[0]
    for x in tab:
        if x[1] >= m[1]:
            m = x
    return m

L = [('Adrien', 17), ('Barnabé', 17), ('Casinir', 17), ('Dorian', 17), ('Emilien', 16), ('Fabien', 16)]
print(maxi(L))
