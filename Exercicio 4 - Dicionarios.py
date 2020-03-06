#Exemplo de dicionario
d = {'Letra':'a','Numero':'1','A':'B'}
print(d)


#Imprimindo elemento
print(d['Letra'])


#Adicionando elementos
d['Carro'] = 'Ford'
print(d)


#Removendo elemento
del d['A']
print(d)


i = d.items()
print(i)
c = d.keys()
print(c)
v = d.values()
print(v)