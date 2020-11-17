from tkinter import *

mainWin = Tk()

def SayHello():
    print("nice work")

but1 = Button(mainWin, text="clique !", command=SayHello)
but1.pack()

mainWin.mainloop()