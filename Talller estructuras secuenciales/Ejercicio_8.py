import math 
#entradas
a=float(input("Ingrese lado a: "))
b=float(input("Ingrese lado b: "))
c=float(input("ingrese lado c: "))
#caja negra
s=(a+b+c)/2
area= math.sqrt(s*(s-a)(s-b)(s-c))
#salida
print("promedio: "+str(area))