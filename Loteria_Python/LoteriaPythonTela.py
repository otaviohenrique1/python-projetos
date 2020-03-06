from tkinter import *
from random import *
from re import *

class LoeriaPythonTela:
    def __init__(self, master = None):
        # Fonte dos textos
        self.fonteAreaNumerosLoteria = ("Arial", "15")
        self.fonteTituloLoteria = ("Arial", "30")

        # Tela do titulo
        self.telaTitulo = Frame(master)
        self.telaTitulo["padx"] = 20
        self.telaTitulo["pady"] = 20
        self.telaTitulo.pack(side=TOP)

        # Tela dos numeros da loteria
        self.areaNumerosLoteria = Frame(master)
        self.areaNumerosLoteria["padx"] = 20
        self.areaNumerosLoteria["pady"] = 20
        self.areaNumerosLoteria.pack(side=TOP)

        # Tela dos numeros da loteria
        self.areaNumerosAposta = Frame(master)
        self.areaNumerosAposta["padx"] = 20
        self.areaNumerosAposta["pady"] = 20
        self.areaNumerosAposta.pack(side=TOP)

        # Tela do resultado da loteria
        self.areaResultado = Frame(master)
        self.areaResultado["padx"] = 20
        self.areaResultado["pady"] = 20
        self.areaResultado["bd"] = 2
        self.areaResultado["relief"] = "groove"
        self.areaResultado.pack(side=TOP)

        # Tela do botao
        self.areaBotao = Frame(master)
        self.areaBotao["padx"] = 20
        self.areaBotao["pady"] = 20
        self.areaBotao.pack(side=TOP)

        # Titulo loteria
        self.tituloLoteria= Label(self.telaTitulo)
        self.tituloLoteria["padx"] = 10
        self.tituloLoteria["pady"] = 10
        self.tituloLoteria["bd"] = 2
        self.tituloLoteria["relief"] = "groove"
        self.tituloLoteria["font"] = self.fonteTituloLoteria
        self.tituloLoteria["text"] = "Loteria Python"
        self.tituloLoteria.pack(side=RIGHT)

        # Campos numeros da loteria
        self.loteriaPrimeiroNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaPrimeiroNumero["padx"] = 10
        self.loteriaPrimeiroNumero["pady"] = 10
        self.loteriaPrimeiroNumero["bd"] = 2
        self.loteriaPrimeiroNumero["relief"] = "groove"
        self.loteriaPrimeiroNumero["text"] = "*"
        self.loteriaPrimeiroNumero["width"] = 3
        self.loteriaPrimeiroNumero.pack(side=RIGHT)

        self.loteriaSegundoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaSegundoNumero["padx"] = 10
        self.loteriaSegundoNumero["pady"] = 10
        self.loteriaSegundoNumero["bd"] = 2
        self.loteriaSegundoNumero["relief"] = "groove"
        self.loteriaSegundoNumero["text"] = "*"
        self.loteriaSegundoNumero["width"] = 3
        self.loteriaSegundoNumero.pack(side=RIGHT)

        self.loteriaTerceiroNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaTerceiroNumero["padx"] = 10
        self.loteriaTerceiroNumero["pady"] = 10
        self.loteriaTerceiroNumero["bd"] = 2
        self.loteriaTerceiroNumero["relief"] = "groove"
        self.loteriaTerceiroNumero["text"] = "*"
        self.loteriaTerceiroNumero["width"] = 3
        self.loteriaTerceiroNumero.pack(side=RIGHT)

        self.loteriaQuartoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaQuartoNumero["padx"] = 10
        self.loteriaQuartoNumero["pady"] = 10
        self.loteriaQuartoNumero["bd"] = 2
        self.loteriaQuartoNumero["relief"] = "groove"
        self.loteriaQuartoNumero["text"] = "*"
        self.loteriaQuartoNumero["width"] = 3
        self.loteriaQuartoNumero.pack(side=RIGHT)

        self.loteriaQuintoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaQuintoNumero["padx"] = 10
        self.loteriaQuintoNumero["pady"] = 10
        self.loteriaQuintoNumero["bd"] = 2
        self.loteriaQuintoNumero["relief"] = "groove"
        self.loteriaQuintoNumero["text"] = "*"
        self.loteriaQuintoNumero["width"] = 3
        self.loteriaQuintoNumero.pack(side=RIGHT)

        self.loteriaSextoNumero = Label(self.areaNumerosLoteria, font=self.fonteAreaNumerosLoteria)
        self.loteriaSextoNumero["padx"] = 10
        self.loteriaSextoNumero["pady"] = 10
        self.loteriaSextoNumero["bd"] = 2
        self.loteriaSextoNumero["relief"] = "groove"
        self.loteriaSextoNumero["text"] = "*"
        self.loteriaSextoNumero["width"] = 3
        self.loteriaSextoNumero.pack(side=RIGHT)

        # Campos numeros da aposta
        self.apostaPrimeiroNumero = Entry(self.areaNumerosAposta)
        self.apostaPrimeiroNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaPrimeiroNumero["width"] = 3
        self.apostaPrimeiroNumero.pack(side=RIGHT)

        self.apostaSegundoNumero = Entry(self.areaNumerosAposta)
        self.apostaSegundoNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaSegundoNumero["width"] = 3
        self.apostaSegundoNumero.pack(side=RIGHT)

        self.apostaTerceiroNumero = Entry(self.areaNumerosAposta)
        self.apostaTerceiroNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaTerceiroNumero["width"] = 3
        self.apostaTerceiroNumero.pack(side=RIGHT)

        self.apostaQuartoNumero = Entry(self.areaNumerosAposta)
        self.apostaQuartoNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaQuartoNumero["width"] = 3
        self.apostaQuartoNumero.pack(side=RIGHT)

        self.apostaQuintoNumero = Entry(self.areaNumerosAposta)
        self.apostaQuintoNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaQuintoNumero["width"] = 3
        self.apostaQuintoNumero.pack(side=RIGHT)

        self.apostaSextoNumero = Entry(self.areaNumerosAposta)
        self.apostaSextoNumero["font"] = self.fonteAreaNumerosLoteria
        self.apostaSextoNumero["width"] = 3
        self.apostaSextoNumero.pack(side=RIGHT)

        # Titulo do resultado
        self.tituloResultado = Label(self.areaResultado)
        self.tituloResultado["padx"] = 10
        self.tituloResultado["pady"] = 10
        self.tituloResultado["width"] = 20
        self.tituloResultado["font"] = self.fonteAreaNumerosLoteria
        self.tituloResultado["text"] = "Resultado:"
        self.tituloResultado.pack(side=TOP)

        # Campo que exibe o resultado da loteria e os erros
        self.campoResultado = Label(self.areaResultado)
        self.campoResultado["padx"] = 10
        self.campoResultado["pady"] = 10
        self.tituloResultado["width"] = 20
        self.campoResultado["font"] = self.fonteAreaNumerosLoteria
        self.campoResultado["text"] = "----------"
        self.campoResultado["width"] = 40
        self.campoResultado.pack(side=TOP)

        # Botao realiza aposta
        self.realizaAposta = Button(self.areaBotao)
        self.realizaAposta["text"] = "Realiza aposta"
        self.realizaAposta["font"] = self.fonteAreaNumerosLoteria
        self.realizaAposta["command"] = self.realizaApostaLoteria
        self.realizaAposta.pack(side=LEFT)

        # Botao reinicia aposta
        self.realizaReinicia = Button(self.areaBotao)
        self.realizaReinicia["text"] = "Reinicia aposta"
        self.realizaReinicia["font"] = self.fonteAreaNumerosLoteria
        self.realizaReinicia["command"] = self.reiniciaApostaLoteria
        self.realizaReinicia.pack(side=LEFT)

        # Numero aleatorio
        self.valorLoteriaPrimeiroNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaSegundoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaTerceiroNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaQuartoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaQuintoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaSextoNumero = self.geraNumeroAleatorio(1, 60)

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

        self.validaPrimeiroCampo = self.valorApostaPrimeiroNumero == ""
        self.validaSegundoCampo = self.valorApostaSegundoNumero == ""
        self.validaTerceiroCampo = self.valorApostaTerceiroNumero == ""
        self.validaQuartoCampo = self.valorApostaQuartoNumero == ""
        self.validaQuintoCampo = self.valorApostaQuintoNumero == ""
        self.validaSextoCampo = self.valorApostaSextoNumero == ""

        self.validaNumeroPrimeiroCampo = findall("[a-zA-Z]", self.valorApostaPrimeiroNumero)
        self.validaNumeroSegundoCampo = findall("[a-zA-Z]", self.valorApostaSegundoNumero)
        self.validaNumeroTerceiroCampo = findall("[a-zA-Z]", self.valorApostaTerceiroNumero)
        self.validaNumeroQuartoCampo = findall("[a-zA-Z]", self.valorApostaQuartoNumero)
        self.validaNumeroQuintoCampo = findall("[a-zA-Z]", self.valorApostaQuintoNumero)
        self.validaNumeroSextoCampo = findall("[a-zA-Z]", self.valorApostaSextoNumero)

        if(self.validaPrimeiroCampo and self.validaSegundoCampo and self.validaTerceiroCampo and
           self.validaQuartoCampo and self.validaQuintoCampo and self.validaSextoCampo):
            self.campoResultado["text"] = "Campos vazios"
        elif (self.validaPrimeiroCampo or self.validaSegundoCampo or self.validaTerceiroCampo or
              self.validaQuartoCampo or self.validaQuintoCampo or self.validaSextoCampo):
            self.campoResultado["text"] = "Campo vazio"
        elif(self.validaNumeroPrimeiroCampo and self.validaNumeroSegundoCampo and self.validaNumeroTerceiroCampo and
             self.validaNumeroQuartoCampo and self.validaNumeroQuintoCampo and self.validaNumeroSextoCampo):
            self.campoResultado["text"] = "Somente numeros nos campos"
            self.limpaCamposApostaNumero()
        elif(self.validaNumeroPrimeiroCampo or self.validaNumeroSegundoCampo or self.validaNumeroTerceiroCampo or
             self.validaNumeroQuartoCampo or self.validaNumeroQuintoCampo or self.validaNumeroSextoCampo):
            self.campoResultado["text"] = "Somente numeros nos campos"
            self.limpaCamposApostaNumero()
        elif(int(self.valorApostaPrimeiroNumero) > 60 and int(self.valorApostaSegundoNumero) > 60 and
             int(self.valorApostaTerceiroNumero) > 60 and int(self.valorApostaQuartoNumero) > 60 and
             int(self.valorApostaQuintoNumero) > 60 and int(self.valorApostaSextoNumero) > 60):
            self.campoResultado["text"] = "Somente numeros menores ou iguais a 60"
        elif(int(self.valorApostaPrimeiroNumero) > 60 or int(self.valorApostaSegundoNumero) > 60 or
             int(self.valorApostaTerceiroNumero) > 60 or int(self.valorApostaQuartoNumero) > 60 or
             int(self.valorApostaQuintoNumero) > 60 or int(self.valorApostaSextoNumero) > 60):
            self.campoResultado["text"] = "Somente numeros menores ou iguais a 60"
        elif(int(self.valorApostaPrimeiroNumero) <= 0 and int(self.valorApostaSegundoNumero) <= 0 and
             int(self.valorApostaTerceiroNumero) <= 0 and int(self.valorApostaQuartoNumero) <= 0 and
             int(self.valorApostaQuintoNumero) <= 0 and int(self.valorApostaSextoNumero) <= 0):
            self.campoResultado["text"] = "Somente numeros maiores que 0"
        elif(int(self.valorApostaPrimeiroNumero) <= 0 or int(self.valorApostaSegundoNumero) <= 0 or
             int(self.valorApostaTerceiroNumero) <= 0 or int(self.valorApostaQuartoNumero) <= 0 or
             int(self.valorApostaQuintoNumero) <= 0 or int(self.valorApostaSextoNumero) <= 0):
            self.campoResultado["text"] = "Somente numeros maiores que 0"
        elif(self.comparaPrimeiroValor and self.comparaSegundoValor and self.comparaTerceiroValor and
             self.comparaQuartoValor and self.comparaQuintoValor and self.comparaSextoValor):
            self.campoResultado["text"] = "Ganhou"
            self.loteriaPrimeiroNumero["text"] = self.valorLoteriaPrimeiroNumero
            self.loteriaSegundoNumero["text"] = self.valorLoteriaSegundoNumero
            self.loteriaTerceiroNumero["text"] = self.valorLoteriaTerceiroNumero
            self.loteriaQuartoNumero["text"] = self.valorLoteriaQuartoNumero
            self.loteriaQuintoNumero["text"] = self.valorLoteriaQuintoNumero
            self.loteriaSextoNumero["text"] = self.valorLoteriaSextoNumero
        else:
            self.campoResultado["text"] = "Perdeu"
            self.loteriaPrimeiroNumero["text"] = self.valorLoteriaPrimeiroNumero
            self.loteriaSegundoNumero["text"] = self.valorLoteriaSegundoNumero
            self.loteriaTerceiroNumero["text"] = self.valorLoteriaTerceiroNumero
            self.loteriaQuartoNumero["text"] = self.valorLoteriaQuartoNumero
            self.loteriaQuintoNumero["text"] = self.valorLoteriaQuintoNumero
            self.loteriaSextoNumero["text"] = self.valorLoteriaSextoNumero

    def reiniciaApostaLoteria(self):
        self.loteriaPrimeiroNumero["text"] = "*"
        self.loteriaSegundoNumero["text"] = "*"
        self.loteriaTerceiroNumero["text"] = "*"
        self.loteriaQuartoNumero["text"] = "*"
        self.loteriaQuintoNumero["text"] = "*"
        self.loteriaSextoNumero["text"] = "*"
        self.limpaCamposApostaNumero()
        self.campoResultado["text"] = "----------"

    def limpaCamposApostaNumero(self):
        self.apostaPrimeiroNumero.delete(0, "end")
        self.apostaSegundoNumero.delete(0, "end")
        self.apostaTerceiroNumero.delete(0, "end")
        self.apostaQuartoNumero.delete(0, "end")
        self.apostaQuintoNumero.delete(0, "end")
        self.apostaSextoNumero.delete(0, "end")


root = Tk()
LoeriaPythonTela(root)
root.geometry("600x500") # "x" e "y" -> "600x500" -> x=600 e y=500
root.title("Loteria Python")
root.resizable(False,False) # "x" e "y" -> "600x500" -> x=600 e y=500
root.mainloop()
