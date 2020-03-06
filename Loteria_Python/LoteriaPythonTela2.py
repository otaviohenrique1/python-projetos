from tkinter import *;
from random import *;

class LoeriaPythonTela2:
    def __init__(self, master = None):
        # Fonte dos textos
        self.fonteAreaNumerosLoteria = ("Arial", "15")
        self.fonteTituloLoteria = ("Arial", "30")

        self.telaTitulo = self.criaFrame(master, 20, 20, TOP)

        self.areaNumerosLoteria = self.criaFrame(master, 20, 20, TOP)

        self.areaNumerosAposta = self.criaFrame(master, 20, 20, TOP)

        self.areaResultado = self.criaFrame(master, 20, 20, TOP)

        self.areaBotao = self.criaFrame(master, 20, 20, TOP)

        self.tituloLoteria = self.criaLabel(self.telaTitulo, 10, 10, 2, "groove",
                                            self.fonteTituloLoteria, "Loteria Python", RIGHT)

        # Campos numeros da loteria
        self.loteriaPrimeiroNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                    self.fonteTituloLoteria, "*", RIGHT)
        self.loteriaSegundoNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                   self.fonteTituloLoteria, "*", RIGHT)
        self.loteriaTerceiroNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                    self.fonteTituloLoteria, "*", RIGHT)
        self.loteriaQuartoNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                  self.fonteTituloLoteria, "*", RIGHT)
        self.loteriaQuintoNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                  self.fonteTituloLoteria, "*", RIGHT)
        self.loteriaSextoNumero = self.criaLabel(self.areaNumerosLoteria, 10, 10, 2, "groove",
                                                 self.fonteTituloLoteria, "*", RIGHT)

        # Campos numeros da aposta
        self.apostaPrimeiroNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                          self.fonteAreaNumerosLoteria, 3, RIGHT)
        self.apostaSegundoNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                         self.fonteAreaNumerosLoteria, 3, RIGHT)
        self.apostaTerceiroNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                          self.fonteAreaNumerosLoteria, 3, RIGHT)
        self.apostaQuartoNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                        self.fonteAreaNumerosLoteria, 3, RIGHT)
        self.apostaQuintoNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                        self.fonteAreaNumerosLoteria, 3, RIGHT)
        self.apostaSextoNumero = self.criaCampoDeTexto(self.areaNumerosAposta,
                                                       self.fonteAreaNumerosLoteria, 3, RIGHT)

        # Campo resultado
        self.campoResultado = self.criaLabel(self.areaResultado, 10, 10, 2, "groove",
                                             self.fonteAreaNumerosLoteria, "Resultado: ", RIGHT)

        # Botoes
        self.realizaAposta = self.criaBotao(self.areaBotao, "Realiza aposta",
                                            self.fonteAreaNumerosLoteria, self.realizaApostaLoteria, TOP)
        self.reiniciaAposta = self.criaBotao(self.areaBotao, "Rinicia aposta",
                                             self.fonteAreaNumerosLoteria, self.reiniciaApostaLoteria, TOP)
        self.geraNumeroSorteio()

    def geraNumeroSorteio(self):
        # Numero aleatorio
        self.valorLoteriaPrimeiroNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaSegundoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaTerceiroNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaQuartoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaQuintoNumero = self.geraNumeroAleatorio(1, 60)
        self.valorLoteriaSextoNumero = self.geraNumeroAleatorio(1, 60)

    def geraNumeroAleatorio(self, x, y):
        return randint(x, y)

    def criaFrame(self, local, padx, pady, valorSide):
        self.frame = Frame(local)
        self.frame["padx"] = padx
        self.frame["pady"] = pady
        self.frame.pack(side=valorSide)
        return self.frame

    def criaBotao(self, local, texto, fonte, comando, valorSide):
        self.botao = Button(local)
        self.botao["text"] = texto
        self.botao["font"] = fonte
        self.botao["command"] = comando
        self.botao.pack(side=valorSide)
        return self.botao

    def criaLabel(self, local, padx, pady, bordaLargura, bordaTipo, fonte, texto, valorSide):
        self.label = Label(local)
        self.label["padx"] = padx
        self.label["pady"] = pady
        self.label["font"] = fonte
        self.label["bd"] = bordaLargura
        self.label["relief"] = bordaTipo
        self.label["text"] = texto
        self.label.pack(side=valorSide)
        return self.label

    def criaCampoDeTexto(self, local, fonte, largura, valorSide):
        self.campoDeTexto = Entry(local)
        self.campoDeTexto["font"] = fonte
        self.campoDeTexto["width"] = largura
        self.campoDeTexto.pack(side=valorSide)
        return self.campoDeTexto

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

        if(self.comparaPrimeiroValor and
            self.comparaSegundoValor and
            self.comparaTerceiroValor and
            self.comparaQuartoValor and
            self.comparaQuintoValor and
            self.comparaSextoValor
        ):
            self.campoResultado["text"] = "Resultado: Ganhou"
            self.loteriaPrimeiroNumero["text"] = self.valorLoteriaPrimeiroNumero
            self.loteriaSegundoNumero["text"] = self.valorLoteriaSegundoNumero
            self.loteriaTerceiroNumero["text"] = self.valorLoteriaTerceiroNumero
            self.loteriaQuartoNumero["text"] = self.valorLoteriaQuartoNumero
            self.loteriaQuintoNumero["text"] = self.valorLoteriaQuintoNumero
            self.loteriaSextoNumero["text"] = self.valorLoteriaSextoNumero
        else:
            self.campoResultado["text"] = "Resultado: Perdeu"
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
        self.apostaPrimeiroNumero.delete(0, "end")
        self.apostaSegundoNumero.delete(0, "end")
        self.apostaTerceiroNumero.delete(0, "end")
        self.apostaQuartoNumero.delete(0, "end")
        self.apostaQuintoNumero.delete(0, "end")
        self.apostaSextoNumero.delete(0, "end")
        self.geraNumeroSorteio()

root = Tk()
LoeriaPythonTela2(root)
root.title("Loteria Python")
root.mainloop()
