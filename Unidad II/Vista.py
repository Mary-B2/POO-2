class VistaObra:
    def menu(self):
        print("\n===== TEATRO SUCRE =====")
        print("1. Registrar obra")
        print("2. Mostrar obras")
        print("3. Vender entradas")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")
        return opcion
    
    def solicitar_datos(self):
        titulo=input("Nombre de la obra: ")
        precio = float(input("Precio de la obra: "))
        butacas = int(input("Cantidad de butacas: "))
        return titulo, precio, butacas

    def solicitar_venta(self):
        codigo = int(input("Código de la obra: ").strip())
        cantidad = int(input("Cantidad de butacas: ").strip())
        return codigo, cantidad
    
    def mostrar_obras(self, obras):
        if not obras:
            print("No hay obras registradas")
        else:
            for obra in obras:
                print(obra)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
        
    