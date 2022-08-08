Preciopagado=float(input("Ingrese precio que pago "))
Preciopublico=float(input("Ingrese precio al publico  "))
ppd=abs(((Preciopagado*100)/Preciopublico)-100)
print("Descuento aplicado", ppd)
