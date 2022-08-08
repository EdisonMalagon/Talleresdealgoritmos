sueldo=float(input("ingresa el sueldo base: "))
a=float(input("ingresa venta 1: "))
b=float(input("ingresa venta 2: "))
c=float(input("ingresa venta 3: "))
#caja negra
comision=(a+b+c)*.10
#salidas
print("el sueldo del vendedor es: $", sueldo)
print("la comision por las tres ventas del mes es: $", comision)
print("el sueldo total con la comision es: $", sueldo+comision)