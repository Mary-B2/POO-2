from modelo import*
from Vista import VistaObra
from controlador import ControladorObra

modelo = ListaObra()
vista = VistaObra()
controlador = ControladorObra(modelo, vista)
controlador.ejecutar()