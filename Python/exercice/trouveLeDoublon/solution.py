listeDoublons:list = [0, 1, 1, 1, 2, 4, 5, 1, 7, 1, 0, -5]

def doublon(listeIn:list):
    """
    Prends une liste en entrée et revoie une même liste mais sans les doublons qui y sont présents, 
    affiche aussi les doublons incriminés.
    """
    listeOut = []
    listeIn.sort()
    for x in range(0, len(listeIn)):
        if listeIn[x-1] == listeIn[x]:
            print("Le(s) doublon(s) est/sont -->", listeIn[x])
        else:
            listeOut.append(listeIn[x])
    return listeOut


print(doublon(listeDoublons))
