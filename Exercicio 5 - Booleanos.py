#Booleano(bol) especialização do inteiro(int) onde o 1 é true e o 0 é false
#Os operadores booleanos no Python são: and, or, not, is e in.

#and: retorna um valor verdadeiro se e somente se receber duas expressões que forem verdadeiras.
print (0 and 3) # Mostra 0
print (2 and 3) # Mostra 3

#or: retorna um valor falso se e somente se receber duas expressões que forem falsas.
print (0 or 3)  # Mostra 3
print (2 or 3) # Mostra 2

#not: retorna falso se receber uma expressão verdadeira e vice-versa.
print (not 0) # Mostra True
print (not 2) # Mostra False

#is: retorna verdadeiro se receber duas referências ao mesmo objeto e falso em caso contrário.
print (2 in (2, 3)) # Mostra True

#in: retorna verdadeiro se receber um item e uma lista e o item ocorrer uma ou mais vezes na lista e falso em caso contrário.
print (2 is 3) # Mostra False