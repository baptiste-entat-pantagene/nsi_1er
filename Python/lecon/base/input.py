"""utlisation de input en python"""

print("\n\nexemple basic")
"""exemple basic"""
ageUtilisateur = input("qu elle age avez vous ?\n") # \n permet de passer a la ligne dans la console (peut aussi etre utiliser avec print)
#il est possible de mettre du texte directement dans input
#la valeur que lutilisateur a entrer est stocker dans la variable ageUtilisateur
print("Vous avez {age} ans !".format(age = ageUtilisateur)) #voir lecon/base/HelloWorld pour .format


print("\n\nversion protégée")
"""version protégée"""
while True:
    try: #pour try/except voir lecon/erreur/tryAndExcept
        enteUtilisateur = input("qu elle age avez vous ?\n")
        ageUtilisateur = int(enteUtilisateur)
        break

    except:
        print("veullier n'utiliser que des chiffres")
        continue

print("Vous avez {age} ans !".format(age = ageUtilisateur))