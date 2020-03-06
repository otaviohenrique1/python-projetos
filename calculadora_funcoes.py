class calculadora(object):
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

    def divisao(self, x, y):
        return x / y

    def multiplicacao(self, x, y):
        return x * y


if __name__ == '__main__':
    calculadora = calculadora();
    print("Soma: ", calculadora.soma(2, 2))
    print("Subtracao: ", calculadora.subtracao(2, 2))
    print("Multiplicacao: ", calculadora.multiplicacao(2, 2))
    print("Divisao: ", calculadora.divisao(2, 2))
