from sprite import *

def affiche(obj:sprite):
    buff:str = ""
    for col in range(len(obj._graph)):
        for row in range(len(obj._graph)):
            buff += obj._graph[col][row]
        buff = buff + "\n"
    print(buff)

mario = sprite()

affiche(mario)