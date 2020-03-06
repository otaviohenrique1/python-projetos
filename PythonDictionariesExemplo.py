carro1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
print(carro1)
x1 = carro1["modelo"]
x2 = carro1.get("modelo")
carro1["ano"] = 2018
for x in carro1:
    print(x)
for x in carro1:
    print(carro1[x])
for x in carro1.values():
    print(x)
for x, y in carro1.items():
    print(x, y)
if("modelo" in carro1):
    print("'modelo' existe em carro")
print(len(carro1))
carro1["cor"] = "vermelho"
print(carro1)
carro1.pop("cor")
print(carro1)
carro1.popitem()
print(carro1)
del carro1["modelo"]
print(carro1)
carro2 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
carro2.clear()
print(carro2)
carro3 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
carro4 = carro3.copy()
print(carro4)
carro5 = dict(carro3)
print(carro5)
carro6 = dict(marca="Ford", modelo="Mustang", ano=1964)
print(carro6)
x3 = ('a1', 'a2', 'a3')
y1 = 2
lista1 = dict.fromkeys(x3, y1)
print(lista1)
x4 = ('a1', 'a2', 'a3')
lista2 = dict.fromkeys(x4)
print(lista2)
carro7 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
x5 = carro7.keys()
print(x5)
carro8 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
x6 = carro8.keys()
carro8["cor"] = "branco"
print(x6)
carro9 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
x7 = carro9.setdefault("model", "Bronco")
print(x7)
carro10 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
x8 = carro10.setdefault("color", "white")
print(x8)
carro11 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": "1964"
}
carro11.update({"cor": "Branco"})
print(carro11)
