from tkinter import *

mainWin = Tk()

def work():
    print("nice work")

but1 = Button(mainWin, text="clique !", command=work)
but1.pack()

mainWin.mainloop()