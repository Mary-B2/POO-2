class VistaPrestamo:
    def menu(self):
        print("\n" + "-" * 10, "MENÚ DE USUARIO", "-" * 10)
        print("1. Registrar equipo")
        print("2. Mostrar equipos")
        print("3. Prestar equipo")
        print("4. Buscar por nombre")
        print("5. Devolver")
        print("6. Mostrar prestamos")
        print("7. Reporte General")
        print("8. Salir (guarda los archivos)")
        opcion = int(input("Ingrese una opción: "))
        return opcion