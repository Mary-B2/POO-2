class Obra:
    
    def __init__ (self,codigo,titulo,precio,butacas):
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
        return f"{self.codigo:<10}{self.titulo:<30} ${self.precio:<10.2f}{self.butacas}"

obras = [
    Obra(1, "Hamlet", 10.00, 120),
    Obra(2, "La casa de Bernarda", 8.00, 90)
]

def registrar_obra():
    titulo = input("Ingrese el titulo de la obra: ")
    precio = float(input("Ingrese el precio: "))
    butacas = int(input("Ingrese la cantidad de butacas: "))

    codigo = len(obras) + 1

    nueva_obra = Obra(codigo, titulo, precio, butacas)

    obras.append(nueva_obra)

    print(f"Registrado con el codigo {codigo}.")

def mostrar_obras():
    print("\nCodigo----Titulo-------------------------Precio-----Butacas")
    for obra in obras:
        print(obra)

def vender_entradas():
    codigo = int(input("Ingrese el codigo de la obra: "))
    obra_encontrada = None
    for obra in obras:
        if obra.codigo == codigo:
            obra_encontrada = obra
            break
    if obra_encontrada is None:
        print("Error: no existe ese codigo")
        return
    cantidad = int(input("Ingrese la cantidad de entradas: "))
    if obra_encontrada.vender_entradas(cantidad):
        print(f"Quedan {obra_encontrada.butacas} butacas")

while True:
    print("\n===== TEATRO SUCRE =====")
    print("1. Registrar obra")
    print("2. Mostrar obras")
    print("3. Vender entradas")
    print("4. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_obra()

    elif opcion == "2":
        mostrar_obras()

    elif opcion == "3":
        vender_entradas()

    elif opcion == "4":
        print("Gracias por utilizar el sistema.")
        break

    else:
        print("Opcion no valida")