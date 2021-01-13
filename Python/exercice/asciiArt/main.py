

def repeter_lettres_n_fois(text:str, multi:int):
    index = 0
    buff = ""
    for i in text:
        for ii in range(multi):
            buff += text[index]
        index += 1
    return buff


def repeter_lettres_liste(text, tab):
    buff = ""
    for i in range(len(text)):
        for ii in range(tab[i]):
            buff += text[i]
    return buff

print(repeter_lettres_liste("salut", [4, 1, 4, 1, 5]))




def triangle2(x):
    buff = ""
    for i in range(x, 0, -1):
        buff += (" "*(x-i) + "@"*i + "\n")
    return buff

def triangle3(x):
    buff = ""
    for i in range(x, 0, -1):
        buff +=("@"*i + "\n")
    return buff

def triangle4(x):
    buff = 0
    for i in range(0, x +1):
        if(x ==i ): 
            print("@"*i + "\n")
        else: 
            print(" "*(x -i) + "@" *i)
    return buff

def diagonal(x):
    buff = ""
    for i in range(x, 0, -1):
        buff += " "*(i) + "/\n"
    return buff


def diagonalReverse(x):
    buff = ""
    for i in range(x):
        buff += " "*(i)+"\\\n"
    return buff


print(triangle2(3))

