from tkinter import *
from functools import partial

mainWin = Tk()

modLigne:bool = True #True == FirstLigne, False == SecondLigne
calcMod:int = -1 #-1 == not defined, 0 == add, 1 == soust
firstLigne:str = ""
secondLigne:str = ""


def SayHello() -> None:
    """
    default command
    """

    print("not implement")

def update_labelResult(txt:str):
    """
    Modifie le texte de l'afffichage du resultat.
    """
    global affichageResult
    affichageResult.config(text=txt)

def addToLigne(num:str, label = 0) -> None:
    global firstLigne
    global secondLigne
    if modLigne == True:
        firstLigne = firstLigne + num
        update_labelResult(firstLigne)
    else:
        secondLigne = secondLigne + num
        update_labelResult(secondLigne)

def changeMod(modeDeCalcul:int = -1, label = 0) -> None:
    global modLigne
    global calcMod
    if modeDeCalcul == 0:
        calcMod = 0
    elif modeDeCalcul == 1:
        calcMod = 1
    elif modeDeCalcul == 2:
        calcMod = 2
    elif modeDeCalcul == 3:
        calcMod = 3

    if modLigne == True:
        modLigne = False
        update_labelResult(secondLigne)
    else:
        modLigne = True
        update_labelResult(firstLigne)


def result(label = 0) -> None:
    global calcMod
    global firstLigne
    global secondLigne
    
    if calcMod == 0:
        update_labelResult(str(int(firstLigne) + int(secondLigne)))
        print("result -->", str(int(firstLigne) + int(secondLigne)))
    elif calcMod == 1:
        update_labelResult(str(int(firstLigne) - int(secondLigne)))
    elif calcMod == 2:
        update_labelResult(str(int(firstLigne) / int(secondLigne)))
    elif calcMod == 3:
        update_labelResult(str(int(firstLigne) * int(secondLigne)))
    else:
        print("not defined -1 result")
    firstLigne = ""
    secondLigne = ""


# frame def
FramNum = Frame(mainWin, borderwidth=2, relief=GROOVE)
FramNum.grid(column=0, row=0)
FramAction = Frame(mainWin, borderwidth=2, relief=GROOVE)
FramAction.grid(column=0, row=1)
FramAffi = Frame(mainWin, borderwidth=2, relief=GROOVE)
FramAffi.grid(column=1, row=0)

#FramAffi
affichageResult = Label(FramAffi, text="")
affichageResult.grid(column=0, row=0)


# Ajout des boutons de la calc

x = 0
for i in range(9, -1, -1):
    button = Button(FramNum, text=str(i), command=partial(addToLigne, str(i)))
    button.grid(column = i, row = i)
    mainWin.bind(str(i), partial(addToLigne, str(i)))
    

"""
but_1 = Button(FramNum, text="1", command=partial(addToLigne, '1'))
but_1.grid(column=0, row=2)
mainWin.bind('1', partial(addToLigne, '1'))
but_4 = Button(FramNum, text="4", command=partial(addToLigne, '4'))
but_4.grid(column=0, row=1)
mainWin.bind('4', partial(addToLigne, '4'))
but_7 = Button(FramNum, text="7", command=partial(addToLigne, '7'))
but_7.grid(column=0, row=0)
mainWin.bind('7', partial(addToLigne, '7'))

but_2 = Button(FramNum, text="2", command=partial(addToLigne, '2'))
but_2.grid(column=1, row=2)
mainWin.bind('2', partial(addToLigne, '2'))
but_5 = Button(FramNum, text="5", command=partial(addToLigne, '5'))
but_5.grid(column=1, row=1)
mainWin.bind('5', partial(addToLigne, '5'))
but_8 = Button(FramNum, text="8", command=partial(addToLigne, '8'))
but_8.grid(column=1, row=0)
mainWin.bind('8', partial(addToLigne, '8'))

but_3 = Button(FramNum, text="3", command=partial(addToLigne, '3'))
but_3.grid(column=2, row=2)
mainWin.bind('3', partial(addToLigne, '3'))
but_6 = Button(FramNum, text="6", command=partial(addToLigne, '6'))
but_6.grid(column=2, row=1)
mainWin.bind('6', partial(addToLigne, '6'))
but_9 = Button(FramNum, text="9", command=partial(addToLigne, '9'))
but_9.grid(column=2, row=0)
mainWin.bind('9', partial(addToLigne, '9'))

but_0 = Button(FramNum, text="0", command=partial(addToLigne, '0'))
but_0.grid(column=1, row=3)
mainWin.bind('0', partial(addToLigne, '0'))
"""


#framAction
but_Plus = Button(FramAction, text="+", command=partial(changeMod, 0))
but_Plus.grid(column=0, row=0)
but_Moins = Button(FramAction, text="-", command=partial(changeMod, 1))
but_Moins.grid(column=1, row=0)
but_Div = Button(FramAction, text="/", command=partial(changeMod, 2))
but_Div.grid(column=2, row=0)
but_Multi = Button(FramAction, text="*", command=partial(changeMod, 3))
but_Multi.grid(column=3, row=0)
but_Egal = Button(FramAction, text="=", command=partial(result))
but_Egal.grid(column=4, row=0)
#bind action
mainWin.bind('+', partial(changeMod, 0))
mainWin.bind('-', partial(changeMod, 1))
mainWin.bind('/', partial(changeMod, 2))
mainWin.bind('*', partial(changeMod, 3))
mainWin.bind('<Key-Return>', partial(result))


#entry = Entry(FramAction)
#entry.grid(row=0, column=0)
#entry.bind('<Key-Return>', partial(result))


#end


mainWin.mainloop()