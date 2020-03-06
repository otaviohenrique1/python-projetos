import math;
class OperacoesMatematicas():
    def adicao(valor1, valor2):
        return float(valor1) + float(valor2);
    def subtracao(valor1, valor2):
        return float(valor1) - float(valor2);
    def divisao(valor1, valor2):
        return float(valor1) / float(valor2);
    def multiplicao(valor1, valor2):
        return float(valor1) * float(valor2);
    def sinal(valor1):
        return float(valor1) * -1;
    def porcentagem(valor1):
        return float(valor1) / 100;
    def inverso(valor1):
        return 1 / float(valor1);
    def numero_pi(self):
        return math.pi;
    def potencia_2(valor1):
        return math.pow(float(valor1), 2);
    def potencia_3(valor1):
        return math.pow(float(valor1), 3);
    def potencia_x(valor1, valor2):
        return math.pow(float(valor1), float(valor2));
    def raiz_2(valor1):
        return math.sqrt(float(valor1), 2);
    def raiz_3(valor1):
        return math.sqrt(float(valor1), 3);
    def raiz_x(valor1, valor2):
        return math.sqrt(float(valor1), float(valor2));

if(__name__ == '__main__'):
    resultado = OperacoesMatematicas;
    print(resultado.adicao(1, 2));
    print(resultado.subtracao(1, 2));
    print(resultado.divisao(1, 2));
    print(resultado.multiplicao(1, 2));
