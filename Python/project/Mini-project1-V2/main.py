import os

from requests.api import options
import Gateway


def cls():
    """
    clear console
    """
    os.system('cls' if os.name=='nt' else 'clear')


def inputSecured(msg, returnType:str):
    """
    returnType: "int", "str", "bool"(yes/no)
    """
    while True:
        print(msg)
        buff = input()

        if returnType == "int":
            if buff == "":
                continue
            try:
                int(buff)
            except:
                continue
            return int(buff)
        elif returnType == "str":
            if buff == "":
                continue
            return buff
        elif returnType == "bool":
            if buff == "":
                continue
            elif buff == "yes":
                return True
            elif buff == "no":
                return False
        else:
            raise NotImplementedError()



selectedDisplaySystem = 0
dataMethod = 0

"""
#select display system
while True:
    print("--> Start <--")

    answer = inputSecured(msg="Choose the display system\n  Console -> 0\n  TKinter -> 1 (TKinter is only a test)", returnType="int")
    if answer == 0:
        selectedDisplaySystem = 0
        break
    elif answer == 1:
        selectedDisplaySystem = 1
        raise NotImplementedError()
        break
    else:
        print("Please retry")
        continue

cls()
#select request mode
while True:
    answer = inputSecured(msg="Select the request data system\n  Online -> 0 (need some library)\n  Off-line -> 1 (need a large csv file -> not on github)", returnType="int")
    if answer == 0:
        #check si les dépendences existe
        dirList_BasePath = os.listdir(os.getcwd())
        if "requests" not in dirList_BasePath:
            raise NotADirectoryError("We need requests module")
        elif "urllib3" not in dirList_BasePath:
            raise NotADirectoryError("We need urllib3 module")
        elif "chardet" not in dirList_BasePath:
            raise NotADirectoryError("We need chardet module")
        elif "certifi" not in dirList_BasePath:
            raise NotADirectoryError("We need certifi module")
        elif "idna" not in dirList_BasePath:
            raise NotADirectoryError("We need idna module")

        print("Successful selection of the online mode")
        dataMethod = 0
        break
     
    elif answer == 1:
        #check si la dépendence existe
        dirList_BasePath = os.listdir(os.getcwd())
        if "fr-openfoodfacts-org-products.csv" not in dirList_BasePath:
            raise NotADirectoryError("We need fr-openfoodfacts-org-products.csv file")

        print("Successful selction of the off-line mode")
        dataMethod = 1
        break
    else:
        print("Please retry")
        continue
cls()
"""

def launchConsole(dataMethod):
    gateway = Gateway.Gateway(requestMethod=dataMethod)
    cls()
    while True:
        #event = inputSecured("select action\n    0 -> request ID\n    1 -> request name (generique)\n   -1 -> exit", "int")
        event=0 #debug var
        dump = gateway.requestID("3017620425035") #id
        if event == 0:
            cls()
            #id = inputSecured("type the id of product", "str")
            dump = gateway.requestID("3017620425035") #id
            #3017620425035 #nutella
            #000000001576 #quik test
            #0000000001199 #quik test
        elif event == 1:
            cls()
            #name = inputSecured("type the name", "str")
            name = "nutella" #debug var
            dump = gateway.requestName(productName=name)

        dump = gateway.cleanDump(dump=dump)
        product1 = gateway.getProductInDump(dump=dump, number=0)
        buffMsg = ("We found a match for -> " + str(gateway.getProductFacts(product1, name=True)) + "\n     -> type 'yes' or 'no' for confirm product")
        
        #confirmProduct = inputSecured(buffMsg, "bool")
        confirmProduct = True #debug var
        if confirmProduct == True:
            cls()
            while True:
                select = inputSecured("Select facts\n     0 -> name\n     -1 -> most important data", returnType="int")
                if select == 0:
                    print("product name -->", gateway.getProductFacts(product1, name=True))
                elif select == -1:
                    print("product name -->", gateway.getProductFacts(product1, name=True))
                else:
                    print("Please retry")
                    continue

        elif confirmProduct == False:
            print("aaaaaahhh")


        elif event == -1:
            print(" ▄▄▄▄    ▄▄▄      ▓██   ██▓\n▓█████▄ ▒████▄     ▒██  ██▒\n▒██▒ ▄██▒██  ▀█▄    ▒██ ██░\n▒██░█▀  ░██▄▄▄▄██   ░ ▐██▓░\n░▓█  ▀█▓ ▓█   ▓██▒  ░ ██▒▓░\n░▒▓███▀▒ ▒▒   ▓▒█░   ██▒▒▒")
            exit()
        else:
            continue
        break #after please destroy me !

def launchDisplay(dataMethod):
    raise NotImplementedError()

if selectedDisplaySystem == 0:
    launchConsole(dataMethod)
elif selectedDisplaySystem == 1:
    launchDisplay(dataMethod)

print("End of session")