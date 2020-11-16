# coding: utf-8
 
from tkinter import * 




mainWindows = Tk()

def LolMachine():
    print("lol")

boutton = Button(mainWindows, text="mon boutton magique", commande=LolMachine)
boutton.pack
mainWindows.mainloop()
