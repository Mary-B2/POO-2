class Obra:
    def __init__ (self, codigo, titulo, precio, butacas):
        self.codigo=codigo
        self.titulo=titulo
        self.precio=precio
        self.butacas=butacas
        
    def vender_entradas(self, cantidad):
            if cantidad <=0:
                print("Error la cantidad debe ser mayor a 0")
                return False
            elif cantidad > self.butacas:
                print(f"Error: solo hay {self.butacas} butacas")
                return False
            else: 
                self.butacas -= cantidad
                return True
    def __str__(self):
            return f"Codigo: {self.codigo:<10} Titulo: {self.titulo:<30} Precio: {self.precio:<10.2f} Butacas: {self.butacas}"

class ListaObra:
    def __init__(self):
        self.listaObra=[]
        self.cargar_datos()

    def cargar_datos(self):
        lista=[
            Obra(1, "Hamlet", 10.00, 120),
            Obra(2, "La casa de Bernarda", 8.00, 90)
        ]
        for o in lista:
            self.listaObra.append(o)

    def registrar_obra(self,codigo,titulo,precio,butacas):
        self.listaObra.append(Obra(codigo,titulo,precio,butacas))
        return print("Obra registrada correctamente")

    def vender_obra(self,codigo, cantidad):
        for obra in self.listaObra:
            if obra.codigo == codigo:
                return obra.vender_entradas(cantidad)
        return False

    def mostrar_lista(self):
        return self.listaObra