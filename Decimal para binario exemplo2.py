#Converter decimal para binario
import math
import array
import string
import plistlib

def binario(n):
   if n > 1:#Verifica se o numero é maior que 1
       binario(n//2)#Divisão inteira do numero por 2
   print(n % 2,end = '')#Imprime os restos das divisões

decimal = input("Digite o ip em numeros inteiros: ")
n1,n2,n3,n4 = (decimal.split("."))
print(n1,n2,n3,n4)
#numero(decimal)
#binario()
