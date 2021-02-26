import Gateway
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
# now, to clear the screen
#cls()

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



selectedDisplaySystem = -1
dataMethod =-1

while True:
    print("--> Start <--")

    answer = inputSecured(msg="Choose the display system\n  Console -> 1\n  TKinter -> 2 (TKinter is only a test)", returnType="int")
    if answer == 1:
        selectedDisplaySystem = 1
        break
    elif answer == 2:
        selectedDisplaySystem = 2
        raise NotImplementedError()
        break
    else:
        print("Please retry")
        continue

cls()
while True:
    answer = inputSecured(msg="Select the request data system\n  Online -> 1 (need some library)\n  Off-line -> 2 (need a large csv file -> not on github)", returnType="int")
    if answer == 1:
        #add try block
        print("Successful selction of the online mode")
        dataMethod = 1
        break
    elif answer == 2:
        #add try block
        print("Successful selction of the off-line mode")
        dataMethod = 2
        break
    else:
        print("Please retry")
        continue
cls()

def launchConsole(dataMethod):

    webGateway = Gateway.Gateway(requestMethod=0)
    webGateway.requestID(3017620425035)

def launchDisplay(dataMethod):
    pass

if selectedDisplaySystem == 1:
    launchConsole(dataMethod)
elif selectedDisplaySystem == 2:
    launchDisplay(dataMethod)

print("End of session")