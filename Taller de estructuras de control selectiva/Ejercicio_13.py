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
if (mes_n==11 and (dia_n>=23 and dia_n<= 30)) or (mes_n== 12 and dia_n<= 21):
  Signo="sagitario"
if(mes_n== 12 and (dia_n>= 22 and dia_n<= 31)) or (mes_n==1 and dia_n<= 20):
  Signo="capricornio"
if(mes_n== 1 and (dia_n>= 21 and dia_n<= 31)) or (mes_n==2 and dia_n<= 19):
  Signo="acuario"
if(mes_n == 2 and (dia_n >= 20 and dia_n <= 29)) or (mes_n==3 and dia_n<= 20):
  Signo="piscis"
if(mes_n == 3 and (dia_n >= 21 and dia <= 31)) or (mes_n==4 and dia_n<=20):
  Signo="aries"
if(mes_n == 4 and (dia_n >= 21 and dia_n <= 30)) or (mes_n==5 and dia_n <= 20):
  Signo="tauro"
if(mes_n == 5 and (dia_n >= 22 and dia_n <= 31)) or (mes_n == 6 and dia_n <= 21):
  Signo="geminis"
if(mes_n == 6 and (dia_n >= 22 and dia_n <= 30)) or (mes_n == 7 and dia_n <= 22):
  Signo="cancer"
if(mes_n == 7 and (dia_n >= 23 and dia_n <= 31)) or (mes_n == 8 and dia_n <= 22):
  Signo="leo"
if (mes_n == 8 and (dia_n >= 23 and dia_n <= 31)) or (mes_n == 9 and dia_n <= 22):
  Signo="virgo"
if(mes_n == 9 and ( dia_n >= 23 and dia_n <= 30)) or (mes_n == 10 and dia_n <= 22):
  Signo="libra"
if (mes_n == 10 and (dia_n >= 23 and dia_n <= 31)) or (mes_n == 11 and dia_n <= 22):
  Signo="escorpion"
#salida
print(edad)
print(Signo)