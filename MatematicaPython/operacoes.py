# -*- coding: utf-8 -*-
# class Numero(object):
#     def __init__(self, numero):
#         self.__numero = numero
#
#     def avalia(self):
#         return self.__numero
#
#     @property
#     def expressao_esquerda(self):
#         return self.__expressao_esquerda
#
#     @property
#     def expressao_direita(self):
#         return self.__expressao_direita
#
#     def aceita(self, visitor):
#         visitor.visita_subtracao(self)
#
# class Subtracao(object):
#     def __init__(self, expressao_esquerda, expressao_direita):
#         self.__expressao_esquerda = expressao_esquerda
#         self.__expressao_direita = expressao_direita
#
#     def avalia(self):
#         return (self.__expressao_esquerda.avalia()
#                 - self.__expressao_direita.avalia())
#
#     def aceita(self, visitor):
#         visitor.visita_soma(self)
#
#     @property
#     def expressao_esquerda(self):
#         return self.__expressao_esquerda
#
#     @property
#     def expressao_direita(self):
#         return self.__expressao_direita
#
# class Soma(object):
#     def __init__(self, expressao_esquerda, expressao_direita):
#         self.__expressao_esquerda = expressao_esquerda
#         self.__expressao_direita = expressao_direita
#
#     def avalia(self):
#         return (self.__expressao_esquerda.avalia()
#                 + self.__expressao_direita.avalia())
#
#     def aceita(self, visitor):
#         visitor.visita_numero(self)
#
# class Impressora(object):
#     def visita_soma(self, soma):
#         print('('),
#         soma.expressao_esquerda.aceita(self),
#         print('+'),
#         soma.expressao_direita.aceita(self),
#         print(')'),
#
#     def visita_subtracao(self, subtracao):
#         print('('),
#         subtracao.expressao_esquerda.aceita(self),
#         print('-'),
#         subtracao.expressao_direita.aceita(self),
#         print(')'),
#
#     def visita_numero(self, numero):
#         print(numero.avalia())
#
# class Prefixa_Visitor(object):
#     def visita_soma(self, soma):
#         print('+'),
#         print('('),
#         soma.expressao_esquerda.aceita(self)
#         soma.expressao_direita.aceita(self)
#         print(')'),
#
#     def visita_subtracao(self, subtracao):
#         print('-'),
#         print('('),
#         subtracao.expressao_esquerda.aceita(self)
#         subtracao.expressao_direita.aceita(self)
#         print(')'),
#
#     def visita_numero(self, numero):
#         print(numero.avalia()),
#
# if(__name__ == '__main__'):
#     expressao_esquerda = Subtracao(Numero(10), Numero(5))
#     expressao_direita = Soma(Numero(2), Numero(10))
#     expressao_conta = Soma(expressao_esquerda, expressao_direita)
#     visitor = Impressora()
#     expressao_conta.aceita(visitor)

# def calculaFuncao1(x):
#     return (3*(x-2)-2*(x-3))
# def calculaFuncao2(x):
#     return ((x**2)+x-2)
# print("a) " + str(calculaFuncao2(1) + calculaFuncao2(2)))
# print("b) " + str(calculaFuncao2(3)))

from math import *

def calculaFormulaBhaskaraEquacaoSegundoGrau(a, b, c):
    delta = pow(b, 2) - (4*a*c)
    x1 = ((b*(-1)+sqrt(delta)))/2*a
    x2 = ((b*(-1)-sqrt(delta)))/2*a
    return [x1,x2]
# print(calculaFormulaBhaskaraEquacaoSegundoGrau(1,-11,-60))

# teorema de pitagoras em python
# h**2 = c1**2 + c2**2
def calculaTeoremaComHipotenusa(cateto1, cateto2):
    # 1) h = raiz2(c1**2 + c2**2)
    # hipotenusa = sqrt(pow(cateto1, 2) + pow(cateto2, 2))
    return sqrt(pow(cateto1, 2) + pow(cateto2, 2))

def calculaTeoremaComCateto1(hipotenusa, cateto2):
    # 2) c1 = raiz2(h**2 - c2**2)
    # cateto1 = sqrt(pow(hipotenusa, 2) - pow(cateto2, 2))
    return sqrt(pow(hipotenusa, 2) - pow(cateto2, 2))

def calculaTeoremaComCateto2(hipotenusa, cateto1):
    # 3) c2 = raiz2(h**2 + c1**2)
    # cateto2 = sqrt(pow(hipotenusa, 2) + pow(cateto1, 2))
    return sqrt(pow(hipotenusa, 2) - pow(cateto1, 2))

# hipotenusa = 5
# cateto1 = 3
# cateto2 = 4

# hipotenusa = raiz2(4**2 + 3**2) -> hipotenusa = raiz2(16 + 9) -> hipotenusa = raiz2(25) -> hipotenusa = 5
print("calculaTeoremaComHipotenusa->" + str(calculaTeoremaComHipotenusa(3, 4)))

# cateto2 = raiz2(5**2 - 4**2) -> cateto2 = raiz2(25 - 9) -> cateto2 = raiz2(16) -> cateto2 = 4
print("calculaTeoremaComCateto1->" + str(calculaTeoremaComCateto1(5, 3)))

# cateto1 = raiz2(5**2 + 3**2) -> cateto1 = raiz2(25 - 16) -> cateto1 = raiz2(9) -> cateto1 = 3
print("calculaTeoremaComCateto2->" + str(calculaTeoremaComCateto2(5, 4)))

print(
    "Teorema de pitagoras em python" + "\n" +
    "cateto 1 = " + str(3) + "\n" +
    "cateto 2 = " + str(4) + "\n" +
    "hipotenusa = " + str(calculaTeoremaComHipotenusa(3, 4))
)

def calculaTeoremaDePitagoras(hipotenusa, cateto1, cateto2):
    if(hipotenusa==0):
        return sqrt(pow(cateto1, 2) + pow(cateto2, 2))
    elif(cateto1==0):
        return sqrt(pow(hipotenusa, 2) - pow(cateto2, 2))
    elif(cateto2==0):
        return sqrt(pow(hipotenusa, 2) - pow(cateto1, 2))
print(str(calculaTeoremaDePitagoras(10,6,0)))
