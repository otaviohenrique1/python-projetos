#Converter decimal para binario
def binario(n):

   if n > 1:#Verifica se o numero é maior que 1
       binario(n//2)#Divisão inteira do numero por 2
   print(n % 2,end = '')#Imprime os restos das divisões

decimal = int(input("Digite um numero inteiro: "))
binario(decimal)