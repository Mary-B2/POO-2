#Trabajo Grupal 
#Trabajo Grupal de Pooll
#Diana Tigre, Maria Bravo, Daniela Corte, Steven Ortiz, Pablo Alvarado

libro_iniciales = [
{"Codigo": 1, "Titulo": "Cine años de soledad", "Autor": "Gabriel Garcia Marquez", "Estado": "Disponible" },
{"Codigo": 2, "Titulo": "Don Quijote de la mancha", "Autor": "Miguel de Cervantes", "Estado": "Disponible" },
{"Codigo": 3, "Titulo": "Orgullo y Prejuicio", "Autor": "Jane Austen", "Estado": "Disponible" },
{"Codigo": 4, "Titulo": "El Señor de los Anillos", "Autor": "J.R.R. Tolien", "Estado": "Disponible" },
{"Codigo": 5, "Titulo": "La Divina Comedia", "Autor": "Dante Alighieri", "Estado": "Disponible" } 
] 

try:
    with open("Libros.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    contenido = ""

if contenido.strip() == "":

    with open("Libros.txt", "w", encoding="utf-8") as archivo:
        for libro in libro_iniciales:
            archivo.write(
                f"{libro['Codigo']},{libro['Titulo']},"
                f"{libro['Autor']},{libro['Estado']}\n"
            )

try:
    with open("Prestamos.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()

except FileNotFoundError:

    with open("Prestamos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("")


def leer_entero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print("Error, debe ingresar un numero entero")
        return None

def buscar_por_codigo(libros, codigo):
    for libro in libros:
        if libro["Codigo"] == codigo:
            return libro
    return None

def cargar_libros():
    libros = []
    try:
        with open("Libros.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() == "":
                    continue
                datos = linea.strip().split(",")
                libros.append({"Codigo": int(datos[0]), "Titulo": datos[1], "Autor": datos[2], "Estado": datos[3]})
    except FileNotFoundError:
        pass
    return libros

def cargar_prestamos():
    prestamos = []
    try:
        with open("Prestamos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if linea.strip() == "":
                    continue
                datos = linea.strip().split(",")
                prestamos.append({"Numero": int(datos[0]), "Codigo": int(datos[1]), "Estudiante": datos[2], "Fecha": datos[3], "Estado": datos[4]})
    except FileNotFoundError:
        pass
    return prestamos

def guardar_libros(libros):
    with open("Libros.txt", "w", encoding="utf-8") as archivo:
        for l in libros:
            archivo.write(f"{l['Codigo']},{l['Titulo']},{l['Autor']},{l['Estado']}\n")

def guardar_prestamos(prestamos):
    with open("Prestamos.txt", "w", encoding="utf-8") as archivo:
        for p in prestamos:
            archivo.write(f"{p['Numero']},{p['Codigo']},{p['Estudiante']},{p['Fecha']},{p['Estado']}\n")


def registrar_libros ():

    titulo = input("Ingrese el titulo del libro: ")
    autor = input ("Ingrese el autor del libro: ")

    if titulo == "" or autor == "":
        print ("No se aceptas campos vacios")

    else :

        codigo = 1

        with open("Libros.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                codigo = int(datos[0]) + 1

        with open ("Libros.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{codigo},{titulo},{autor},Disponible\n")

        print ("Libro registrado correctamente")

def mostrar_libros():

    with open ("Libros.txt", "r", encoding="utf-8") as archivo:

        print("========== LISTA DE LIBROS ===========")

        for linea in archivo:
            datos = linea.strip().split(",")
            print("Codigo:", datos[0])
            print("Titulo:", datos[1])
            print("Autor:", datos[2])
            print("Estado:", datos[3])
            print("======================================")

def buscar_libro(libros):
    palabra = input("Ingrese la palabra a buscar: ").strip()
    if palabra == "":
        print("Error: no se acepta un texto vacio")
        return 0

    encontrados = 0
    print("\n========== RESULTADO DE BUSQUEDA ===========")
    print(f"{'Codigo':<8}{'Titulo':<30}{'Autor':<25}{'Estado':<12}")
    print("-" * 75)
    for l in libros:
        if palabra.lower() in l["Titulo"].lower():
            print(f"{l['Codigo']:<8}{l['Titulo']:<30}{l['Autor']:<25}{l['Estado']:<12}")
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron libros con esa palabra")
    return encontrados

def prestar_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    if codigo is None:
        return False

    libro = buscar_por_codigo(libros, codigo)
    if libro is None:
        print("Error: el codigo del libro no existe")
        return False
    if libro["Estado"] != "Disponible":
        print("Error: el libro ya esta prestado")
        return False

    estudiante = input("Ingrese el nombre del estudiante: ").strip()
    if estudiante == "":
        print("Error: el nombre no puede estar vacio")
        return False

    fecha = input("Ingrese la fecha del prestamo (AAAA-MM-DD): ").strip()
    if fecha == "":
        print("Error: la fecha no puede estar vacia")
        return False

    if len(prestamos) > 0:
        numero = prestamos[-1]["Numero"] + 1
    else:
        numero = 1

    prestamos.append({"Numero": numero, "Codigo": codigo, "Estudiante": estudiante, "Fecha": fecha, "Estado": "Activo"})
    libro["Estado"] = "Prestado"
    print("Libro prestado correctamente")
    return True

def devolver_libro(libros, prestamos):
    codigo = leer_entero("Ingrese el codigo del libro: ")
    if codigo is None:
        return False

    libro = buscar_por_codigo(libros, codigo)
    if libro is None:
        print("Error: el codigo del libro no existe")
        return False
    if libro["Estado"] != "Prestado":
        print("Error: el libro no esta prestado")
        return False

    for p in prestamos:
        if p["Codigo"] == codigo and p["Estado"] == "Activo":
            p["Estado"] = "Devuelto"
            break
    libro["Estado"] = "Disponible"
    print("Libro devuelto correctamente")
    return True

def mostrar_prestamos(prestamos, libros):
    print("\n========== LISTA DE PRESTAMOS ===========")
    print(f"{'N°':<5}{'Libro':<30}{'Estudiante':<22}{'Fecha':<13}{'Estado':<10}")
    print("-" * 80)
    for p in prestamos:
        libro = buscar_por_codigo(libros, p["Codigo"])
        titulo = libro["Titulo"] if libro else "(desconocido)"
        print(f"{p['Numero']:<5}{titulo:<30}{p['Estudiante']:<22}{p['Fecha']:<13}{p['Estado']:<10}")
    if len(prestamos) == 0:
        print("No hay prestamos registrados")
    return len(prestamos)

def reporte_general(libros, prestamos):
    total = len(libros)
    disponibles = sum(1 for l in libros if l["Estado"] == "Disponible")
    prestados = sum(1 for l in libros if l["Estado"] == "Prestado")
    activos = sum(1 for p in prestamos if p["Estado"] == "Activo")

    if total > 0:
        porcentaje = (prestados / total) * 100
    else:
        porcentaje = 0

    print("\n========== REPORTE GENERAL ==========")
    print(f"Total de libros:        {total}")
    print(f"Libros disponibles:     {disponibles}")
    print(f"Libros prestados:       {prestados}")
    print(f"Prestamos activos:      {activos}")
    print(f"Porcentaje prestados:   {porcentaje:.2f}%")
    return porcentaje


opcion = 0

while opcion != 8:

    print("======================================")
    print("   BIBLIOTECA DIGITAL DEL TEC AZUAY   ")
    print("======================================")
    print("1. Registrar Libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar prestamos")
    print("7. Reporte general")
    print("8. Salir")

    opcion = leer_entero("Ingrese una opcion a elegir: ")

    if opcion == 1:
        registrar_libros()

    elif opcion == 2:
        mostrar_libros()

    elif opcion == 3:
        buscar_libro(cargar_libros())

    elif opcion == 4:
        libros = cargar_libros()
        prestamos = cargar_prestamos()
        if prestar_libro(libros, prestamos):
            guardar_libros(libros)
            guardar_prestamos(prestamos)

    elif opcion == 5:
        libros = cargar_libros()
        prestamos = cargar_prestamos()
        if devolver_libro(libros, prestamos):
            guardar_libros(libros)
            guardar_prestamos(prestamos)

    elif opcion == 6:
        mostrar_prestamos(cargar_prestamos(), cargar_libros())

    elif opcion == 7:
        reporte_general(cargar_libros(), cargar_prestamos())

    elif opcion == 8:
        print("Gracias por utilizar la biblioteca")

    elif opcion is not None:
        print("Debe de ingresar un numero valido entre 1 al 8")