import tkinter as tk

def reponse(xxx = ""):
    ageInt = int(buff.get())
    reponseStr = "Vous êtes donc née en " + str(2020 - ageInt)
    reponseLabel = tk.Label(root, text=reponseStr)
    reponseLabel.grid(column=0, row=2)

root = tk.Tk()

question = tk.Label(root, text="Veillez entre votre âge")

buff = tk.IntVar(root)
entryAge = tk.Entry(root, textvariable=buff)
entryAge.bind('<Key-Return>', reponse)

question.grid(column=0, row=0)
entryAge.grid(column=0, row=1)

root.mainloop()