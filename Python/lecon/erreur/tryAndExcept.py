"""La structure try et except"""

"""forme complete:
try:
    pass
except expression as identifier:
    pass
else:
    pass
finally:
    pass
"""


try:
    age = int(input("votre age ?\n")) #le programme demande l'age et le stucke dans la variable -->age
except: #si l'utilisateur utilise par exemple des lettre, la conversion en ->int<- de ->age<- par int() vas cree une erreur et ->execpt<- sera executer
    print("vous devez n'utiliser que des nombres...")

print("vous avez donc {age} ans !".format(age = age)) #si tout vas bien le print s'execute.


"""version dans une boucle"""

while True: #avec True la boucle tourne sans jamais s'arreter
    try:
        age = int(input("votre age ?\n"))
        break #permet de sortir de la boucle avant de la finir
    except:
        print("vous devez n'utiliser que des nombres...")
        continue #permet de recomencer au debut de la boucle

print("vous avez donc {age} ans !".format(age = age))