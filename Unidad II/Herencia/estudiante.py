from  persona import Persona
class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, celular, correo , edad, direccion, carrera,notas):
            super().__init__( nombre, apellido, cedula, celular, correo , edad, direccion)
            self.carrera=carrera
            self.notas=notas
    def promedio(self):
          return sum(self.notas)/len(self.notas)
    def validar_edad(self):
          return f"{super().validar_edad()} carrera: {self.carrera}"
    def __str__(self):
          return f"{super().__str__} carrera: {self.carrera} promedio: {self.promedio()}"