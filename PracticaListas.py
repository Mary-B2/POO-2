notas=[10,8,9,5]
print(notas)
notas.append(20)
notas.insert(1,10)
print(notas)
print (len(notas))
print(notas[-1])
print(sum(notas))
print(notas[0])
print(min(notas))
print(max(notas))
notas.remove(9)
print(notas)
print(sorted(notas))
print(notas[2:4])
print(notas[:2])
print(notas[::-1])

#Tuplas#
meses=("Enero","Febrero","Marzo","Abril","Mayo", "Junio", "Julio","Agosto", "Septiembre","Octubre","Noviembre","Diciembre")
print(meses[0])
print(meses[-1])
#meses[3]="otro valor"

#diccionario
estudiante={"Cedula": "0107009508",
            "Nombre": "Maria Bravo",
            "Correo": "maria.bravo9837@gmail.com",
            "Celular": "0997544690",
            "Notas": [10,8,8.4,7.2]
            }
print(estudiante["Nombre"])
print(estudiante.get("Nombre"))
print(estudiante.keys( ))

#conjuntos
conjunto_a={1,1,5,4,6,8}
conjunto_b={1,9,6,5,4}
print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

