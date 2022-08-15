Nc=(input("Escriba el nombre del cliente: "))
Cr=int(input("Digite el valor de la compra: $"))
if(Cr<50000):
    print("No es posible hacer descuento")
elif(Cr>=50000 and Cr<=100000):
    Descuento=Cr*0.05
    print("El descuento realizado a la compra es del 5%")
elif(Cr>=100000 and Cr<=700000):
    Descuento=Cr*0.11
    print("El descuento realizado a la compra es del 11%")
elif(Cr>=700000 and Cr<=1500000):
    Descuento=Cr*0.18
    print("El descuento realizado a la compra es del 18%")
elif(Cr>1500000):
    Descuento=Cr*0.25
    print("El descuento realizado a la compra es del 25%")
print("El valor de la compra realizada es de: $",Cr, "El monto total a pagar es de: $",Cr-Descuento, "El cliente que recibió el descuento aplicable es: ",Nc)