from fonction import *
from dataBase import *

print("\nstart-------start\n")

#entrUti = ""
#entrUti = inputSec("name ?")
#print("-->", entrUti)


dtBs = DataBase()
dtBs.load("data.txt")
print("list eleve ->", dtBs.listEleve)
print("lsit prof ->", dtBs.listProf)
