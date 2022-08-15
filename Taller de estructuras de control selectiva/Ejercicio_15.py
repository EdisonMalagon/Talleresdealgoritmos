edad_en_meses = float (input ('Ingresa el valor de edad en meses: '))
nivel_de_hemoglobina = float (input ('Ingresa el valor de nivel de hemoglobina: '))
rango_menor=0
if edad_en_meses<=1:
    rango_menor=13
if edad_en_meses>1 and edad_en_meses<=6:
    rango_menor=10
if edad_en_meses>6 and edad_en_meses<=12:
    rango_menor=11
if edad_en_meses>12 and edad_en_meses<=60:
    rango_menor=11.5
if edad_en_meses>30 and edad_en_meses<=120:
    rango_menor=12.6
if edad_en_meses>120 and edad_en_meses<=180:
    rango_menor=13
if nivel_de_hemoglobina<rango_menor:
    print ('Positivo en anemia')
else:
    print ('Negativo en anemia')
print ('Valor de rango menor: ' + repr (rango_menor))
