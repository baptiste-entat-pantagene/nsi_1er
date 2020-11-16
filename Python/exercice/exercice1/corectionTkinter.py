from tkinter import *

mainWin = Tk()

def work():
    label1 = Label(mainWin, text="buff")
    label1.pack()


but1 = Button(mainWin, text="clique !", command=work)
but1.pack()
but1.pack()

mainWin.mainloop()