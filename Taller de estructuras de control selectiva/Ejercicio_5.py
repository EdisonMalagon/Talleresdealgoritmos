
sueldo=int(input("Digite el valor del sueldo devengado: $"))
ventas_Dep_1=int(input("Digite el valor de las ventas del departamento 1: $"))
ventas_Dep_2=int(input("Digite el valor de las ventas del departamento 2: $"))
ventas_Dep_3=int(input("Digite el valor de las ventas del departamento 3: $"))
venta_total=ventas_Dep_1+ventas_Dep_2+ventas_Dep_3
Comisión=venta_total*0.33
if(ventas_Dep_1>Comisión):
    Sueldo_Dep_1=sueldo+sueldo*0.20
else:
    Sueldo_Dep_1=sueldo
if(ventas_Dep_2>Comisión):
    Sueldo_Dep_2=sueldo+sueldo*0.20
else:
    Sueldo_Dep_2=sueldo
if(ventas_Dep_3>Comisión):
    Sueldo_Dep_3=sueldo+sueldo*0.20
else:
    Sueldo_Dep_3=sueldo
print("Las ventas del departamento 1 son: $",Sueldo_Dep_1)
print("Las ventas del departamento 2 son: $",Sueldo_Dep_2)
print("Las ventas del departamento 3 son: $",Sueldo_Dep_3)