Lectura_Anterior=float(input("Digite el valor de la lectura anterior: "))
Lectura_Actual=float(input("Digite el valor de la lectura Actual: "))

if (Lectura_Actual<=100):
  costo11=abs(Lectura_Anterior-Lectura_Actual)*4600
  costo_luz=Lectura_Actual*4600
  print("monto a pagar de aseo: ", costo11)
  print("monto a pagar de luz: ", costo_luz)
if (Lectura_Actual>=101 and Lectura_Actual<=300):
  costo11=abs(Lectura_Anterior-Lectura_Actual)*80000
  costo_luz=Lectura_Actual*80000
  print("monto a pagar de aseo: ", costo11)
  print("monto a pagar de luz: ", costo_luz)
if (Lectura_Actual>=301 and Lectura_Actual<=500):
  costo11=abs(Lectura_Anterior-Lectura_Actual)*100000
  costo_luz=Lectura_Actual*100000
  print("monto a pagar de aseo: ", costo11)
  print("monto a pagar de luz: ", costo_luz)
if (Lectura_Actual>=501):
  costo_luz=Lectura_Actual*120000
  costo11=abs(Lectura_Anterior-Lectura_Actual)*120000
  print("monto a pagar de aseo: ", costo11)
  print("monto a pagar de luz: ", costo_luz)