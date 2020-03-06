# -*- coding: UTF-8 -*-
from tkinter import *
from random import *
from re import *


class LoteriaPythonTela:
    def __init__(self, master=None):
        self.fonteAreaNumerosLoteria = ("Arial", "15")
        self.fonteTituloLoteria = ("Arial", "30")
        self.tamanhoBorda = 2
        self.tipoBorda = "groove"
        self.numeroCampoTamanho = 3
        self.textoPadraoCamposLoteriaNumero = "*"
        self.campoResultadoTextoPadrao = "----------"
        self.valorEspacamentoTituloX = 20
        self.valorEspacamentoTituloY = 20
        self.valorEspacamentoCampoX = 10
        self.valorEspacamentoCampoY = 10

        self.areaTitulo = Frame(master, padx=self.valorEspacamentoTituloX, pady=self.valorEspacamentoTituloY)
        self.areaTitulo.pack(side=TOP)

        self.areaNumerosLoteria = Frame(master, padx=self.valorEspacamentoTituloX, pady=self.valorEspacamentoTituloY)
        self.areaNumerosLoteria.pack(side=TOP)

        self.areaNumerosAposta = Frame(master, padx=self.valorEspacamentoTituloX, pady=self.valorEspacamentoTituloY)
        self.areaNumerosAposta.pack(side=TOP)

        self.areaResultado = Frame(master, padx=self.valorEspacamentoTituloX, pady=self.valorEspacamentoTituloY,
                                   bd=self.tamanhoBorda, relief=self.tipoBorda)
        self.areaResultado.pack(side=TOP)

        self.areaBotao = Frame(master, padx=self.valorEspacamentoTituloX, pady=self.valorEspacamentoTituloY)
        self.areaBotao.pack(side=TOP)

        self.tituloLoteria= Label(self.areaTitulo, font=self.fonteTituloLoteria, padx=self.valorEspacamentoCampoX,
                                  pady=self.valorEspacamentoCampoY, bd=self.tamanhoBorda, relief=self.tipoBorda,
                                  text="Loteria Python")
        self.tituloLoteria.pack(side=RIGHT)

        # Campos numeros da loteria
        self.loteriaPrimeiroNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                           padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                           bd=self.tamanhoBorda, relief=self.tipoBorda,
                                           text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaPrimeiroNumero.pack(side=RIGHT)

        self.loteriaSegundoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                          padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                          bd=self.tamanhoBorda, relief=self.tipoBorda,
                                          text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaSegundoNumero.pack(side=RIGHT)

        self.loteriaTerceiroNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                           padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                           bd=self.tamanhoBorda, relief=self.tipoBorda,
                                           text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaTerceiroNumero.pack(side=RIGHT)

        self.loteriaQuartoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                         padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                         bd=self.tamanhoBorda, relief=self.tipoBorda,
                                         text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaQuartoNumero.pack(side=RIGHT)

        self.loteriaQuintoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                         padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                         bd=self.tamanhoBorda, relief=self.tipoBorda,
                                         text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaQuintoNumero.pack(side=RIGHT)

        self.loteriaSextoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria,
                                        padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                        bd=self.tamanhoBorda, relief=self.tipoBorda,
                                        text=self.textoPadraoCamposLoteriaNumero, width=self.numeroCampoTamanho)
        self.loteriaSextoNumero.pack(side=RIGHT)

        # Campos numeros da aposta
        self.apostaPrimeiroNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                          width=self.numeroCampoTamanho)
        self.apostaPrimeiroNumero.pack(side=RIGHT)

        self.apostaSegundoNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                         width=self.numeroCampoTamanho)
        self.apostaSegundoNumero.pack(side=RIGHT)

        self.apostaTerceiroNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                          width=self.numeroCampoTamanho)
        self.apostaTerceiroNumero.pack(side=RIGHT)

        self.apostaQuartoNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                        width=self.numeroCampoTamanho)
        self.apostaQuartoNumero.pack(side=RIGHT)

        self.apostaQuintoNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                        width=self.numeroCampoTamanho)
        self.apostaQuintoNumero.pack(side=RIGHT)

        self.apostaSextoNumero = Entry(self.areaNumerosAposta, font=self.fonteAreaNumerosLoteria,
                                       width=self.numeroCampoTamanho)
        self.apostaSextoNumero.pack(side=RIGHT)

        # Titulo do resultado
        self.tituloResultado = Label(self.areaResultado, font=self.fonteAreaNumerosLoteria,
                                     padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                     width=20, text="Resultado:")
        self.tituloResultado.pack(side=TOP)

        # Campo que exibe o resultado da loteria e os erros
        self.campoResultado = Label(self.areaResultado, font=self.fonteAreaNumerosLoteria,
                                    padx=self.valorEspacamentoCampoX, pady=self.valorEspacamentoCampoY,
                                    width=40, text=self.campoResultadoTextoPadrao)
        self.campoResultado.pack(side=TOP)

        # Botoes
        self.realizaAposta = Button(self.areaBotao, font=self.fonteAreaNumerosLoteria,
                                    text="Realiza aposta", command=self.realizaApostaLoteria)
        self.realizaAposta.pack(side=LEFT)

        self.realizaReinicia = Button(self.areaBotao, font=self.fonteAreaNumerosLoteria,
                                      text="Reinicia aposta", command=self.reiniciaApostaLoteria)
        self.realizaReinicia.pack(side=LEFT)

        # Numero aleatorio
        self.valorLoteriaNumero()

    def valorLoteriaNumero(self):
        self.numeroAleatorioInicio = 1
        self.numeroAleatorioFinal = 60
        self.valorLoteriaPrimeiroNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                   self.numeroAleatorioFinal)
        self.valorLoteriaSegundoNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                  self.numeroAleatorioFinal)
        self.valorLoteriaTerceiroNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                   self.numeroAleatorioFinal)
        self.valorLoteriaQuartoNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                 self.numeroAleatorioFinal)
        self.valorLoteriaQuintoNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                 self.numeroAleatorioFinal)
        self.valorLoteriaSextoNumero = self.geraNumeroAleatorio(self.numeroAleatorioInicio,
                                                                self.numeroAleatorioFinal)

    def geraNumeroAleatorio(self, x, y):
        return randint(x, y)

    def realizaApostaLoteria(self):
        self.valorApostaPrimeiroNumero = self.apostaPrimeiroNumero.get()
        self.valorApostaSegundoNumero = self.apostaSegundoNumero.get()
        self.valorApostaTerceiroNumero = self.apostaTerceiroNumero.get()
        self.valorApostaQuartoNumero = self.apostaQuartoNumero.get()
        self.valorApostaQuintoNumero = self.apostaQuintoNumero.get()
        self.valorApostaSextoNumero = self.apostaSextoNumero.get()

        self.comparaPrimeiroValor = self.valorLoteriaPrimeiroNumero == self.valorApostaPrimeiroNumero
        self.comparaSegundoValor = self.valorLoteriaSegundoNumero == self.valorApostaSegundoNumero
        self.comparaTerceiroValor = self.valorLoteriaTerceiroNumero == self.valorApostaTerceiroNumero
        self.comparaQuartoValor = self.valorLoteriaQuartoNumero == self.valorApostaQuartoNumero
        self.comparaQuintoValor = self.valorLoteriaQuintoNumero == self.valorApostaQuintoNumero
        self.comparaSextoValor = self.valorLoteriaSextoNumero == self.valorApostaSextoNumero

        self.campoVazio = ""
        self.validaPrimeiroCampo = self.valorApostaPrimeiroNumero == self.campoVazio
        self.validaSegundoCampo = self.valorApostaSegundoNumero == self.campoVazio
        self.validaTerceiroCampo = self.valorApostaTerceiroNumero == self.campoVazio
        self.validaQuartoCampo = self.valorApostaQuartoNumero == self.campoVazio
        self.validaQuintoCampo = self.valorApostaQuintoNumero == self.campoVazio
        self.validaSextoCampo = self.valorApostaSextoNumero == self.campoVazio

        self.expressaoRegularBusca = "[a-zA-Z]"
        self.validaNumeroPrimeiroCampo = findall(self.expressaoRegularBusca, self.valorApostaPrimeiroNumero)
        self.validaNumeroSegundoCampo = findall(self.expressaoRegularBusca, self.valorApostaSegundoNumero)
        self.validaNumeroTerceiroCampo = findall(self.expressaoRegularBusca, self.valorApostaTerceiroNumero)
        self.validaNumeroQuartoCampo = findall(self.expressaoRegularBusca, self.valorApostaQuartoNumero)
        self.validaNumeroQuintoCampo = findall(self.expressaoRegularBusca, self.valorApostaQuintoNumero)
        self.validaNumeroSextoCampo = findall(self.expressaoRegularBusca, self.valorApostaSextoNumero)

        self.camposVaziosMensagem = "Campos vazios"
        self.campoVazioMensagem = "Campo vazio"
        self.somenteNumerosMensagem = "Somente numeros nos campos"
        self.numeroMenorQue60Mensagem = "Somente numeros menores ou iguais a 60"
        self.numeroMaiorQueZeroMensagem = "Somente numeros maiores que 0"
        self.mensagemGanhou = "Ganhou"
        self.mensagemPerdeu = "Perdeu"

        self.validaPrimeiroNumeroMaiorQue60 = int(self.valorApostaPrimeiroNumero) > 60
        self.validaSegundoNumeroMaiorQue60 = int(self.valorApostaSegundoNumero) > 60
        self.validaTerceiroNumeroMaiorQue60 = int(self.valorApostaTerceiroNumero) > 60
        self.validaQuartoNumeroMaiorQue60 = int(self.valorApostaQuartoNumero) > 60
        self.validaQuintoNumeroMaiorQue60 = int(self.valorApostaQuintoNumero) > 60
        self.validaSextoNumeroMaiorQue60 = int(self.valorApostaSextoNumero) > 60
        self.validaPrimeiroNumeroMenorIgualAZero = int(self.valorApostaPrimeiroNumero) <= 0
        self.validaSegundoNumeroMenorIgualAZero = int(self.valorApostaSegundoNumero) <= 0
        self.validaTerceiroNumeroMenorIgualAZero = int(self.valorApostaTerceiroNumero) <= 0
        self.validaQuartoNumeroMenorIgualAZero = int(self.valorApostaQuartoNumero) <= 0
        self.validaQuintoNumeroMenorIgualAZero = int(self.valorApostaQuintoNumero) <= 0
        self.validaSextoNumeroMenorIgualAZero = int(self.valorApostaSextoNumero) <= 0

        if(self.validaPrimeiroCampo and self.validaSegundoCampo and self.validaTerceiroCampo and
           self.validaQuartoCampo and self.validaQuintoCampo and self.validaSextoCampo):
            self.campoResultado["text"] = self.camposVaziosMensagem
        elif (self.validaPrimeiroCampo or self.validaSegundoCampo or self.validaTerceiroCampo or
                  self.validaQuartoCampo or self.validaQuintoCampo or self.validaSextoCampo):
            self.campoResultado["text"] = self.campoVazioMensagem
        elif(self.validaNumeroPrimeiroCampo and self.validaNumeroSegundoCampo and self.validaNumeroTerceiroCampo and
             self.validaNumeroQuartoCampo and self.validaNumeroQuintoCampo and self.validaNumeroSextoCampo):
            self.campoResultado["text"] = self.somenteNumerosMensagem
            self.limpaCamposApostaNumero()
        elif(self.validaNumeroPrimeiroCampo or self.validaNumeroSegundoCampo or self.validaNumeroTerceiroCampo or
             self.validaNumeroQuartoCampo or self.validaNumeroQuintoCampo or self.validaNumeroSextoCampo):
            self.campoResultado["text"] = self.somenteNumerosMensagem
            self.limpaCamposApostaNumero()
        elif(self.validaPrimeiroNumeroMaiorQue60 and self.validaSegundoNumeroMaiorQue60 and
             self.validaTerceiroNumeroMaiorQue60 and self.validaQuartoNumeroMaiorQue60 and
             self.validaQuintoNumeroMaiorQue60 and self.validaSextoNumeroMaiorQue60):
            self.campoResultado["text"] = self.numeroMenorQue60Mensagem
        elif(self.validaPrimeiroNumeroMaiorQue60 or self.validaSegundoNumeroMaiorQue60 or
             self.validaTerceiroNumeroMaiorQue60 or self.validaQuartoNumeroMaiorQue60 or
             self.validaQuintoNumeroMaiorQue60 or self.validaSextoNumeroMaiorQue60):
            self.campoResultado["text"] = self.numeroMenorQue60Mensagem
        elif(self.validaPrimeiroNumeroMenorIgualAZero and self.validaSegundoNumeroMenorIgualAZero and
             self.validaTerceiroNumeroMenorIgualAZero and self.validaQuartoNumeroMenorIgualAZero and
             self.validaQuintoNumeroMenorIgualAZero and self.validaSextoNumeroMenorIgualAZero):
            self.campoResultado["text"] = self.numeroMaiorQueZeroMensagem
        elif(self.validaPrimeiroNumeroMenorIgualAZero or self.validaSegundoNumeroMenorIgualAZero or
             self.validaTerceiroNumeroMenorIgualAZero or self.validaQuartoNumeroMenorIgualAZero or
             self.validaQuintoNumeroMenorIgualAZero or self.validaSextoNumeroMenorIgualAZero):
            self.campoResultado["text"] = self.numeroMaiorQueZeroMensagem
        elif(self.comparaPrimeiroValor and self.comparaSegundoValor and self.comparaTerceiroValor and
             self.comparaQuartoValor and self.comparaQuintoValor and self.comparaSextoValor):
            self.campoResultado["text"] = self.mensagemGanhou
            self.loteriaPrimeiroNumero["text"] = self.valorLoteriaPrimeiroNumero
            self.loteriaSegundoNumero["text"] = self.valorLoteriaSegundoNumero
            self.loteriaTerceiroNumero["text"] = self.valorLoteriaTerceiroNumero
            self.loteriaQuartoNumero["text"] = self.valorLoteriaQuartoNumero
            self.loteriaQuintoNumero["text"] = self.valorLoteriaQuintoNumero
            self.loteriaSextoNumero["text"] = self.valorLoteriaSextoNumero
        else:
            self.campoResultado["text"] = self.mensagemPerdeu
            self.loteriaPrimeiroNumero["text"] = self.valorLoteriaPrimeiroNumero
            self.loteriaSegundoNumero["text"] = self.valorLoteriaSegundoNumero
            self.loteriaTerceiroNumero["text"] = self.valorLoteriaTerceiroNumero
            self.loteriaQuartoNumero["text"] = self.valorLoteriaQuartoNumero
            self.loteriaQuintoNumero["text"] = self.valorLoteriaQuintoNumero
            self.loteriaSextoNumero["text"] = self.valorLoteriaSextoNumero

    def reiniciaApostaLoteria(self):
        self.campoResultadoTextoPadrao = "----------"
        self.limpaCamposLoteriaNumero()
        self.limpaCamposApostaNumero()
        self.campoResultado["text"] = self.campoResultadoTextoPadrao

    def limpaCamposLoteriaNumero(self):
        self.textoPadraoCamposLoteriaNumero = "*"
        self.loteriaPrimeiroNumero["text"] = self.textoPadraoCamposLoteriaNumero
        self.loteriaSegundoNumero["text"] = self.textoPadraoCamposLoteriaNumero
        self.loteriaTerceiroNumero["text"] = self.textoPadraoCamposLoteriaNumero
        self.loteriaQuartoNumero["text"] = self.textoPadraoCamposLoteriaNumero
        self.loteriaQuintoNumero["text"] = self.textoPadraoCamposLoteriaNumero
        self.loteriaSextoNumero["text"] = self.textoPadraoCamposLoteriaNumero

    def limpaCamposApostaNumero(self):
        self.apostaPrimeiroNumero.delete(0, "end")
        self.apostaSegundoNumero.delete(0, "end")
        self.apostaTerceiroNumero.delete(0, "end")
        self.apostaQuartoNumero.delete(0, "end")
        self.apostaQuintoNumero.delete(0, "end")
        self.apostaSextoNumero.delete(0, "end")


root = Tk()
LoteriaPythonTela(root)
root.geometry("600x500") # "x" e "y" -> "600x500" -> x=600 e y=500
root.title("Loteria Python")
root.resizable(False,False) # "x" e "y" -> "600x500" -> x=600 e y=500
root.mainloop()
