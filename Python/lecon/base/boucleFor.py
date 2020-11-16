"""boucleFor"""
"""La boucle for peut prendre range() en argument,
    range() luis prend en argument -> un point de depart (souvent 0), un pooint de fin (3 dans l'exemple 1) et un pas (si non mentionner =1 -> exemple 1)
    La boucle For dois aussi avoir une variable pour itterer (compter) elle est accesible librement en python"""

"""forme:

for target_list in expression_list:
    pass

"""

print("\nexemle 1:")
for a in range(0, 3): #For s'arrete avant d'atteindre 3, donc a 2
    print(a)


print("\nexemle 2:")
for b in range(3, 0, -1): # il est possible d'iterer a l'enver
    print(b)

#il n'est passible d'utiliser de nombre flotant avec For