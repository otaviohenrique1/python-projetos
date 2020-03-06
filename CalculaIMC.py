# -*- coding: UTF-8 -*-

class CalculaIMC(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome;
        self.peso = peso;
        self.altura = altura;
    def imprime(self):
        imc = self.peso/(self.altura **2);
        print('O IMC de %s é: %s ' % (self.nome, imc));