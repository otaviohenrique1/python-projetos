#Exemplo de lista
x = ['1','2','3','4','5','6']
y = [1,2,3,4,5,6]
c = ['a','b','c','d','e','f','g']
j = [15,25,35,45,55,65]
k = [100,215,33,48,45,164]
#Imprime lista
print (x)
print (y)
# Varrendo a lista
for a in j:
    print (j)
# Trocar o último elemento
x[-1] = '9'
# Incluir item
x.append('10')
# Remover item
x.remove('2')
# Ordenar a lista
k.sort()
# Inverte a lista
c.reverse()
# Imprime numerado
for i, b in enumerate(y):
    print (i + 1, '=>', b)
# Imprime do segundo item em diante
print (x[1:])






#Pilhas e filas
#Metodo pop() facilita a implementação de filas e pilhas
lista = ['A','B','C']
print ('lista:',lista)
# A lista vazia é avaliada como falsa
while lista:
# Em filas, o primeiro item é o primeiro a sair
# pop(0) remove e retorna o primeiro item
    print ('Saiu', lista.pop(0), ', faltam', len(lista))
# Mais itens na lista
lista += ['D','E','F']
print ('lista:',lista)
while lista:
# Em pilhas, o primeiro item é o último a sair
# pop() remove e retorna o último item
    print ('Saiu',lista.pop(),', faltam',len(lista))




#Tuplas
tupla = (1,[2,3])
#Elementos da tupla referenciados
primeiro_elemento = tupla[0]
#Listas convertidas em tuplas
tupla = tuple(lista)
#Listas convertidas em tuplas
lista = list(tupla)
