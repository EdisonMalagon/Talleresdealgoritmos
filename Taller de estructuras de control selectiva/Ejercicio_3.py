
A=int(input("Digite un valor para A: "))
B=int(input("Digite un valor para B: "))
C=int(input("Digite un valor para C: "))
D=int(input("Digite un valor para D: "))
formula1=((A-C)**2)/D
if(D>0):
    print(formula1)
elif(D==0):
    print("No es posible dividir por 0")
formula2=((A-B)**3)/D
if(D>0):
    print(formula2)
elif(D==0):
    print("No es posible dividir por 0")