from tkinter import *

# Funções...

def Cumprimente():
    hello.set("Olá, mundo!")

# Interface...

gui = Tk()
gui.title("Olá Mundo")
gui.geometry("400x400")

btn = Button(gui, text="Cumprimente", command=Cumprimente)
btn.pack()

hello = StringVar()
lbl = Label(gui, textvariable=hello)
lbl.pack()

gui.mainloop()