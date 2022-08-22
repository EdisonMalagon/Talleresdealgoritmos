a=0
b=0
d=0
s="s"
c=0
f=0
h=0
i=0
while s=="s":
    c=c+1
    print("Encuesta número", c)
    x=input("Digite m= mujer y h= hombre: ")
    y=int(input("Digite su edad: "))
    z=input("Digite s= si toma alcohol y n= si no toma alcohol: ")
    if z=="s":
        q=7
        while q>6:
            q=int(input("1-Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro: "))
    if x=="m":
        if y>19:
            f=f+1
    if x=="h":
        if y>=20 and y<=25:
            if z=="s":
                if q!=1:
                    h=h+1
    if z=="s":
        a=a+1
        if q==3:
            b=b+1
            i=i+y
        elif q==5:
            d=d+1
    s=input("Si desea seguir digite s, sino cualquier otra letra: ")
print("Cantidad encuestados: ",c)
print("Personas que consumen licor: ",a)
print("Mujeres menores de edad: ",f)
print("Hombres que toman, pero no aguardiente entre 20 y 25: ",h)
if (b==0):
  print("Ningun encuestado consume cerveza")
else:
 print("Promedio edad personas que consumen cerveza: ",round(i/b,2))
print("Porcentaje de personas que consumen whisky: ",round(d/c*100,2))