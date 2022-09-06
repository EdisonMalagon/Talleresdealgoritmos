lista=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
diccionario={}
for i in lista:
    a=lista.count(i)
    diccionario[i]=a
    #diccionario.update({i:a})
print(diccionario)