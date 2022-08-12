
km_recorridos=int(input("Escriba la cantidad de km recorridos: "))
km_adicional=int(input("Escriba la cantidad de kilometros adicionales: "))
if(km_recorridos<=300):
    Valor_a_pagar=50000
else:
    if(km_recorridos>300) and (km_recorridos<1000):
        Valor_a_pagar=70000+(30000*km_adicional)
    elif(km_recorridos>1000):
        Valor_a_pagar=150000+(9000*km_adicional)
print("El valor a pagar es de: $",Valor_a_pagar)