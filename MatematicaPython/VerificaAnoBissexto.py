# -*- coding: UTF-8 -*-
from tkinter import *
from re import *

class VerificaAnoBissextoTela:
    def __init__(self, master=None):
        self.fonteTitulo = ("Arial", "20")
        self.fonte = ("Arial", "15")

        self.areaTitulo = Frame(master, padx=10, pady=10)
        self.areaTitulo.pack(side=TOP)
        self.titulo = Label(self.areaTitulo, padx=10, pady=10, font=self.fonteTitulo, text="Verifica ano bissexto")
        self.titulo.pack(side=TOP)

        self.areaCampoAno = Frame(master, padx=10, pady=10)
        self.areaCampoAno.pack(side=TOP)
        self.labelAno = Label(self.areaCampoAno, width=10, padx=10, pady=10, font=self.fonte, text="Ano")
        self.labelAno.pack(side=LEFT)
        self.campoAno = Entry(self.areaCampoAno, width=20, font=self.fonte)
        self.campoAno.pack(side=LEFT)

        self.areaCampoResultado = Frame(master, padx=10, pady=10)
        self.areaCampoResultado.pack(side=TOP)
        self.campoResultado = Label(self.areaCampoResultado, width=30, padx=10, pady=10, bd=2,
                                    relief="groove", font=self.fonte, text="----------")
        self.campoResultado.pack(side=TOP)

        self.areaBotoes = Frame(master, padx=10, pady=10)
        self.areaBotoes.pack(side=TOP)

        self.botaoReiniciar = Button(
            self.areaBotoes, padx=10, pady=10, font=self.fonte, text="Reiniciar", command=self.editaTextoReinicia)
        self.botaoReiniciar.pack(side=RIGHT)

        self.botaoResultado = Button(
            self.areaBotoes, padx=10, pady=10, font=self.fonte, text="Resultado", command=self.editaTextoResultado)
        self.botaoResultado.pack(side=RIGHT)

    def editaTextoResultado(self):
        self.texto = self.campoAno.get()
        self.validaNumero = findall("[a-zA-Z]", str(self.texto))
        if(self.texto == ""):
            self.campoResultado["text"] = "Campo vazio"
        elif(self.validaNumero):
            self.campoAno.delete(0, "end")
            self.campoResultado["text"] = "Somente numeros no campo"
        else:
            self.campoResultado["text"] = self.verificaAnoBissexto(self.texto)

    def editaTextoReinicia(self):
        self.campoResultado["text"] = ""
        self.campoAno.delete(0, "end")
        self.campoResultado["text"] = "----------"

    def verificaAnoBissexto(self, ano):
        self.ano = int(ano)
        if ((self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0)):
            return 'Ano é bissexto'
        return 'Ano não é bissexto'

root = Tk()
VerificaAnoBissextoTela(root)
root.title("Verifica ano bissexto")
root.mainloop()
