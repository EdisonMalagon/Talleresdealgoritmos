#libreria
from datetime import date
today=date.today()
dia_a=today.day
mes_a=today.month
año_a=today.year

#Entradas
fecha_nacimiento=input("digite en este formato: año/mes/dia: ")
(año,mes,dia)=fecha_nacimiento.split("/")
año_n=int(año)
mes_n=int(mes)
dia_n=int(dia)
#caja negra
if(mes_a==mes_n):
  if(dia_n<=dia_a):
    edad=(año_a-año_n)
  else:
    edad=(año_a-año_n)-1
elif(mes_a>mes_n):
    edad=(año_a-año_n)
else:
  edad=(año_a-año_n)-1

#Signo zodiacal
Signo=""
if(dia_n>=22 and mes_n>=11 or dia_n>=21 and mes_n>=12):
  Signo="sagitario"
if(dia_n>=22 or mes_n>=12 or dia_n<=20 and mes_n<=1):
  Signo="capricornio"
if(dia_n>=21 and mes_n>=1 or dia_n<=19 and mes_n<=2):
  Signo="acuario"
if(dia_n>=20 and mes_n>=2 or dia_n<=19 and mes_n<=3):
  Signo="piscis"
if(dia_n>=21 and mes_n>=3 or dia_n<=20 and mes_n<=4):
  Signo="aries"
if(dia_n>=21 and mes_n>=4 or dia_n<=21 and mes_n<=5):
  Signo="tauro"
if(dia_n>=22 and mes_n>=5 or dia_n<=21 and mes_n<=6):
  Signo="geminis"
if(dia_n>=22 and mes_n>=6 or dia_n<=22 and mes_n<=7):
  Signo="cancer"
if(dia_n>=23 and mes_n>=7 or dia_n<=23 and mes_n<=8):
  Signo="leo"
if(dia_n>=24 and mes_n>=8 or dia_n<=22 and mes_n<=9):
  Signo="virgo"
if(dia_n>=23 and mes_n>=9 or dia_n<=23 and mes_n<=10):
  Signo="libra"
if(dia_n>=23 and mes_n>=10 or dia_n<=21 and mes_n<=11):
  Signo="escorpion"
#salida
print(edad)
print(Signo)