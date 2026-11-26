class Persona:
    def __init__(self, nombre, apellido, cedula, celular, correo , edad, direccion):
        self.nombre=nombre
        self.apellido=apellido
        self.cedula=cedula
        self.celular=celular
        self.correo=correo
        self.edad=edad
        self.dereccion=direccion
    def validar_edad(self):
        if self.edad>=18:
            return "Es mayor de edad"
        else:
            return "Es menor de edad"
    def __str__(self):
        return f"nombre: {self.nombre}, Apellido: {self.apellido}, Cedula: {self.cedula}, Celular: {self.celular}, Correo: {self.correo}, Edad: {self.edad}, Direccion: {self.direccion}"