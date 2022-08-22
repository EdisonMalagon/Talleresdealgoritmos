a=0
b=0
c=0
while(True):
    d=int(input())
    if(d==4):
        break
    else:
        if (d==1):
            a+=1
        elif (d == 2):
            b+=1
        elif (d==3):
            c+=1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",a)
print("Gasolina:",b)
print("Diesel:",c)