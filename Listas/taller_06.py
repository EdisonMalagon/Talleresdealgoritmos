# -*- coding: utf-8 -*-
"""Taller_06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13hBmMpEZ3kKJJbDk_OOOEZnTGR_PpLKZ

<h1 align="center">Taller 06 - Introducción a Listas</h1>

## Ejercicio 01: Crear una lista

Suponga que tenemos los puntos que han hecho en el campeonato de fútbol, cinco equipos colombianos. Escribir un programa que crea una lista, llamada ``puntos_equipos`` que contiene los puntos de junior, panteras, millonarios, nacional y america, en ese orden. Utilice la variables que están en el programa. Luego imprima la lista, usando la función ``print()``.
"""

# Las variables con los puntos de los equipos
junior = 47
panteras = 27
millonarios = 3
nacional = 18
america = 23
# TODO: Crear la lista puntos_equipos
puntos_equipos=[junior,panteras,millonarios,nacional,america]

# TODO: imprimir la lista
print(puntos_equipos)
# Verificación
assert puntos_equipos == [47, 27, 3, 18, 23]
print("Prueba superada 😎")

"""---

## Ejercicio 02: Obtener datos de la lista

Suponga que tenemos la lista con las edades de varios estudiantes. Escriba instrucciones para llevar a cabos las siguientes tareas:

* Imprimir el tamaño o el número de elementos de la lista ``edades``.
* Imprimir el segundo elemento de la lista de ``edades`` (debe ser un 11)
* Obtener e imprimir el último elemento de la lista de ``edades`` (que debe ser un 9). Use un índice negativo.
* Imprimir el elemento que se encuentra en la mitad de la lista (que debe ser un 20).
* Usando múltiples índices, guardar en una variable, llamada ``primeros`` los primeros 6 elementos de la lista de ``edades``. Imprima la variable ``primeros``.
* Usando múltiples índices, guardar en una variable llamada ``ultimos`` los últimos 4 elementos de la lista de ``eddades``. Imprima la varibale ``ultimos``.
"""

# Tenemos la lista de edades
edades = [18, 11, 34, 63, 20, 28, 45, 22, 9]

# TODO: Imprimir el tamaño o el número de elementos de la lista edades.
print(len(edades))

# TODO: Imprimir el segundo elemento de la lista de edades (debe ser un 11)

print(edades[1])
# TODO: Obtener e imprimir el último elemento de la lista de edades (que debe ser un 9). Use un índice negativo.
edad=edades[-1]
print((edad))

