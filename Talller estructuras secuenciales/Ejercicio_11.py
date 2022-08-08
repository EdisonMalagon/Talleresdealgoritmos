nombre=str(input("Ingrese el nombre del trabajador: "))
horas=int(input("Ingrese las horas trabajadas: "))
hora=float(input("Ingrese el pago por hora: "))
extras=int(input("Ingrese las horas extras trabajadas: "))
hijos=int(input("Ingrese el total de los hijos: "))
sb=hora*horas
asignacion=(250000+173000*hijos+180000)
deduccion=sb*(0.05+0.02+0.07)
salario_descuentos=sb-deduccion
x=hora*extras
z=x*0.25+x
sueldo_neto=asignacion+deduccion+z
print(f"Las asignaciones son: {asignacion}, las deducciones son: {deduccion} y el sueldo neto que recibira {nombre} en el mes de diciembre es de: {sueldo_neto} ")