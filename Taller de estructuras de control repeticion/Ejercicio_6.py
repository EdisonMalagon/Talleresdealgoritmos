c=int(0)
a=int(input("Digite el dividendo: "))
d=int(input("Digite el divisor: "))
a=a-d
while(a>=0):
    c=c+1
    a=a-d
print("El resultado de la division es:"+str(c))