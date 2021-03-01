"""
# User input management module
## credit
- Entat Baptiste
"""
import os


def entry(returnType:str, failureMsg:str="", debugValue=None):
    """
    - returnType -> "int", "str", "bool"(yes/no)
    """
    if returnType != "int" and returnType != "str" and returnType != "bool":
        raise NotImplementedError("returnType specified are not implemented")
    while True:
        if debugValue != None:
            buff = debugValue
        else:
            buff = input()
        if returnType == "int":  #int
            if buff == "":
                if debugValue != None:
                    return "debugError"
                print(failureMsg)
                continue
            try:
                int(buff)
            except:
                if debugValue != None:
                    return "debugError"
                print(failureMsg)
                continue
            return int(buff)
        elif returnType == "str":  #str
            if buff == "" or buff.isspace() == True:
                if debugValue != None:
                    return "debugError"
                print(failureMsg)
                continue
            return buff
        elif returnType == "bool":  #bool
            if buff == "":
                if debugValue != None:
                    return "debugError"
                print(failureMsg)
                continue
            elif buff == "yes" or buff == "y" or buff == "Y" or buff == "oui" or buff == "Oui":
                return True
            elif buff == "no" or buff == "n" or buff == "N" or buff == "non" or buff == "Non":
                return False
            else:
                if debugValue != None:
                    return "debugError"
                else:
                    continue
        else:
            if debugValue != None:
                    return "debugError"
            print(failureMsg)
            continue




def cls():
    """
    clear console
    - Window and Linux supported
    """
    os.system('cls' if os.name == 'nt' else 'clear')

