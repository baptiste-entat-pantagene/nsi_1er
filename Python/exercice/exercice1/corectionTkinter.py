import tkinter as tk

root = tk.Tk()


label = tk.Label(root, text="J'adore Python !")
bouton = tk.Button(root, text="Quitter", fg="red",
                   command=root.destroy)
label.pack()
bouton.pack()
