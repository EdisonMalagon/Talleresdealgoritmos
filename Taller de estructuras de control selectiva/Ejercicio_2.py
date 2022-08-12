
sueldo=int(input("Escriba el sueldo del trabajador: $"))
aumento=""
if(sueldo<900000):
    Aumento=sueldo*0.15
else:
    aumento=sueldo*0.12
print("El nuevo saldo del trabajador es: $",sueldo+aumento)