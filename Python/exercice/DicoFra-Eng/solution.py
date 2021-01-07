"""
Baptiste Entat 18 Dec 2020
https://github.com/bapt800/nsi_1er
"""

#1. Choisissez 5 mots de la langue française, et créez le dictionnaire traduction.

traduction = {"ordinateur": "computer", "ordinateur portable": "laptop", "clavier": "keyboard", "souris": "mouse", "écran": "screen"}


#2. Ajoutez une entrée au dictionnaire de la question précédente.
traduction["pomme"] = "apple" #(pomme est une bonne marque d'informatique)


#3. Écrivez une fonction anglais qui affiche, ligne par ligne, tous les mots en anglais du dictionnaire.
def anglais(dictIn:dict):
    for i in dictIn.values():
        print("anglais -->", i)
anglais(traduction)


#4. Écrivez une fonction francais qui affiche, ligne par ligne, tous les mots en français du dictionnaire.
def francais(dictIn:dict):
    for i in dictIn.keys():
        print("français -->", i)
francais(traduction)


#5. Écrivez une fonction ajoute prenant "mot1", "mot2" et "dico" comme arguments (mot1 représente le mot en français, mot2 représente le mot en anglais, 
# et "dico" représente le dictionnaire à modifier), 
# et ajoute cet ensemble dans le dictionnaire uniquement si la clé n'est pas présente dans le dictionnaire.
def ajoute(motFr:str, motAng:str, dictIn:dict):
    if motFr in dictIn:
        pass
    else:
        dictIn[motFr] = motAng
    return dictIn
print(ajoute("garçon de jeu", "Game-Boy", traduction))


#BONUS
#6. Écrivez une fonction "supprime" prenant "lett" et "dico" comme arguments et qui supprime du dictionnaire toutes les entrées dont la clé commence par la lettre lett.
def supp(lett:chr, dictIn:dict):
    dictOut:dict = {}
    for k, v in dictIn.items():
        if k[0] != lett:
            dictOut[k] = v
    return dictOut
print(supp('g', traduction))