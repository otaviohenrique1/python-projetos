# -*- coding: utf-8 -*-
from math import *
from tkinter import *

class TelaCalculo:
    def __init__(self, master = None):
        self.fonteTitulo = ("Arial", "15")
        self.fonteCampo = ("Arial", "10")
        self.areaTitulo = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.areaTituloFrame = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.tituloLabel = Label(self.areaTituloFrame, padx=10, pady=10, font=self.fonteTitulo, text="Tela calculo").pack(side=TOP)
        self.areaTianguloFrame = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.canvas = Canvas(self.areaTituloFrame, height=300, width=500)
        # self.canvas.create_polygon([250,100,400,200,250,200,250,100], outline='gray', fill='gray', width=2)
        # self.canvas.create_polygon([100,40,160,80,100,80,100,40], outline='gray', fill='gray', width=2)
        self.canvas.create_polygon([200,80,320,160,200,160,200,80], outline='gray', fill='gray', width=2)
        self.canvas.pack(side=TOP)

        self.areaCampoHipotenusa = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.tituloCampoHipotenusa = Label(self.areaCampoHipotenusa, padx=10, pady=10, font=self.fonteTitulo, text="Hipotenusa: ").pack(side=TOP)
        self.campoHipotenusa = Entry(self.areaCampoHipotenusa, width=50, font=self.fonteCampo).pack(side=TOP)

        self.areaCampoCateto1 = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.tituloCampoCateto1 = Label(self.areaCampoCateto1, padx=10, pady=10, font=self.fonteTitulo, text="Cateto 1: ").pack(side=TOP)
        self.campoCateto1 = Entry(self.areaCampoCateto1, width=50, font=self.fonteCampo).pack(side=TOP)

        self.areaCampoCateto2 = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.tituloCampoCateto2 = Label(self.areaCampoCateto2, padx=10, pady=10, font=self.fonteTitulo, text="Cateto 2: ").pack(side=TOP)
        self.campoCateto2 = Entry(self.areaCampoCateto2, width=50, font=self.fonteCampo).pack(side=TOP)

        self.areaBotoesFrame = Frame(master, padx=10, pady=10).pack(side=TOP)
        self.botaoResultado = Button(
            self.areaBotoesFrame, padx=10, pady=10, font=self.fonteCampo, text="Resultado")
        self.botaoResultado.pack(side=TOP)

root = Tk()
TelaCalculo(root)
root.title("Tela calculo")
root.mainloop()
