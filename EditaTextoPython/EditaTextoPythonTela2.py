# -*- coding: UTF-8 -*-
from tkinter import *
from re import *

class EditaTextoPythonTela2:
    def __init__(self, master = None):
        self.fonteTitulo = ("Arial", "15")
        self.fonteCampo = ("Arial", "10")

        self.areaTitulo = Frame(master)
        self.areaTitulo["padx"]=10
        self.areaTitulo["pady"]=10
        self.areaTitulo.pack(side=TOP)

        self.titulo = Label(self.areaTitulo)
        self.titulo["padx"]=10
        self.titulo["pady"]=10
        self.titulo["font"]=self.fonteTitulo
        self.titulo["text"]="Edita Texto Python"
        self.titulo.pack(side=TOP)

        self.areaCampoPalavra = Frame(master)
        self.areaCampoPalavra["padx"]=10
        self.areaCampoPalavra["pady"]=10
        self.areaCampoPalavra.pack(side=TOP)

        self.campoPalavra = Entry(self.areaCampoPalavra)
        self.campoPalavra["width"]=50
        self.campoPalavra["font"]=self.fonteCampo
        self.campoPalavra.pack(side=TOP)

        self.campoResultado = Entry(self.areaCampoPalavra)
        self.campoResultado["width"]=50
        self.campoResultado["font"]=self.fonteCampo
        self.campoResultado.pack(side=TOP)

        self.areaBotoes = Frame(master)
        self.areaBotoes["padx"]=10
        self.areaBotoes["pady"]=10
        self.areaBotoes.pack(side=TOP)

        self.botaoReiniciar = Button(self.areaBotoes)
        self.botaoReiniciar["padx"]=10
        self.botaoReiniciar["pady"]=10
        self.botaoReiniciar["font"]=self.fonteCampo
        self.botaoReiniciar["text"]="Reiniciar"
        self.botaoReiniciar["command"]=self.editaTextoReinicia
        self.botaoReiniciar.pack(side=RIGHT)

        self.botaoResultado = Button(self.areaBotoes)
        self.botaoResultado["padx"]=10
        self.botaoResultado["pady"]=10
        self.botaoResultado["font"]=self.fonteCampo
        self.botaoResultado["text"]="Resultado"
        self.botaoResultado["command"]=self.editaTextoResultado
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
EditaTextoPythonTela2(root)
root.title("Edita Texto Python")
root.mainloop()
