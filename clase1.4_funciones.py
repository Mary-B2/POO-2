#declaraciones de funciones
def saludar():
    print("Hola Maria")
saludar()

#funcion con parametro
#def calcular_edad(anio_nacimiento, anio_actual):
#    print("La edad es:", anio_actual- anio_nacimiento)

#a = int(input("Ingrese su año de nacimiento: "))
#b = int(input("Ingrese el año actual: "))
#calcular_edad(a,b)

#funciones con retorno
def calcular_iva(precio, iva):
    return precio*iva
resultado=calcular_iva(10, 0.15)
print("El iva es: ", resultado)

#funciones con valores por defecto
def calcular_iva(precio, iva=0.15):
    return precio*iva
resultado=calcular_iva(100)
print("El iva es: ", resultado)

resultado=calcular_iva(100, 0.14)
print("El iva es: ", resultado)

#funciones con listas
def calcular_par(numeros):
    for e in numeros:
        if e%2==0:
            print("El numero", e, "Es par")
        else:
            print("El numero", e, "es impar")
lista_numeros = range(0,1000,2)
calcular_par(lista_numeros)

lista_numeros= range(5,0,-1)
for e in lista_numeros:
    print(e, end=" ")

#funciones con tuplas
def suma_numeros(*a):
    return sum(a)
print("la suma es: ",suma_numeros(1,2,3))

#funciones con diccionarios
def estudiantes(**lista_estudiantes):
    suma_total=0
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante", nombre, "tiene", edad, "años")
        suma_total += edad
    print("La suma total es: ", suma_total)

estudiantes(Veronica=20, Juan=25, Maria=30, daniela=20, Pablo=21, Domenica=20, Karen=20)

***
ejercicio clase 1.4
Menu de usuario
1. Ingrese nombre: Mensaje de bienvenida
2. Menu de preguntas: le vam a presentar las 11 preguntas Pregunta 1: Listas Pregunta 2: Diccionario
3. Salir

***
