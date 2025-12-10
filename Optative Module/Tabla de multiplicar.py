#_*_ coding: utf-8 _*_
lista = ""
for i in range(1, 11):
    for j in range(1,11):
        resultado = i * j
        lista += str(resultado) + "\t"
    lista += "\n"
print(lista)