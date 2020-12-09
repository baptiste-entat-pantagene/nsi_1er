#dict de base
boutique_dico = {"modèle": "laptop" , "constructeur": "HP" , "RAM": "16G" , "corei7-4700HQ": "processeur", "stockage": "500 Go", "français":"clavier"}


#1) Corriger une erreur de référencement "stockage" vaut "1 To"
boutique_dico["stockage"] = "1 To" #modifie la valeur "1 To" pour la clée "stockage"


#2) Écrire l’instruction pour ajouter la paire clé-valeur : "Système d'exploitation" : "Windows 10"
boutique_dico["Système d'exploitation"] = "Windows 10" #affecte la valeur "Windows 10" a la clée "Système d'exploitation"


#3) Écrire un programme qui affiche la liste des clés, la liste des valeurs et la liste des paires de clés et valeurs
for i in boutique_dico.keys(): #print keys
    print("keys-->", i)

for i in boutique_dico.values(): #print values
    print("values--> ", i)

for k, v in boutique_dico.items(): #print keys and values
    print("keys->", k, "; values->", v)


#4) Écrire à la suite de votre programme les instructions pour inverser les paires de clés et valeurs erronées pour "processeur" et "clavier", en complétant cette structure
boutiqueDicoNice:dict = {} #new dict
for k, v in boutique_dico.items(): #cherche ligne par ligne dans le dict avec k->key et v->value
    if v == "processeur" or v == "clavier": #la valeur match avec "processeur" ou(or) "clavier"
        boutiqueDicoNice[v] = k #inverse la clée est la valeur
    else: boutiqueDicoNice[k] = v #copie la ligne du dict
print(boutiqueDicoNice) #affiche le nouveau dict


#5) Écrire une création de dictionnaire par compréhension qui inverse toutes les clés-valeurs de boutique_dico_ok
inversionDictNice:dict = {v : k for k, v in boutiqueDicoNice.items()} #boucle dans boutiqueDicoNice et affecte pour chaque itteration k->key et v->value (k, v->variable temp) puis affecte dans le dict v : k (inversion clees et valeurs)
print(inversionDictNice) #affiche le nouveau dict