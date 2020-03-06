
print("1 : Para Adição")
print("2 : Para Subtração")
print("3 : Para Divisão")
print("4 : Para Multiplicação")
print("5 : Para Potenciação")
print("6 : Para Raticiação")
o = float(input("Escolha uma operação :"))

if o == 1:
    x1 = float(input("Digite numero para x1:"))
    x2 = float(input("Digite numero para x2:"))
    x3 = (x1 + x2)
    print("Resultado:",x3)
elif o == 2:
    x1 = float(input("Digite numero para x1:"))
    x2 = float(input("Digit
    x2 = float(input("Digite numero para x2:"))
    x3 = (x1 ** x2)e numero para x2:"))
    x3 = (x1 - x2)
    print("Resultado:",x3)
elif o == 3:
    x1 = float(input("Digite numero para x1:"))
    x2 = float(input("Digite numero para x2:"))
    x3 = (x1 / x2)
    print("Resultado:",x3)
elif o == 4:
    x1 = float(input("Digite numero para x1:"))
    x2 = float(input("Digite numero para x2:"))
    x3 = (x1 * x2)
    print("Resultado:",x3)
elif o == 5:
    x1 = float(input("Digite numero para x1:"))
    print("Resultado:",x3)
elif o == 6:
    x1 = float(input("Digite numero para x1:"))
    x2 = float(input("Digite numero para x2:"))
    x3 = (x1 ** (1/x2))
    print("Resultado:",x3)
else:
    print("Essa opção não existe")