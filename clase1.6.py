#crear una clase 
class Libro:
    pass

libro1 = Libro()
print(type(libro1))

# crear constructor de la clase
class Libro:
    def __init__(self, nombre, autor, estado, listaLibros):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.listaLibros = listaLibros

    def mostrar(self):
        print("Nombre del libro:", self.nombre, "Autor:", self.autor)

    def cambiar_estado(self, estado1):
        self.estado = estado1

    def mostrar_lista(self):
        for e in self.listaLibros:
            print(e)

    def __str__(self):
        return f"Nombre: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}"

libro2 = Libro("Python intermedio", "Sandoval", "Disponible", ["Python basico", "Python intermedio"])
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("Prestado")
print(libro2)
libro2.estado = "Disponible"
print(libro2)
print(libro2.nombre)
libro2.mostrar_lista()