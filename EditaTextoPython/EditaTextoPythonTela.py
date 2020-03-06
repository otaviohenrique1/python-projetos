# -*- coding: UTF-8 -*-
from tkinter import *
from re import *

class EditaTextoPythonTela:
    def __init__(self, master = None):
        self.fonteTitulo = ("Arial", "15")
        self.fonteCampo = ("Arial", "10")

        self.areaTitulo = Frame(master, padx=10, pady=10)
        self.areaTitulo.pack(side=TOP)

        self.titulo = Label(self.areaTitulo, padx=10, pady=10, font=self.fonteTitulo, text="Edita Texto Python")
        self.titulo.pack(side=TOP)

        self.areaCampoPalavra = Frame(master, padx=10, pady=10)
        self.areaCampoPalavra.pack(side=TOP)

        self.campoPalavra = Entry(self.areaCampoPalavra, width=50, font=self.fonteCampo)
        self.campoPalavra.pack(side=TOP)

        self.campoResultado = Entry(self.areaCampoPalavra, width=50, font=self.fonteCampo)
        self.campoResultado.pack(side=TOP)

        self.areaBotoes = Frame(master, padx=10, pady=10)
        self.areaBotoes.pack(side=TOP)

        self.botaoReiniciar = Button(
            self.areaBotoes, padx=10, pady=10, font=self.fonteCampo, text="Reiniciar", command=self.editaTextoReinicia)
        self.botaoReiniciar.pack(side=RIGHT)

        self.botaoResultado = Button(
            self.areaBotoes, padx=10, pady=10, font=self.fonteCampo, text="Resultado", command=self.editaTextoResultado)
        self.botaoResultado.pack(side=RIGHT)

    def editaTextoResultado(self):
        self.texto = self.campoPalavra.get()
        self.textoSemEspaco = sub("\s", "_", self.texto)
        self.textoSemTraco = sub("-", "_", self.textoSemEspaco)
        self.textoSemPonto = sub("[.]", "", self.textoSemTraco)
        self.campoResultado.delete(0, "end")
        self.campoResultado.insert(0, self.textoSemPonto)

    def editaTextoReinicia(self):
        self.campoPalavra.delete(0, "end")
        self.campoResultado.delete(0, "end")

root = Tk()
EditaTextoPythonTela(root)
root.title("Edita Texto Python")
root.mainloop()
