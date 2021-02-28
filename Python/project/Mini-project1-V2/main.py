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
    #isspace() #rajoute moi 
    while True:
        print(msg)
        buff = input()

        if returnType == "int": #int
            if buff == "":
                continue
            try:
                int(buff)
            except:
                continue
            return int(buff)
        elif returnType == "str": #str
            if buff == "":
                continue
            return buff
        elif returnType == "bool": #bool
            if buff == "":
                continue
            elif buff == "yes" or buff == "y" or buff == "Y":
                return True
            elif buff == "no" or buff == "n" or buff == "N":
                return False
        else:
            raise NotImplementedError()

def baybay():
    print(" ▄▄▄▄    ▄▄▄      ▓██   ██▓\n▓█████▄ ▒████▄     ▒██  ██▒\n▒██▒ ▄██▒██  ▀█▄    ▒██ ██░\n▒██░█▀  ░██▄▄▄▄██   ░ ▐██▓░\n░▓█  ▀█▓ ▓█   ▓██▒  ░ ██▒▓░\n░▒▓███▀▒ ▒▒   ▓▒█░   ██▒▒▒")
    exit()


selectedDisplaySystem = 1
dataMethod = 0

""" #testing
#select display system
while True:
    print("--> Start <--")

    answer = inputSecured(msg="Choose the display system\n  Console -> 0\n  TKinter -> 1 (TKinter is only a test)", returnType="int")
    if answer == 0:
        selectedDisplaySystem = 0
        break
    elif answer == 1:
        selectedDisplaySystem = 1
        break
    else:
        print("Please retry")
        continue
"""
cls()
#select request mode
while True:
    print("Use the online mode to get the full potential of the App")
    answer = inputSecured(msg="Select the request data system\n  0 -> Online (need some library)\n  1 -> Off-line (need a large csv file -> not on github)\n -1 -> Exit", returnType="int")
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
    elif answer == -1:
        baybay()
    else:
        print("Please retry")
        continue
cls()


def launchConsole(dataMethod):
    gateway = Gateway.Gateway(requestMethod=dataMethod)
    cls()
    while True:
        event = inputSecured("select action\n    0 -> request ID\n    1 -> request name (generique)\n   -1 -> exit", "int")
        #event=0 #debug var
        global dump
        if event == 0:
            cls()
            id = inputSecured("type the id of product", "str")
            dump = gateway.requestID(id) #id
            dump = gateway.cleanDump(dump=dump)
            #3017620425035 #nutella
            #000000001576 #quik test
            #0000000001199 #quik test
        elif event == 1:
            cls()
            name = inputSecured("type the name", "str")
            #name = "nutella" #debug var
            dump = gateway.requestName(productName=name)
            dump = gateway.cleanDump(dump=dump)

        elif event == -1:
            baybay()
        else:
            continue

        #select one product in dump
        while True:
            print("We found a match for : ")
            lenListProductDump = 3
            for i in range(0, lenListProductDump):
                productN = gateway.getProductInDump(dump=dump, number=i)
                print("     ", i, "->" + str(gateway.getProductFacts(productN, option=("name"))))
            productN = inputSecured("Select your product.\n     -> type is number for select product", "int")
            if int(productN) < 0 or int(productN) >= lenListProductDump:
                continue
            break
        selectedProduct = gateway.getProductInDump(dump, number=productN)
        cls()
        while True:
            optionInside = ("all", "name", "ingredients", "code", "ecoscore_score", "ecoscore_grade","nutriscore_grade", "stores", "packaging", "quantity", "brands", "labels")
            buffMsg = ""
            for i in range(len(optionInside)):
                buffMsg += ("   \n  " + str(i) + " -> " + str(optionInside[i]))
            buffMsg += "\n  -1 -> full dump"
            select = inputSecured(buffMsg, returnType="int")
            if int(select) < 0 or int(select) >= len(optionInside):
                if int(select) != -1:
                    print("Value error, retry")
                    continue
            for i in range(len(optionInside)):
                if select == i and select != 0:
                    print("     ", optionInside[i] ," --> ", gateway.getProductFacts(selectedProduct, option=(optionInside[i]))[optionInside[i]])
                if select == 0:
                    print("     ", optionInside[i] ," --> ", gateway.getProductFacts(selectedProduct, option=(optionInside[i])))
            if select == -1:
                buff = dump
                print("\nfull dump-->")
                print(buff, flush=True)
                print("\n<--\n")




def launchDisplay(dataMethod): #just testing
    gateway = Gateway.Gateway(requestMethod=dataMethod)
    cls()
    import window
    app = window.Application()
    app.mainloop()


if selectedDisplaySystem == 0:
    launchConsole(dataMethod)
elif selectedDisplaySystem == 1: #just testing
    #raise NotImplementedError("reserved for dev")
    launchDisplay(dataMethod)

print("End of session")