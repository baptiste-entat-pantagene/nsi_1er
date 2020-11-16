from tkinter import *

mainWin = Tk()

def work():
    print("nice work")

text1 = Label(mainWin, text="je suis en vie")
text1.pack()
but1 = Button(mainWin, text="clique !", command=work)
but1.pack()

mainWin.mainloop()