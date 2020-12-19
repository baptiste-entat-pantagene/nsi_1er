def inputSec(msg:str = ""):
    if msg != "":
        print(msg)
    while True:
        buff:str = ""
        try:
            buff = input()
            break
        except:
            continue
    return buff

