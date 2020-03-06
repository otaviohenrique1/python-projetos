# -*- coding: UTF-8 -*-
from tkinter import *
from re import *

class ExpressaoRegularPythonTela:
    def __init__(self, master=None):
        self.fonteTitulo = ("Arial", "20")
        self.fonteCampo = ("Arial", "15")

        self.areaTitulo = Frame(master)
        self.areaTitulo["padx"] = 10
        self.areaTitulo["pady"] = 10
        self.areaTitulo.pack(side=TOP)

        self.labelTitulo = Label(self.areaTitulo)
        self.labelTitulo["padx"] = 10
        self.labelTitulo["pady"] = 10
        self.labelTitulo["font"] = self.fonteTitulo
        self.labelTitulo["text"] = "Expressao Regular Python"
        self.labelTitulo.pack(side=TOP)

        self.areaCampoPalavra = Frame(master)
        self.areaCampoPalavra["padx"] = 10
        self.areaCampoPalavra["pady"] = 10
        self.areaCampoPalavra.pack(side=TOP)

        self.labelFrase = Label(self.areaCampoPalavra)
        self.labelFrase["padx"] = 10
        self.labelFrase["pady"] = 10
        self.labelFrase["font"] = self.fonteCampo
        self.labelFrase["text"] = "Frase"
        self.labelFrase.pack(side=TOP)

        self.campoPalavra = Entry(self.areaCampoPalavra)
        self.campoPalavra["width"] = 50
        self.campoPalavra["font"] = self.fonteCampo
        self.campoPalavra.pack(side=TOP)

        self.areaExpressaoRegular = Frame(master)
        self.areaExpressaoRegular["padx"] = 10
        self.areaExpressaoRegular["pady"] = 10
        self.areaExpressaoRegular.pack(side=TOP)

        self.labelExpressaoRegular = Label(self.areaExpressaoRegular)
        self.labelExpressaoRegular["padx"] = 10
        self.labelExpressaoRegular["pady"] = 10
        self.labelExpressaoRegular["font"] = self.fonteCampo
        self.labelExpressaoRegular["text"] = "Expressao Regular"
        self.labelExpressaoRegular.pack(side=TOP)

        self.campoExpressaoRegular = Entry(self.areaExpressaoRegular)
        self.campoExpressaoRegular["width"] = 50
        self.campoExpressaoRegular["font"] = self.fonteCampo
        self.campoExpressaoRegular.pack(side=TOP)

        self.areaResultado = Frame(master)
        self.areaResultado["padx"] = 10
        self.areaResultado["pady"] = 10
        self.areaResultado.pack(side=TOP)

        self.labelResultado = Label(self.areaResultado)
        self.labelResultado["padx"] = 10
        self.labelResultado["pady"] = 10
        self.labelResultado["font"] = self.fonteCampo
        self.labelResultado["text"] = "Resultado:"
        self.labelResultado.pack(side=TOP)

        self.labelCampoResultado = Label(self.areaResultado)
        self.labelCampoResultado["padx"] = 10
        self.labelCampoResultado["pady"] = 10
        self.labelCampoResultado["font"] = self.fonteCampo
        self.labelCampoResultado["bd"]=2
        self.labelCampoResultado["relief"] = "groove"
        self.labelCampoResultado["width"] = 30
        self.labelCampoResultado["text"] = "--------------------"
        self.labelCampoResultado.pack(side=TOP)

        self.areaBotoes = Frame(master)
        self.areaBotoes["padx"] = 10
        self.areaBotoes["pady"] = 10
        self.areaBotoes.pack(side=TOP)

        self.botaoReiniciar = Button(self.areaBotoes)
        self.botaoReiniciar["padx"] = 10
        self.botaoReiniciar["pady"] = 10
        self.botaoReiniciar["font"] = self.fonteCampo
        self.botaoReiniciar["text"] = "Reiniciar"
        self.botaoReiniciar["command"] = self.editaTextoReinicia
        self.botaoReiniciar.pack(side=RIGHT)

        self.botaoAnalisa = Button(self.areaBotoes)
        self.botaoAnalisa["padx"] = 10
        self.botaoAnalisa["pady"] = 10
        self.botaoAnalisa["font"] = self.fonteCampo
        self.botaoAnalisa["text"] = "Analisa"
        self.botaoAnalisa["command"] = self.expressaoRegularResultado
        self.botaoAnalisa.pack(side=RIGHT)

    def expressaoRegularResultado(self):
        self.texto = self.campoPalavra.get()
        self.expressaoRegularTexto = self.campoExpressaoRegular.get()
        self.textoResultado = findall(self.expressaoRegularTexto, self.texto)
        if(self.texto == ""):
            self.labelCampoResultado["text"] = "Campo vazio"
        else:
            if(self.textoResultado):
                self.labelCampoResultado["text"] = "Encontrou"
            else:
                self.labelCampoResultado["text"] = "Não encontrou"
            # Exemplo -> [a-zA-Z0-9]

    def editaTextoReinicia(self):
        self.campoPalavra.delete(0, "end")
        self.campoExpressaoRegular.delete(0, "end")
        self.labelCampoResultado["text"] = "--------------------"

root = Tk()
ExpressaoRegularPythonTela(root)
root.title("Expressao Regular Python")
root.mainloop()
