from systemeMonetaire import *
import tkinter as tk
import gui

print("--> start <--")

gestM = GestionMonetaire()
gestM.set_compte_exemple()


#print(gestM.renduMonnaies(49))



app = gui.Application()
app.mainloop()