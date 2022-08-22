can_est=int(input("Cantidad de estudiantes: "))
promfmax=0
sumapromf=0
epfin=0
epfsp=0
estpromfmax=" "
estpromfmin=" "
promfmin=0
for i in range (1,can_est+1):
    n_est=input("Nombre del estudiante: ")
    pun_fi=float(input("Puntaje final: "))
    sumapromf=pun_fi+sumapromf
    if(promfmax<=pun_fi):
        promfmax=pun_fi
        estpromfmax=n_est
    if(promfmax>pun_fi):
        promfmin=pun_fi
        estpromfmin=n_est
print("Estudiante con mayor puntaje final:",estpromfmax)
print("Estudiante con menor puntaje final:",estpromfmin)
print("Máximo puntaje obtenido:",promfmax)
print("Mínimo puntaje obtenido:",promfmin)
print("Promedio puntajes:",round(sumapromf/can_est,2))