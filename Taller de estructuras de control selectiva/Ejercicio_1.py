
Can=int(input("Escriba la cantidad invertida: $"))
Tasa=float(input("Escriba la tasa de interes: "))

Inte=Can*Tasa
if(Inte>100000):

    print("El interes obtenido es: ",Inte, "supera los 100000")
else:

    print("El interes obtenido es: ",Inte, "no supera los 100000")

print("El monto total existente en la cuenta es de: ",Can+Inte)