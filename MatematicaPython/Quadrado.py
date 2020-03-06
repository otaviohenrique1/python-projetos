import math;

class Quadrado(object):
    def __init__(self, x):
        self.x = x;

    def calcula_area(self):
        return 'Area do quadrado: ' + str(float(self.x) ** 2);

    def calcula_perimetro(self):
        return 'Perimetro do quadrado: ' + str(float(self.x) * 4);

# Teste da classe Quadrado
quadradoTeste1 = Quadrado(2);
print(quadradoTeste1.calcula_area());
print(quadradoTeste1.calcula_perimetro());
