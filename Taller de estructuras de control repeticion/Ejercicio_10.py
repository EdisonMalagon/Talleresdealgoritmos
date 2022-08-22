cantidad=int(input("Digite la cantidad de estudiantes: "))
altura_mayor=0
for i in range(1,cantidad+1):
    altura=float(input("Digite altura: "))
    if(altura_mayor<=altura):
        altura_mayor=altura
print(altura_mayor)