# TODO: Imprimir el elemento que se encuentra en la mitad de la lista (que debe ser un 20).
print(edades[len(edades)//2])

# TODO: Usando múltiples índices, guardar en una variable, llamada primeros los primeros 6 elementos de la lista de edades. Imprima la variable primeros.
primeros=edades[0:6]
print(primeros)


# TODO: Usando múltiples índices, guardar en una variable llamada ultimos los últimos 4 elementos de la lista de eddades. Imprima la varibale ultimos.
ultimos=edades[5:9]
print(ultimos)

# TODO: Guardar en otra variable ``primeros2`` otra vez los primeros 6 elementos de la lista ``edades``. Esta vez simplifique la escogencia omitiendo el índice inicial

primeros2=primeros
# TODO: Guardar en otra variable ``ultimos2`` otra vez los últimos 4 elementos de la lista ``edades``. Esta vez simplifique la escogencia omitiendo el índice final
ultimos2=ultimos

"""---

## Ejercicio 03: Manipulando listas

Vamos a realizar el siguiente trabajo para modificar la lista de edades.

* Actualice el valor del último elemento de la lista ``edades``. Ya no queremos que sea un ``9`` sino que sea un 19.
* Modifique el valor del tercer elemento de la lista de ``edades``. Guardar un 24 en esa posición.
* Imprima la lista de edades. Verifique que el tercer elemento sea un 24, y que el último sea un 19.
* Agregue los elementos ``21``, ``32`` y ``16`` al final de la lista ``edades``. Imprima el tamaño de la lista y luego imprima la lista.
* Elimine el primer elemento de la lista, y luego elimine el quinto elemento de la lista de edades. Imprima la lista y el tamaño de la lista también.
"""

# TODO: Actualice el valor del último elemento de la lista edades. Ya no queremos que sea un 9 sino que sea un 19.
edades.append(19)

# TODO: Modifique el valor del tercer elemento de la lista de edades. Guardar un 24 en esa posición.
edades.insert(2,24)

# TODO: Imprima la lista de edades. Verifique que el tercer elemento sea un 24, y que el último sea un 19.
print(edades)

# TODO: Agregue los elementos 21, 32 y 16 al final de la lista edades. Imprima el tamaño de la lista y luego imprima la lista.
edades.extend([21,32,16])
print(len(edades))
print(edades)

# TODO: Elimine el primer elemento de la lista, y luego elimine el quinto elemento de la lista de edades. Imprima la lista y el tamaño de la lista también.
edades.pop(0)
edades.pop(4)
print(len(edades))
print(edades)

"""---

## Ejercicio 04 - Leer una lista de números

Escribir un **programa** en Python que lea la edad de $N$ estudiantes del curso, los almacene en una lista de números y luego imprima la lista
"""

# Programa en Python para leer la edad de varios estudiantes. 
# Vamos a preguntar cuantos estudiantes hay = N.
Numero_estudiantes=int(input("Digite nuemero de estudiantes"))
C=0
Lista=[]
while True:
 if(C==Numero_estudiantes):
   break
 C=C+1
 edad=int(input("Digite edad: "))
 Lista.append(edad)
print(Lista)

"""---

## Ejercicio 05 - Leer una lista de tuplas

Escribir un **Programa** que le pregunte al usuario el nombre de paises y sus capitales, los guarde en un *Par*  o *Tupla*, y luego almacene ese par en una lista. Para finalizar, el nombre del país y el nombre de la capital deben ser vacíos (al tiempo). Imprima la lista una vez finalice la lectura de los datos
"""

# Programa en Python para leer paises y capitales. Vamos a preguntar cuantos paises leer.
Paises_capital=[]
while True:
  pais=input("Digite pais: ")
  capital=input("Digite capital: ")
  if(pais=="" and capital==""):
    break
  tupla=(pais,capital)
  Paises_capital.append(tupla)
  print(Paises_capital)

"""---

## Ejercicio 06 

Escribir un Programa en Python que le pregunte a un usuario el nombre, carrera y promedio en la carrera, de varios estudiantes de la universidad, almacene cada uno de esos tres datos en una tupla, y luego guarde la tupla en una lista. Al final, imprima la lista. Use un while para saber si debemos seguir o no en la lectura de los datos.
"""

# Programa en Python para leer información de varios estudiantes. Use un while para saber si seguimos la lectura o no
lista_1=[]
s=True
while s:
    n=str(input("Ingrese Nombre: "))
    c=input("Ingrese carrera: ")
    p=float(input("Ingrese promedioo: "))
    s=input("Desea continuar? True or False: ")
    tupla_1=(n,c,p)
    lista_1.append(tupla_1)
print(lista_1)

"""---

## Ejercicio 07 - Contar de una lista 

Escriba una **función** en Python que reciba una lista de números ```float``` que representa los promedios de temperatura en Bogotá en los últimos días, y que retorne cuántas de esas temperaturas están entre los 15 y los 20 grados centígrados.
"""

# Función que cuenta en una lista
def contar_temperaturas(temps: [float]) -> int:
    contar=0 
    for i in temps:
        if (i>=15 and i <=20):
            contar=contar+1
    return contar


# Pruebas de la función anterior
assert contar_temperaturas([11, 18, 23.5, 19.5, 6, 16.3, 22.1, 4.6, 18.9, 18.6, 15.1, 16.1, 19.9, 1.5, 12, 21.7]) == 8
print("Prueba superada 💪🏽")

"""---

## Ejercicio 08

Escriba una **función** en Python que reciba una lista de números enteros que representan la edad de los diversos compañeros del curso, y que calcule y retorne cuántos de esos compañeros son menores de edad, es decir, cuántas edades son inferiores a 18 años.
"""

# Función que cuenta los menores de edad en una lista de edades
def ejercicio08(lista_edades:[int]) -> int:
    contar=0
    for i in lista_edades:
      if (i >0 and i<18):
       contar=contar+1
    return contar 

# Pruebas de la función anterior
assert ejercicio08([23, 31, 16, 11, 21, 18, 34, 45, 17, 16, 32, 43, 20, 19, 18, 16, 14, 33]) == 6
print("Prueba superada 💪🏽")

"""---

## Ejercicio 09

SEn Python, resulta que una palabra es una lista de letras. A partir de esto, escriba una **función** en Python que cuente en esa lista de letras cuántas vocales en minúsculas hay en la lista.

"""

# Función que cuenta las vocales en una palabra
def ejercicio09(palabra: str) -> int:
    contar=0
    for i in palabra:
        if(i=="a"):
            contar=contar+1
        elif(i=="e"):
            contar=contar+1
        elif(i=="i"):
            contar=contar+1
        elif(i=="o"):
            contar=contar+1
        elif(i=="u"):
            contar=contar+1
    return contar

# Pruebas de la función anterior
assert (ejercicio09("Lorem ipsum dolor sit Amet, consectetur adipiscing elit")) == 18
assert (ejercicio09("Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis"))== 25
print("Prueba superada 💪🏽")

"""---

## Ejercicio 10

Escriba una función en Python que reciba una lista de números enteros positivos, y que retorne cuántos de los números de la lista son múltiplos de 2, 3 y 5 al mismo tiempo.
"""

# Función que cuenta los múltiplos
def ejercicio10(numeros: [int]) -> int:
    contar=0
    for i in numeros:
         if (i % 2==0 and i%3==0 and i%5==0):
             contar=contar+1
    return contar

# Pruebas para la función anterior
assert (ejercicio10([5, 10, 30, 25, 24, 60, 12, 100, 120, 15, 90, 95, 36, 35, 72, 180])) == 5
print("Prueba superada 💪🏽")

"""---

## Ejercicio 11 - Múltiples contadores

Escriba una función en Python que reciba una lista con los nombre de los perros de mis vecinos, y que retorne cuántos perros de la lista se llaman ```"fifi"``` y cuantos se llaman ```"mateo"```. **OJO: Son dos contadores diferentes**.
"""

# Función que cuenta el número de perros
def ejercicio11(perros: [str]) -> (int, int):
    f=0
    m=0
    for i in perros:
        if i=="fifi":
            f=f+1
        elif i=="mateo":
            m=m+1
    return f,m

# Prueba de la función anterior
assert (ejercicio11(["lila", "firulais", "romeo", "fifi", "neron", "milagro", "fifi", "lila", "cariño", "rosa", "fifi", "mateo", "rex"])) == (3,1)
print("Prueba superada 💪🏽")

"""---

## Ejercicio 12 - Contar en listas de tuplas

En una tupla de dos elementos hemos almacenado el resultado de cada uno de los partidos que ha jugado el Junior de Barranquilla. El primer elemento es la cantidad de goles que hizo el equipo en el partido, y el segundo elemento corresponde a los goles que le hicieron al equipo en el partido. Escriba una función que reciba esta lista de tuplas con los resultados de los partidos, y que retorne cuántos partidos ganó en total, cuántos empató y cuántos perdió.
"""

# Función para contar partidos
def resultados_partidos(partidos:[(int, int)]) -> (int, int, int):
    gano=0
    empato=0
    perdio=0
    for x,y in partidos:
      if(x==y):
        empato+=1
      if(x>y):
        gano+=1
      if(x<y):
        perdio+=1
    return gano,empato,perdio
    

# prueba de la función anterior
assert (resultados_partidos([(1, 3), (0, 0), (4, 0), (5, 3), (2, 2), (4, 3), (1, 0), (1, 2), (0, 0), (3, 2), (3, 1), (7, 0), (0, 2), (3, 3), (4, 2), (3, 4)])) == (8, 4, 4)
print("Prueba superada 💪🏽")

"""---

# Ejercicio 13

La información de los salarios de una empresa se almacena en una tupla de 3 elementos, de la siguiente manera:

* El primer elemento es el cargo del empleado
* El segundo elemento de la tupla es la edad del empleado
* El tercer elemento de la tupla es el sueldo del empleado

Escriba una función en Python que reciba esta lista de tuplas con la información de los empleados, y que retorne cuántos empleados que tienen un cargo de gerente o contador, tienen entre 45 y 50 años, pero ganan menos de dos millones de pesos.
"""

# Función para resolver el ejercicio 13
def ejercicio13(empleados: [(str, int, float)]) -> int:
    k=0

    for c,e,s in empleados:
      if(c=="gerente" or c=="contador" and e>=45 and e<=50 and s<2000000):
        k=k+1
    return k





# Pruebas de la función anterior
assert (ejercicio13([("director", 38, 1500000), ("gerente", 47, 1_450_000), ("celador", 63, 700_000), ("director", 29, 2_700_000),
                    ("contador", 51, 1_900_000), ("contador", 49, 1_900_000), ("analista", 23, 11_200_000), ("gerente", 46, 1_200_000),
                    ("contador", 39, 2_100_000), ("profesional", 36, 2_100_000), ("gerente", 45, 1_050_000), ("contador", 46, 800_000)])) == 5
print("Prueba superada 💪🏽")

"""---

# Ejercicio 14

Un estudiante registra toda su historia académica en una lista de tuplas con la siguiente conformación:

* El primer elemento es el nombre de la unidad de estudio
* El segundo elemento es número de créditos de la unidad de estudio
* El tercer elemento es el semestre al que pertenece esa unidad de estudio
* El cuarto y quinto elemento son las notas del primer corte y segundo corte de la unidad de estudios

Sabiendo que para obtener la nota final de una unidad de estudios debemos tener en cuenta que el primer corte pesa el 40% de la nota final, y el segundo corte pesa el 60% de la nota, escriba una función que reciba esta lista con las notas del estudiante y que retorne cuántas unidades de estudio perdió el estudiante.
"""

# Función para resolver el Ejercicio 14: Completar los datos de entrada
def ejercicio14(materias:[(str,int,int,int)]) -> int:
    k=0
    for n,u,s,n1,n2 in materias:
      if ((n1*.4+n2*.6)<60):
        k=k+1
    return k
# Pruebas para la función anterior
assert (ejercicio14([("calculo", 6, 1, 45, 67), ("frances", 3, 2, 77, 89), ("calculo", 6, 1, 72, 58), ("ecuaciones", 3, 4, 68, 61),
                    ("ingles basico", 3, 2, 79, 85), ("quimica", 4, 1, 88, 92), ("fisica", 3, 2, 56,61), ("procesos", 3, 4, 75, 77),
                    ("cultura", 2, 3, 33, 21), ("deportes", 2, 1, 98, 90), ("cocina", 3, 4, 79, 98), ("estadistica", 3, 4, 53, 10)])) == 4

print("Prueba superada 💪🏽")

"""---

# Ejercicio 15

La información sobre todos los contagiados de Coronavirus son almacenados en una tupla con la siguiente coformación:

* El primer elemento de la tupla es el género del contagiado ('M' = masculino, y 'F' = femenino)
* El segundo elemento es la edad del contagiado
* El tercer elemento de la tupla es cuantos días lleva contagiado
* El cuarto elemento es si el contagiado falleció o no (True == si falleció, False == no falleció)

Escriba una función en Python que reciba una lista con estas tuplas que representan la información de los contagiados y que retorne cuántas mujeres mayores de 60 años han fallecido y cuántos menores de edad tienen más de una semana de haber sido contagiados.
"""

# Función para resolver el Ejercicio 15
def ejercicio15(contagiados: [(str,int ,int ,int ,int)]) -> int:
    c1=0
    c2=0
    for g,e,d,f in contagiados:
        if (g=="F" and e>60 and f==True):
            c1 += 1
        if e<18 and d>7:
            c2 += 1
    return c1,c2

# Pruebas de la función anterior
assert (ejercicio15([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True)])) == (4, 3)
print("Prueba superada 💪🏽")

"""---

# Ejercicio 16

Seguimos trabajando con la lista de contagiados presentada anteriormente. Escriba una función que permita saber cuantos fallecido hay de cada género, es decir, cuántas mujeres han fallecido y cuántos hombres han fallecido.
"""

# Función para resolver el ejercicio 16
def ejercicio16(contagiados: [(str,int ,int ,str ,str)]) -> (int, int):
   n=0
   m=0
   for r,e,d,f in contagiados:
     if r=='F' and f==True:
            n=n+1
     if r=='M' and f==True:
            m=m+1
   return n,m

# Pruebas de la función anterior
assert (ejercicio16([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True), ('F', 72, 6, True)])) == (5, 3)
print("Prueba superada 💪🏽")

"""---

## Ejercicio 17

Seguimos trabajando con la lista de contagiados. Ahora queremos saber cuántas personas que no han fallecido tienen entre 20 y 30 años de edad.
"""

# Función para resolver el ejercicio 17
def ejercicio17(contagiados: [(int,int ,int ,int ,int)]) -> int:
  n=0
  for g,e,d,f in contagiados:
    if f==False and e>=20 and e<=30:
      n=n+1
  return n

    

# Pruebas de la función anterior
assert (ejercicio17([('M', 23, 12, False), ('M', 45, 3, False), ('M', 72, 6, True), ('F', 81, 11, True), ('M', 11, 12, False), ('M', 17, 8, True),
                   ('F', 77, 3, True), ('M', 67, 4, False), ('F', 61, 5, True), ('M', 14, 28, False), ('M', 44, 11, True), ('M', 6, 3, False),
                    ('M', 28, 19, False), ('F', 91, 10, True), ('F', 72, 6, True), ('F', 26, 5, False)])) == 3
print("Prueba superada 💪🏽")