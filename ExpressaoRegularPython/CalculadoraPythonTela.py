# -*- coding: UTF-8 -*-
from tkinter import *


class CalculadoraPythonTela:
    def __init__(self, master=None):
        self.fonte = ("Arial", "20")
        self.larguraBotoes = 5

        self.areaVisor = Frame(master)
        self.areaVisor.pack(side=TOP)
        self.areaBotoes = Frame(master).pack(side=TOP)
        self.areaLinhaBotoes1 = Frame(self.areaBotoes)
        self.areaLinhaBotoes1.pack(side=TOP)
        self.areaLinhaBotoes2 = Frame(self.areaBotoes)
        self.areaLinhaBotoes2.pack(side=TOP)
        self.areaLinhaBotoes3 = Frame(self.areaBotoes)
        self.areaLinhaBotoes3.pack(side=TOP)
        self.areaLinhaBotoes4 = Frame(self.areaBotoes)
        self.areaLinhaBotoes4.pack(side=TOP)
        self.areaLinhaBotoes5 = Frame(self.areaBotoes)
        self.areaLinhaBotoes5.pack(side=TOP)
        self.areaLinhaBotoes6 = Frame(self.areaBotoes)
        self.areaLinhaBotoes6.pack(side=TOP)

        self.visor = Label(self.areaVisor, font=self.fonte, padx=20, pady=20, width=20,
                           bd=2, relief="groove", text="0.0")
        self.visor.pack(side=RIGHT)

        self.botaoPorcentagem = Button(self.areaLinhaBotoes1, font=self.fonte, text="%",
                                       width=self.larguraBotoes, command=self.porcentagem)
        self.botaoPorcentagem.pack(side=LEFT)
        self.botaoRaizQuadrada = Button(self.areaLinhaBotoes1, font=self.fonte, text="Raiz2",
                                        width=self.larguraBotoes, command=self.raiz_quadrada)
        self.botaoRaizQuadrada.pack(side=LEFT)
        self.botaoPotenciaQuadrado = Button(self.areaLinhaBotoes1, font=self.fonte, text="^2",
                                            width=self.larguraBotoes, command=self.potencia_quadrado)
        self.botaoPotenciaQuadrado.pack(side=LEFT)
        self.botaoInverso = Button(self.areaLinhaBotoes1, font=self.fonte, text="1/x",
                                   width=self.larguraBotoes, command=self.inverso)
        self.botaoInverso.pack(side=LEFT)

        self.botaoApagaVisor = Button(self.areaLinhaBotoes2, font=self.fonte, text="CE",
                                      width=self.larguraBotoes, command=self.apaga_visor)
        self.botaoApagaVisor.pack(side=LEFT)
        self.botaoLimpaVisor = Button(self.areaLinhaBotoes2, font=self.fonte, text="C",
                                      width=self.larguraBotoes, command=self.limpa_visor)
        self.botaoLimpaVisor.pack(side=LEFT)
        self.botaoDelete = Button(self.areaLinhaBotoes2, font=self.fonte, text="Del",
                                  width=self.larguraBotoes, command=self.delete)
        self.botaoDelete.pack(side=LEFT)
        self.botaoDivisao = Button(self.areaLinhaBotoes2, font=self.fonte, text="/",
                                   width=self.larguraBotoes, command=self.divisao)
        self.botaoDivisao.pack(side=LEFT)

        self.botaoNumeroSete = Button(self.areaLinhaBotoes3, font=self.fonte, text="7",
                                      width=self.larguraBotoes, command=self.numero_sete)
        self.botaoNumeroSete.pack(side=LEFT)
        self.botaoNumeroOito = Button(self.areaLinhaBotoes3, font=self.fonte, text="8",
                                      width=self.larguraBotoes, command=self.numero_oito)
        self.botaoNumeroOito.pack(side=LEFT)
        self.botaoNumeroNove = Button(self.areaLinhaBotoes3, font=self.fonte, text="9",
                                      width=self.larguraBotoes, command=self.numero_nove)
        self.botaoNumeroNove.pack(side=LEFT)
        self.botaoMultiplicacao = Button(self.areaLinhaBotoes3, font=self.fonte, text="*",
                                         width=self.larguraBotoes, command=self.multiplicacao)
        self.botaoMultiplicacao.pack(side=LEFT)

        self.botaoNumeroQuatro = Button(self.areaLinhaBotoes4, font=self.fonte, text="4",
                                        width=self.larguraBotoes, command=self.numero_quatro)
        self.botaoNumeroQuatro.pack(side=LEFT)
        self.botaoNumeroCinco = Button(self.areaLinhaBotoes4, font=self.fonte, text="5",
                                       width=self.larguraBotoes, command=self.numero_cinco)
        self.botaoNumeroCinco.pack(side=LEFT)
        self.botaoNumeroSeis = Button(self.areaLinhaBotoes4, font=self.fonte, text="6",
                                      width=self.larguraBotoes, command=self.numero_seis)
        self.botaoNumeroSeis.pack(side=LEFT)
        self.botaoSubtracao = Button(self.areaLinhaBotoes4, font=self.fonte, text="-",
                                     width=self.larguraBotoes, command=self.subracao)
        self.botaoSubtracao.pack(side=LEFT)

        self.botaoNumeroUm = Button(self.areaLinhaBotoes5, font=self.fonte, text="1",
                                    width=self.larguraBotoes, command=self.numero_um)
        self.botaoNumeroUm.pack(side=LEFT)
        self.botaoNumeroDois = Button(self.areaLinhaBotoes5, font=self.fonte, text="2",
                                      width=self.larguraBotoes, command=self.numero_dois)
        self.botaoNumeroDois.pack(side=LEFT)
        self.botaoNumeroTres = Button(self.areaLinhaBotoes5, font=self.fonte, text="3",
                                      width=self.larguraBotoes, command=self.numero_tres)
        self.botaoNumeroTres.pack(side=LEFT)
        self.botaoAdicao = Button(self.areaLinhaBotoes5, font=self.fonte, text="+",
                                  width=self.larguraBotoes, command=self.adicao)
        self.botaoAdicao.pack(side=LEFT)

        self.botaoSinal = Button(self.areaLinhaBotoes6, font=self.fonte, text="+/-",
                                 width=self.larguraBotoes, command=self.troca_sinal_numero)
        self.botaoSinal.pack(side=LEFT)
        self.botaoNumeroZero = Button(self.areaLinhaBotoes6, font=self.fonte, text="0",
                                      width=self.larguraBotoes, command=self.numero_zero)
        self.botaoNumeroZero.pack(side=LEFT)
        self.botaoPonto = Button(self.areaLinhaBotoes6, font=self.fonte, text=".",
                                 width=self.larguraBotoes, command=self.ponto)
        self.botaoPonto.pack(side=LEFT)
        self.botaoIgual = Button(self.areaLinhaBotoes6, font=self.fonte, text="=",
                                 width=self.larguraBotoes, command=self.igual)
        self.botaoIgual.pack(side=LEFT)

    def numero_um(self):
        self.visor["text"] = "1"

    def numero_dois(self):
        self.visor["text"] = "2"

    def numero_tres(self):
        self.visor["text"] = "3"

    def numero_quatro(self):
        self.visor["text"] = "4"

    def numero_cinco(self):
        self.visor["text"] = "5"

    def numero_seis(self):
        self.visor["text"] = "6"

    def numero_sete(self):
        self.visor["text"] = "7"

    def numero_oito(self):
        self.visor["text"] = "8"

    def numero_nove(self):
        self.visor["text"] = "9"

    def numero_zero(self):
        self.visor["text"] = "0"

    def adicao(self):
        self.visor["text"] = "+"

    def subracao(self):
        self.visor["text"] = "-"

    def multiplicacao(self):
        self.visor["text"] = "*"

    def divisao(self):
        self.visor["text"] = "/"

    def igual(self):
        self.visor["text"] = "="

    def ponto(self):
        self.visor["text"] = "."

    def raiz_quadrada(self):
        self.visor["text"] = "Raiz2"

    def potencia_quadrado(self):
        self.visor["text"] = "^2"

    def inverso(self):
        self.visor["text"] = "1/x"

    def apaga_visor(self):
        self.visor["text"] = "0.0"

    def limpa_visor(self):
        self.visor["text"] = "0.0"

    def delete(self):
        self.visor["text"] = ""

    def troca_sinal_numero(self):
        self.visor["text"] = "+/-"

    def porcentagem(self):
        self.visor["text"] = "%"


root = Tk()
CalculadoraPythonTela(root)
root.geometry("400x450")
root.title("Calculadora Python")
root.resizable(False,False)
root.mainloop()
