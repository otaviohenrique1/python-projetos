#Converter decimal para binario
def binario(n1,n2,n3,n4):
   if n1 > 1 :
        if n2 > 1:
            if n3 > 1:
                if n4 > 1:
                    binario(n1//2, n2//2,n3//2, n4//2)
   print(n1 % 2,end = '')
   print(n2 % 2,end = '')
   print(n3 % 2,end = '')
   print(n4 % 2,end = '')
decimal1 = int(input("Digite um numero inteiro: "))
decimal2 = int(input("Digite um numero inteiro: "))
decimal3 = int(input("Digite um numero inteiro: "))
decimal4 = int(input("Digite um numero inteiro: "))
binario(decimal1,decimal2,decimal3,decimal4)