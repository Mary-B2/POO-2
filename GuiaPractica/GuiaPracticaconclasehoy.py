#Trabajo Grupal de Pooll
#Diana Tigre, Maria Bravo, Daniela Corte, Steven Ortiz, Pablo Alvarado

from datetime import date

ARCHIVO_LIBROS = "libros.txt"
ARCHIVO_PRESTAMOS = "prestamos.txt"


class Libro:
    def __init__(self, codigo, titulo, autor, estado="Disponible"):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def prestar(self):
        if self.estado != "Disponible":
            return False
        self.estado = "Prestado"
        return True

    def devolver(self):
        if self.estado != "Prestado":
            return False
        self.estado = "Disponible"
        return True

    def __str__(self):
        return f"{self.codigo:<8}{self.titulo:<30}{self.autor:<25}{self.estado:<12}"


class Prestamo:
    def __init__(self, numero, codigo, estudiante, fecha, estado="Activo"):
        self.numero = numero
        self.codigo = codigo
        self.estudiante = estudiante
        self.fecha = fecha
        self.estado = estado

    def devolver(self):
        self.estado = "Devuelto"


class Biblioteca:
    def __init__(self):
        self.libros = self.cargar_libros()
        self.prestamos = self.cargar_prestamos()

    def guardar_libros(self):
        with open(ARCHIVO_LIBROS, "w", encoding="utf-8") as archivo:
            for l in self.libros:
                archivo.write(f"{l.codigo},{l.titulo},{l.autor},{l.estado}\n")

    def guardar_prestamos(self):
        with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as archivo:
            for p in self.prestamos:
                archivo.write(f"{p.numero},{p.codigo},{p.estudiante},{p.fecha},{p.estado}\n")

    def cargar_libros(self):
        libros = []
        try:
            with open(ARCHIVO_LIBROS, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip() == "":
                        continue
                    datos = linea.strip().split(",")
                    libros.append(Libro(int(datos[0]), datos[1], datos[2], datos[3]))
        except FileNotFoundError:
            print("No se encontro libros.txt: se usan los libros iniciales.")
            libros = [
                Libro(1, "Python para todos", "Charles Severance"),
                Libro(2, "Aprende Java", "Ana Torres"),
                Libro(3, "Bases de datos", "Carlos Mora")
            ]
            self.libros = libros
            self.guardar_libros()
        except (ValueError, IndexError):
            print("Error: el archivo libros.txt tiene datos incorrectos")
        return libros

    def cargar_prestamos(self):
        prestamos = []
        try:
            with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip() == "":
                        continue
                    datos = linea.strip().split(",")
                    prestamos.append(Prestamo(int(datos[0]), int(datos[1]), datos[2], datos[3], datos[4]))
        except FileNotFoundError:
            pass
        except (ValueError, IndexError):
            print("Error: el archivo prestamos.txt tiene datos incorrectos")
        return prestamos

    def buscar_por_codigo(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def registrar_libro(self):
        titulo = leer_texto("Ingrese el titulo del libro: ")
        autor = leer_texto("Ingrese el autor del libro: ")

        if len(self.libros) > 0:
            codigo = max(l.codigo for l in self.libros) + 1
        else:
            codigo = 1

        libro = Libro(codigo, titulo, autor)
        self.libros.append(libro)
        self.guardar_libros()
        print("Libro registrado correctamente")
        return libro

    def mostrar_libros(self):
        print("\n========== LISTA DE LIBROS ===========")
        print(f"{'Codigo':<8}{'Titulo':<30}{'Autor':<25}{'Estado':<12}")
        print("-" * 75)
        for libro in self.libros:
            print(libro)
        if len(self.libros) == 0:
            print("No hay libros registrados")
        return len(self.libros)

    def buscar_libro(self):
        palabra = input("Ingrese la palabra a buscar: ").strip()
        if palabra == "":
            print("Error: no se acepta un texto vacio")
            return 0

        encontrados = 0
        print("\n========== RESULTADO DE BUSQUEDA ===========")
        print(f"{'Codigo':<8}{'Titulo':<30}{'Autor':<25}{'Estado':<12}")
        print("-" * 75)
        for l in self.libros:
            if palabra.lower() in l.titulo.lower():
                print(l)
                encontrados += 1
        if encontrados == 0:
            print("No se encontraron libros con esa palabra")
        return encontrados

    def prestar_libro(self):
        codigo = leer_entero("Ingrese el codigo del libro: ")
        libro = self.buscar_por_codigo(codigo)
        if libro is None:
            print("Error: el codigo del libro no existe")
            return False
        if not libro.prestar():
            print("Error: el libro ya esta prestado")
            return False

        estudiante = leer_texto("Ingrese el nombre del estudiante: ")
        fecha = str(date.today())

        if len(self.prestamos) > 0:
            numero = self.prestamos[-1].numero + 1
        else:
            numero = 1

        self.prestamos.append(Prestamo(numero, codigo, estudiante, fecha))
        self.guardar_libros()
        self.guardar_prestamos()
        print("Libro prestado correctamente")
        return True

    def devolver_libro(self):
        codigo = leer_entero("Ingrese el codigo del libro: ")
        libro = self.buscar_por_codigo(codigo)
        if libro is None:
            print("Error: el codigo del libro no existe")
            return False
        if not libro.devolver():
            print("Error: el libro no esta prestado")
            return False

        for p in self.prestamos:
            if p.codigo == codigo and p.estado == "Activo":
                p.devolver()
                break
        self.guardar_libros()
        self.guardar_prestamos()
        print("Libro devuelto correctamente")
        return True

    def mostrar_prestamos(self):
        print("\n========== LISTA DE PRESTAMOS ===========")
        print(f"{'N°':<5}{'Libro':<30}{'Estudiante':<22}{'Fecha':<13}{'Estado':<10}")
        print("-" * 80)
        for p in self.prestamos:
            libro = self.buscar_por_codigo(p.codigo)
            titulo = libro.titulo if libro else "(desconocido)"
            print(f"{p.numero:<5}{titulo:<30}{p.estudiante:<22}{p.fecha:<13}{p.estado:<10}")
        if len(self.prestamos) == 0:
            print("No hay prestamos registrados")
        return len(self.prestamos)

    def reporte_general(self):
        total = len(self.libros)
        disponibles = sum(1 for l in self.libros if l.estado == "Disponible")
        prestados = sum(1 for l in self.libros if l.estado == "Prestado")
        activos = sum(1 for p in self.prestamos if p.estado == "Activo")

        try:
            porcentaje = (prestados / total) * 100
        except ZeroDivisionError:
            porcentaje = 0

        print("\n========== REPORTE GENERAL ==========")
        print(f"Total de libros:        {total}")
        print(f"Libros disponibles:     {disponibles}")
        print(f"Libros prestados:       {prestados}")
        print(f"Prestamos registrados:  {len(self.prestamos)}")
        print(f"Prestamos activos:      {activos}")
        print(f"Porcentaje prestados:   {porcentaje:.2f}%")
        return porcentaje


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error, debe ingresar un numero entero")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error, no se aceptan campos vacios")
        elif "," in texto:
            print("Error, no se permiten comas")
        else:
            return texto


def main():
    biblioteca = Biblioteca()
    biblioteca.guardar_prestamos()
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
            biblioteca.registrar_libro()

        elif opcion == 2:
            biblioteca.mostrar_libros()

        elif opcion == 3:
            biblioteca.buscar_libro()

        elif opcion == 4:
            biblioteca.prestar_libro()

        elif opcion == 5:
            biblioteca.devolver_libro()

        elif opcion == 6:
            biblioteca.mostrar_prestamos()

        elif opcion == 7:
            biblioteca.reporte_general()

        elif opcion == 8:
            biblioteca.guardar_libros()
            biblioteca.guardar_prestamos()
            print("Datos guardados. Gracias por utilizar la biblioteca")

        else:
            print("Debe de ingresar un numero valido entre 1 al 8")


main()