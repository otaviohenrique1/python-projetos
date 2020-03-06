# -*- coding: UTF-8 -*-
from tkinter import *
from re import *

class ConverteTemperaturaTela:
    def __init__(self, master=None):
        self.fonteTitulo = ("Arial", "20")
        self.fonte = ("Arial", "15")
        self.listaTemperatura = ["Selecione", "Kelvin", "Celsius", "Fahrenheit"]

        self.areaTitulo = self.criaFrame(master, 10, 10, TOP)
        self.tituloTela = self.criaLabel(self.areaTitulo, 10, 10, self.fonteTitulo, "Conversao de temperaturas", TOP)
        self.textoMensagem = self.criaLabel(self.areaTitulo, 10, 10, self.fonte, "", TOP)

        self.areaCampoTemperatura1 = self.criaFrame(master, 10, 10, TOP)
        self.tituloCampoTemperatura1 = self.criaLabel(self.areaCampoTemperatura1, 10, 10, self.fonte, "Converte de ", LEFT)
        self.item1 = StringVar(self.areaCampoTemperatura1)
        self.item1.set(self.listaTemperatura[0])
        self.selecionaTemperatura1 = OptionMenu(self.areaCampoTemperatura1, self.item1, *self.listaTemperatura)
        self.selecionaTemperatura1["font"] = self.fonte
        self.selecionaTemperatura1.pack(side=LEFT)
        self.campoTemperatura1 = self.criaEntry(self.areaCampoTemperatura1, self.fonte, 10, LEFT)

        self.areaCampoTemperatura2 = self.criaFrame(master, 10, 10, TOP)
        self.tituloCampoTemperatura2 = self.criaLabel(self.areaCampoTemperatura2, 10, 10, self.fonte, "para ", LEFT)
        self.item2 = StringVar(self.areaCampoTemperatura2)
        self.item2.set(self.listaTemperatura[0])
        self.selecionaTemperatura2 = OptionMenu(self.areaCampoTemperatura2, self.item2, *self.listaTemperatura)
        self.selecionaTemperatura2["font"] = self.fonte
        self.selecionaTemperatura2.pack(side=LEFT)
        self.campoTemperatura2 = self.criaLabel(self.areaCampoTemperatura2, 10, 10, self.fonte, "0", LEFT)

        self.areaBotoes = self.criaFrame(master, 10, 10, TOP)
        self.botaoResultado = self.criaButton(self.areaBotoes, "Resultado", self.fonte, self.resultado, LEFT)
        self.botaoApagarCampos = self.criaButton(self.areaBotoes, "Apagar campos", self.fonte, self.apagarCampos, LEFT)

    def resultado(self):
        self.item1Campo = self.item1.get()
        self.item2Campo = self.item2.get()
        self.valorTemperatura = self.campoTemperatura1.get()
        self.validaNumeroTexto = findall("[a-zA-Z]", self.valorTemperatura)
        self.mensagemCampoVazio = "Vampo vazio"
        self.mensagemSelecioneTemperatura = "Selecione temperatura"
        self.mensagemSomenteNumeros = "Somente numeros no campo"
        self.textoCampoVazio = ""
        self.textoSelecione = "Selecione"
        self.textoCelsius = "Celsius"
        self.textoFahrenheit = "Fahrenheit"
        self.textoKelvin = "Kelvin"

        if(self.valorTemperatura == self.textoCampoVazio):
            self.textoMensagem["text"] = self.mensagemCampoVazio
        elif(self.item1Campo == self.textoSelecione and self.item2Campo == self.textoSelecione):
            self.textoMensagem["text"] = self.mensagemSelecioneTemperatura
        elif (self.item1Campo == self.textoSelecione or self.item2Campo == self.textoSelecione):
            self.textoMensagem["text"] = self.mensagemSelecioneTemperatura
        elif (self.validaNumeroTexto):
            self.textoMensagem["text"] = self.mensagemSomenteNumeros
            self.campoTemperatura1.delete(0, "end")
            self.campoTemperatura2["text"] = "0"
        else:
            self.textoMensagem["text"] = self.textoCampoVazio
            if(self.item1Campo == self.textoCelsius and self.item2Campo == self.textoFahrenheit):
                self.campoTemperatura2["text"] = self.converteCelsiusParaFahrenheit(self.valorTemperatura)
            elif (self.item1Campo == self.textoCelsius and self.item2Campo == self.textoKelvin):
                self.campoTemperatura2["text"] = self.converteCelsiusParaKelvin(self.valorTemperatura)
            elif (self.item1Campo == self.textoFahrenheit and self.item2Campo == self.textoCelsius):
                self.campoTemperatura2["text"] = self.converteFahrenheitParaCelsius(self.valorTemperatura)
            elif (self.item1Campo == self.textoFahrenheit and self.item2Campo == self.textoKelvin):
                self.campoTemperatura2["text"] = self.converteFahrenheitParaKelvin(self.valorTemperatura)
            elif (self.item1Campo == self.textoKelvin and self.item2Campo == self.textoCelsius):
                self.campoTemperatura2["text"] = self.converteKelvinParaCelsius(self.valorTemperatura)
            elif (self.item1Campo == self.textoKelvin and self.item2Campo == self.textoFahrenheit):
                self.campoTemperatura2["text"] = self.converteKelvinParaFahrenheit(self.valorTemperatura)
            elif (self.item1Campo == self.textoKelvin and self.item2Campo == self.textoKelvin):
                self.campoTemperatura2["text"] = self.valorTemperatura
            elif (self.item1Campo == self.textoFahrenheit and self.item2Campo == self.textoFahrenheit):
                self.campoTemperatura2["text"] = self.valorTemperatura
            elif (self.item1Campo == self.textoCelsius and self.item2Campo == self.textoCelsius):
                self.campoTemperatura2["text"] = self.valorTemperatura

    def apagarCampos(self):
        self.campoTemperatura1.delete(0, "end")
        self.campoTemperatura2["text"] = "0"
        self.textoCampoVazio = ""
        self.textoMensagem["text"] = self.textoCampoVazio
        self.item1.set(self.listaTemperatura[0])
        self.item2.set(self.listaTemperatura[0])

    def criaFrame(self, local, padx, pady, valorSide):
        self.frame = Frame(local)
        self.frame["padx"] = padx
        self.frame["pady"] = pady
        self.frame.pack(side=valorSide)
        return self.frame

    def criaButton(self, local, texto, fonte, comando, valorSide):
        self.button = Button(local)
        self.button["text"] = texto
        self.button["font"] = fonte
        self.button["command"] = comando
        self.button.pack(side=valorSide)
        return self.button

    def criaLabel(self, local, padx, pady, fonte, texto, valorSide):
        self.label = Label(local)
        self.label["padx"] = padx
        self.label["pady"] = pady
        self.label["font"] = fonte
        self.label["text"] = texto
        self.label.pack(side=valorSide)
        return self.label

    def criaEntry(self, local, fonte, largura, valorSide):
        self.entry = Entry(local)
        self.entry["font"] = fonte
        self.entry["width"] = largura
        self.entry.pack(side=valorSide)
        return self.entry

    def converteCelsiusParaFahrenheit(self, temperaturaCelsius):
        self.temperaturaFahrenheit = float(temperaturaCelsius) * 1.8 + 32
        return self.temperaturaFahrenheit

    def converteCelsiusParaKelvin(self, temperaturaCelsius):
        self.temperaturaKelvin = float(temperaturaCelsius) + 273.15
        return self.temperaturaKelvin

    def converteFahrenheitParaCelsius(self, temperaturaFahrenheit):
        self.temperaturaCelsius = (float(temperaturaFahrenheit) - 32)/1.8
        return self.temperaturaCelsius

    def converteFahrenheitParaKelvin(self, temperaturaFahrenheit):
        self.temperaturaKelvin = (float(temperaturaFahrenheit) + 459.67)/1.8
        return self.temperaturaKelvin

    def converteKelvinParaCelsius(self, temperaturaKelvin):
        self.temperaturaCelsius = float(temperaturaKelvin) - 273.15
        return self.temperaturaCelsius

    def converteKelvinParaFahrenheit(self, temperaturaKelvin):
        self.temperaturaFahrenheit = float(temperaturaKelvin) * 1.8 - 459.67
        return self.temperaturaFahrenheit

root = Tk()
ConverteTemperaturaTela(root)
root.title("Conversao de temperatura")
root.mainloop()
