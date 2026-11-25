class ControladorObra:
    def __init__(self, modelo, vista):
        self.modelo=modelo
        self.vista=vista
    def ejecutar(self):
        opcion=" "
        while opcion!="4":
            opcion = self.vista.menu()
            if opcion == "1":
                try:
                    titulo, precio, butacas= self.vista.solicitar_datos()
                    mensaje = self.modelo.registrar_obra(titulo,precio,butacas)
                    self.vista.mostrar_mensaje(mensaje)
                except ValueError:
                    self.vista.error("Datos ingresados incorrectos")

            elif opcion == "2":
                try:
                    self.vista.mostrar_obras(self.modelo.mostrar_lista())
                except ValueError:
                    self.vista.error("Lista vacia")

            elif opcion == "3":
                try:
                    codigo, cantidad = self.vista.solicitar_venta()
                    resultado = self.modelo.vender_obra(codigo, cantidad)
                    if resultado:
                        self.vista.mostrar_mensaje("Operacion realizada correctamente")
                    else:
                        self.vista.mostrar_mensaje("No hay butacas disponibles")
                except ValueError:
                    self.vista.error("Datos ingresados incorrectos")

            elif opcion == "4":
                self.vista.mostrar_mensaje("Gracias por utilizar el sistema")