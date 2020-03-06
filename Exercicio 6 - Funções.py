#Exemplo de função
def fun(f):
    #Codigos
    print ("Exemplo de função")
    return f
#Exemplo de fatorial
def fatorial(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * i
    return j
    # Testando
for i in range(1, 6):
    print (i, '->', fatorial(i))



def soma(x,y):
    l = 0
    l = x + y
    return l
print ("Soma :", soma(12,27))

