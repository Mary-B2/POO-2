
def mostrar_menu():
    print("\n=== MENÚ DE USUARIO ===")
    print("1. Ingrese nombre")
    print("2. Menú de preguntas")
    print("3. Salir")
    return input("Elija una opción: ").strip()


def saludar(nombre):
    print(f"Bienvenido/a, {nombre}")


def pregunta_1():
    print("\n--- Pregunta 1 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print('socio = {"nombre": "Ana", "saldo": 120}')
    print('print(socio.get("correo", "Sin correo"))')
    print()
    print("Respuesta correcta: Sin correo")

def pregunta_2():
    print("\n--- Pregunta 2 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print("a = [1, 2, 3]")
    print("b = a")
    print("b[0] = 5")
    print("print(a)")
    print()
    print("Respuesta correcta: [5, 2, 3]")
 
 
def pregunta_3():
    print("\n--- Pregunta 3 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print('ciudad = "Paute y"')
    print("print(ciudad[-1].upper())")
    print()
    print("Respuesta correcta: Y")
 
 
def pregunta_4():
    print("\n--- Pregunta 4 ---")
    print("¿Qué ocurre al ejecutar el siguiente código?")
    print()
    print("datos = (10, 20, 30)")
    print("datos[1] = 99")
    print("print(datos)")
    print()
    print("Respuesta correcta: Se produce un TypeError")
 
 
def pregunta_5():
    print("\n--- Pregunta 5 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print('texto = "TEC Azuay"')
    print("print(texto[4:7])")
    print()
    print("Respuesta correcta: Azu")
 
 
def pregunta_6():
    print("\n--- Pregunta 6 ---")
    print("¿Cuántas veces se imprime «*» en el siguiente código?")
    print()
    print("for i in range(3):")
    print("    for j in range(2):")
    print('        print("*", end="")')
    print()
    print("Respuesta correcta: 6")
 
 
def pregunta_7():
    print("\n--- Pregunta 7 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print("for i in range(1, 10, 3):")
    print('    print(i, end=" ")')
    print()
    print("Respuesta correcta: 1 4 7")
 
 
def pregunta_8():
    print("\n--- Pregunta 8 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print("for x in [2, 4, 6]:")
    print("    if x == 7:")
    print('        print("Encontrado")')
    print("        break")
    print("else:")
    print('    print("No encontrado")')
    print()
    print("Respuesta correcta: No encontrado")
 
 
def pregunta_9():
    print("\n--- Pregunta 9 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
    print()
    print("Respuesta correcta: [4, 16]")
 
 
def pregunta_10():
    print("\n--- Pregunta 10 ---")
    print("¿Qué imprime el siguiente código?")
    print()
    print("for i in range(3, 0, -1):")
    print('    print(i, end=" ")')
    print()
    print("Respuesta correcta: 3 2 1")

def pregunta_11():
    print("\n--- Pregunta 11 ---")
    print("Pares e impares")
    print("Pida números enteros con input() hasta que el usuario escriba fin.")
    print("Guárdelos en una lista y, con comprensiones, cree una lista de pares")
    print("y otra de impares. Muestre ambas listas, ordenadas, y la suma de cada una.\n")

    numeros = []
    while True:
        dato = input("Ingrese un número entero (o 'fin'): ").strip()
        if dato.lower() == "fin":
         break
        if dato.lstrip("-").isdigit():
         numeros.append(int(dato))
        else:
            print("Valor no válido. Escriba un número entero o 'fin'.")

    pares = sorted([n for n in numeros if n % 2 == 0])
    impares = sorted([n for n in numeros if n % 2 != 0])

    print("\nPares:", pares, "| Suma:", sum(pares))
    print("Impares:", impares, "| Suma:", sum(impares))

def menu_preguntas():
    while True:
        print("\n=== MENÚ DE PREGUNTAS ===")
        for i in range(1, 12):
            print(f"{i}. Pregunta {i}")
        print("0. Volver al menú principal")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            pregunta_1()
        elif opcion == "2":
            pregunta_2()
        elif opcion == "3":
            pregunta_3()
        elif opcion == "4":
            pregunta_4()
        elif opcion == "5":
            pregunta_5()
        elif opcion == "6":
            pregunta_6()
        elif opcion == "7":
            pregunta_7()
        elif opcion == "8":
            pregunta_8()
        elif opcion == "9":
            pregunta_9()
        elif opcion == "10":
            pregunta_10()
        elif opcion == "11":
            pregunta_11()
        elif opcion == "0":
            break
        else:
            print("Opción no válida.")

def main():
    nombre = ""
    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese su nombre: ").strip()
            saludar(nombre)
        elif opcion == "2":
            if not nombre:
                print("Primero ingrese su nombre (opción 1).")
            else:
                print(f"{nombre}, le vamos a presentar las 11 preguntas.")
                menu_preguntas()
        elif opcion == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida.")


main()