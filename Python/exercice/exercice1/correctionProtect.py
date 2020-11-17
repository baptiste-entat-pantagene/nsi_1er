"""crorectionProtect"""

while True:
    try:
        ageUti = int(input("Veillez entre votre âge\n"))
        break
    except:
        print("Veuillez n'utiliser que des nombres\n\n")
        continue

print("Vous êtes donc née en {time}".format(time=2020-ageUti))