import os
import Gateway


def cls():
    """
    clear console
    """
    os.system('cls' if os.name=='nt' else 'clear')


def inputSecured(msg:str, returnType:str):
    """
    returnType: "int", "str"
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
    answer = inputSecured(msg="Select the request data system\n  Online -> 00 (need some library)\n  Off-line -> 1 (need a large csv file -> not on github)", returnType="int")
    if answer == 0:
        #check si les dépendence existe
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
        #print("select action\n    0 -> requestID\n    1 -> ?")
        event = inputSecured("select action\n    0 -> request ID\n    1 -> request name (generique)", "int")

        if event == 0:
            cls()
            id = inputSecured("type the id of product", "str")
            gateway.requestID(id)
            #3017620425035 #nutella
            #000000001576 #quik test
        elif event == 1:
            cls()
            name = inputSecured("type the name", "str")
            gateway.requestName(name)
        else:
            continue

def launchDisplay(dataMethod):
    raise NotImplementedError()

if selectedDisplaySystem == 0:
    launchConsole(dataMethod)
elif selectedDisplaySystem == 1:
    launchDisplay(dataMethod)

print("End of session")