"""Hello World"""
print("hello world")


maVariableInt = 0
maVariableBool = True
maVariableString = "abc"
print("ma premiere variable ==>", maVariableInt,
        "puis ==>", maVariableBool,
        "puis ==>", maVariableString) #il est possible d'écrire sur plusieurs lignes entre les ()
        #print peut afficher des variable de tout type


"""premiere utilisation de .format"""
ageUtilisateur = 16
print("vous avez : {age} ans !".format(age = ageUtilisateur)) #.format permet d'avoir un code plus lisible et facile a modifier
