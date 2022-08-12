""""
Temperatura en grados Farenheit-->float-->t
Salidas
Deporte-->str-->d
"""
t=float(input("Digite la temperatura: "))
d=""
if(t>85 and t<=120):
    d="Natación"
elif(t>70 and t<=85):
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esqui"
elif(t>=0 and t<=10):
    d="Marcha"            
else:
    d="La temperatura no pertenece a ningún deporte"
print("El deporte a practicar es: ",d)