Sb=int(input("Introduzca el sueldo devengado por el empleado: $"))
Cate=int(input("Digite la categoria a la que pertenece el empleado: "))
#Caja negra
if(Sb>=5000000):
    Aumento=Sb*0.10
    print("La categoria del trabajador es: ",Cate)
elif(Sb>=4300000):
    Aumento=Sb*0.15
    print("La categoria del trabajador es: ",Cate)
elif(Sb>=3600000):
    Aumento=Sb*0.20
    print("La categoria del trabajador es: ",Cate)
elif(Sb>=2000000):
    Aumento=Sb*0.40
    print("La categoria del trabajador es: ",Cate)
elif(Sb>=900000):
    Aumento=Sb*0.60
    print("La categoria del trabajador es: ",Cate)
#Salidas
print("El nuevo saldo bruto del trabajador es de: $",Sb+Aumento)