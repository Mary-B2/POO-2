
#1¿Qué imprime el siguiente código?
socio = {"nombre": "Ana", "saldo": 120}
print(socio.get("correo", "Sin correo"))

#respuesta: Sin correo

#2¿Qué imprime el siguiente código?
a = [1, 2, 3]
b = a
b[0] = 5
print(a)
#Respuesta: [5,2,3]

#3.¿Qué imprime el siguiente código?
ciudad = "Paute y"
print(ciudad[-1].upper())
#Respuesta: Y

#4.¿Qué ocurre al ejecutar el siguiente código?
#datos = (10, 20, 30)
#datos[1] = 99
#print(datos)
#Respuesta: TypeError

#5.¿Qué imprime el siguiente código?
texto = "TEC Azuay"
print(texto[4:7])
#Respuesta: Azu

#6.¿Cuantas veces imprime "*" en el siguiente código?
for i in range(3):
    for j in range(2):
        print("*", end="")
        print()
#Respuesta: 6

#7.¿Qué imprime el siguiente código?
for i in range(1, 10, 3):
    print(i, end=" ")
    print()
#Respuesta: 1, 4, 7

#8.¿Qué imprime el siguiente código?
for x in [2, 4, 6]:
    if x == 7:
        print("Encontrado")
        break
else:
    print("No encontrado")
#Respuesta: No encontrado

#9.¿Qué imprime el siguiente código?
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])
#Respuesta: [4, 16]

#10.¿Qué imprime el siguiente código?
for i in range(3, 0, -1):
    print(i, end=" ")
    print()
#Respuesta: 3,2,1

#Pida números enteros con input() hasta que el usuario escriba fin. 
#Guárdelos en una lista y luego, con comprensiones, cree una lista de pares y otra de impares. 
#Muestre ambas listas, ordenadas, y la suma de cada una.

numeros = []   
while True:
  dato = input("Ingrese numeros enteros (o 'fin'): ").strip()
  if dato.lower() == "fin":    
      break
  if dato.lstrip("-").isdigit():
      numeros.append(int(dato))
  else:
      print("Valor no valido, escriba un numero entero o 'fin' ")

pares = sorted([n for n in numeros if n % 2 == 0])
impares = sorted([n for n in numeros if n % 2 != 0])

print("\nPares:", pares, "| Suma:", sum(pares))
print("Impares:", impares, "| Suma:", sum(impares))

# Respuesta:
# Ingrese numeros enteros (o 'fin'): 5
# Ingrese numeros enteros (o 'fin'): 2
# Ingrese numeros enteros (o 'fin'): 9
# Ingrese numeros enteros (o 'fin'): 18
# Ingrese numeros enteros (o 'fin'): 14
# Ingrese numeros enteros (o 'fin'): 17
# Ingrese numeros enteros (o 'fin'): fin

# Pares: [2, 14, 18] | Suma: 34
# Impares: [5, 9, 17] | Suma: 31