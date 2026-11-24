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
        obra=input("Nombre de la obra: ")
        precio = float(input("Precio de la obra: "))
        butacas = int(input("Cantidad de butacas: "))
        return obra, precio, butacas
    
    def mostrar_obras(self, obras):
        print("\n============Lista de Obras=================================")
        print("--Codigo----Titulo-------------------------Precio-----Butacas--")
        for obra in obras:
            print(obra)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
        
    def mostrar_resultado(self, resultado):
        if resultado:
            print("Operación realizada correctamente.")
        else:
            print("No se pudo realizar la operación.")