"""boucleWhile"""
"""prend en argument une condition avec des valeur ou variable
    liste des operateur
    ==, !=, <, >, =<, =>
    liste des condition suplementaire possible
    and, or, not, ?
"""

"""forme:

while expression:
    pass

pass --> il n'est présent que dans les code snippet pour eviter les erreur d'execution lorsque la boucle est vide, donc pas present dans les vrai code)
break --> permet de sortir de la boucle
continue --> permet de remonter au debut de la boucle
"""


nombre = 1
while nombre < 100:
    nombre += 1.5
    print(nombre)

while nombre 

"""version avec try et except"""

while True: # True permet de tourner sans fin
    try:
        age = int(input("votre age ?\n"))
        break #permet de sortir de la boucle avant de la finir
    except:
        print("vous devez n'utiliser que des nombres...")
        continue #permet de recomencer au debut de la boucle

print("vous avez donc {age} ans !".format(age = age))