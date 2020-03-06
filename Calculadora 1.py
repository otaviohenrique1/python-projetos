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
    a = 0
    b = 0
    c = 0
    a = int(input("Numero"))
    b = int(input("Numero"))
    c = a + b
    print("Resultado: " , c)

# Subtração
elif i == 2:
    a = 0
    b = 0
    c = 0
    a = int(input("Numero"))
    b = int(input("Numero"))
    c = a - b
    print("Resultado: " , c)

# Multiplicação
elif i == 3:
    a = 0
    b = 0
    c = 0
    a = int(input("Numero"))
    b = int(input("Numero"))
    c = a * b
    print("Resultado: " , c)

# Divisão
elif i == 4:
    a = 0
    b = 0
    c = 0
    a = int(input("Numero"))
    b = int(input("Numero"))
    c = a / b
    print("Resultado: " , c)

# Potencia
elif i == 5:
    a = int(input("Numero"))
    b = int(input("Potencia"))
    a = 0
    b = 0
    c = 0
    c = a ** b
    print("Resultado: " , c)

# Radiciação
elif i == 6:
    a = int(input("Numero"))
    b = int(input("Raiz"))
    a = 0
    b = 0
    c = 0
    c = a ** 1/b
    print("Resultado: " , c)
