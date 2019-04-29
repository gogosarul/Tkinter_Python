from tkinter import *

root = Tk()
root.title("Hola")
root.resizable(1,1)
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
#frame.pack()
#frame.pack(side="right") #lado derecho y left a la izquierda
#frame.pack(side="bottom") #abajo en medio y superior en medio top
#frame.pack(side="bottom", anchor="w") #abajo y anclado a la izquerda (oeste)
frame.pack(fill="both", expand=1) # y rellenar abajo y expandir, a los lados solo con x
frame.config(cursor="spider", bg="lightblue", bd=25, relief="sunken")

root.config(cursor="watch", bg="blue", bd=15, relief="ridge")

root.mainloop()