import math

print("Calculadora 1")
print ("Adição - 1")
print ("Subtração - 2")
print ("Multiplicação - 3")
print ("Divisão- 4")
print ("Potenciação - 5")
print ("Radiciação - 6")
i = int(input("Escolha operação matematica"))

# Adição
if i == 1:
    def adicao(x,y):
        k = 0
        k = x + y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , adicao(a,b))

# Subtração
elif i == 2:
    def subtracao(x,y):
        k = 0
        k = x - y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , subtracao(a,b))

# Multiplicação
elif i == 3:
    def multiplicacao(x,y):
        k = 0
        k = x * y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , multiplicacao(a,b))

# Divisão
elif i == 4:
    def divisao(x,y):
        k = 0
        k = x / y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , divisao(a,b))

# Potencia
elif i == 5:
    def potenciacao(x,y):
        k = 0
        k = x ** y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , potenciacao(a,b))

# Radiciação
elif i == 6:
    def radiciacao(x,y):
        k = 0
        k = x ** 1/y
        return k
    a = int(input("Numero"))
    b = int(input("Numero"))
    print("Resultado: " , radiciacao(a,b))
