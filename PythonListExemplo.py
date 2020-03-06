# -----List-----
lista = ["apple", "banana", "cherry"]
print(lista)
# -----Acessar Itens-----
lista = ["apple", "banana", "cherry"]
print(lista[1])
# -----Alterar valor do item-----
lista = ["apple", "banana", "cherry"]
lista[1] = "blackcurrant"
print(lista[1])
# -----Loop através de uma lista-----
lista = ["apple", "banana", "cherry"]
for x in lista:
    print(x)
# -----Verifique se o item existe-----
lista = ["apple", "banana", "cherry"]
if("apple" in lista):
    print("'apple' existe na list 'lista'")
# -----Comprimento da lista-----
lista = ["apple", "banana", "cherry"]
print(len(lista))
# -----Adicionar itens-----
lista = ["apple", "banana", "cherry"]
lista.append("orange")
print(lista)
lista = ["apple", "banana", "cherry"]
lista.insert(1, "orange")
print(lista)
# -----Remover item-----
lista = ["apple", "banana", "cherry"]
lista.remove("banana")
print(lista)
lista = ["apple", "banana", "cherry"]
lista.pop()
print(lista)
lista = ["apple", "banana", "cherry"]
del lista[0]
print(lista)
lista = ["apple", "banana", "cherry"]
del lista
lista = ["apple", "banana", "cherry"]
lista.clear()
print(lista)
# -----Copiar uma lista-----
lista = ["apple", "banana", "cherry"]
lista2 = lista.copy()
print(lista2)
lista = ["apple", "banana", "cherry"]
lista3 = list(lista)
print(lista3)
# -----O construtor list()-----
lista = list(("apple", "banana", "cherry"))
print(lista)
# -----extend()-----
fruits = ["apple", "banana", "cherry"]
cars = ["Ford", "BMW", "Volvo"]
fruits.extend(cars)
print(fruits)
print(cars)
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
print(cars)
# -----count()-----
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
# -----index()-----
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
# -----reverse()-----
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# -----sort()-----
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
def myFunc(e):
  return e['year']
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
