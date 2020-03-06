print(9 + 8)
print(9 * 8)
print(9 - 8)
print(9 / 8)
print(9 // 8) #Divisão com arredondamento
print(9 % 8)
print(9 ^ 8)

x1 = float(input("Digite numero para x1: "))
x2 = float(input("Digite numero para x1: "))

z1 = float(input("Digite numero para z1: "))
z2 = float(input("Digite numero para z1: "))

y1 = float(input("Digite numero para y1: "))
y2 = float(input("Digite numero para y1: "))

a1 = float(input("Digite numero para a1: "))
a2 = float(input("Digite numero para a1: "))

b1 = float(input("Digite numero para b1: "))
b2 = float(input("Digite numero para b1: "))

x3 = x1 * x2# Multiplicação
z3 = z1 / z2#Divisão
y3 = y1 - y2#Subtração
a3 = a1 + a2#Adição
b3 = b1 ** b2#Potenciação
#Para raticiação eleva a numero com ponto flutuante exemplo(81 ** 0.5 = 9)
# ou eleva-se o numero a uma fração exemplo(81 ** (1/2) = 9)
print("O resultado da multiplicação de", x1, "*", x2, "é iqual a:", x3)
print("O resultado da divisão de", z1, "/", z2, "é iqual a:", z3)
print("O resultado da subtração de", y1, "-", y2, "é iqual a:", y3)
print("O resultado da adição de", a1, "+", a2, "é iqual a:", a3)
print("O resultado da potenciação de", b1, "**", b2, "é iqual a:", b3)
#import math é a biblioteca de operações matematicas do python