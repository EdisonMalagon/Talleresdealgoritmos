import math
math.sqrt
A=float(input("Ditige el valor de A: "))
B=float(input("Digite el valor de B: "))
C=float(input("Digite el valor de C: "))
D=B**2-4*A*C
if (D==0):
 X1=-B/(2*A)
 X2=-B/(2*A)
 print(X1)
 print(X2)
if (D>0):
  X1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
  X2=(-B-math.sqrt(B**2-4*A*C))/(2*A)
  print(X1)
  print(X2)
if (D<0):
  print("No tiene solucion real")
