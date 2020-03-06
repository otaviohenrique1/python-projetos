#Pacotes são coleções de varios modulos, exemplos:
#Pacote de matematica, exemplos:
import math
print("Raiz :",math.sqrt(9))
print("Logaritmo :",math.log(2,5))
print("Logaritmo 1 + x :",math.log1p(2))
print("Logaritmo base 10 :",math.log10(2))
print("Fatorial :",math.factorial(10))
print("Cosseno :", math.cos(10))
print("Seno :", math.sin(10))
print("Base com expoente (base elevado(**) a expoente):", math.pow(2,9))
print("Base com expoente fracionario (base elevado(**) a 1/expoente):", math.pow(2,1/9))
print("-------------------------------------------------------------------------")

#Pacote de numeros complexos, exemplos:
import cmath
for cpx in [3j, 1.5 + 1j, -2 - 2j]:
    plr = cmath.polar(cpx)
    print ('Complexo:', cpx)
    print ('Forma polar:', plr, '(em radianos)')
    print ('Amplitude:', abs(cpx))
    print ('Ângulo:', math.degrees(plr[1]), '(graus)')
print("-------------------------------------------------------------------------")

#Pacote random, que gera numeros aleatorios, exemplos:
import random
import string

# Escolha uma letra
print (random.choice(string.ascii_uppercase))
# Escolha um número de 1 a 10
print (random.randrange(1, 11))
# Escolha um float no intervalo de 0 a 1
print (random.random())
print("-------------------------------------------------------------------------")

#Pacote de decimais, exemplos:
#import decimal
from decimal import *
t = 5.
for i in range(50):
    t = t - 0.1
print ('Float:', t)
t = Decimal('5.')
for i in range(50):
    t = t - Decimal('0.1')
print ('Decimal:', t)
print("-------------------------------------------------------------------------")




#Pacote de frações, exemplos:
from fractions import Fraction
# Três frações
f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')
print ("Fraction('-2/3') =", f1)
print ("Fraction('3, 4') =", f2)
print ("Fraction('.25') =", f3)
# Soma
print (f1, '+', f2, '=', f1 + f2)
print (f2, '+', f3, '=', f2 + f3)
print("-------------------------------------------------------------------------")


