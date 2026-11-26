from datetime import date
class Equipo: 
    def __init__(self, codigo, tipo, valor_reposion, diponibles):
        self.codigo=codigo
        self.tipo=tipo
        self.valor_reposicion=valor_reposion
        self.disponibles=diponibles
    def __str__(self):
        return f"codigo: {self.codigo} tipo: {self.tipo} valor reposicion: {self.valor_reposicion} disponibles: {self.disponibles}"

class Prestamo:
    def __init__(self, numero, codigo_equipo, estudiante, cantidad, fecha, estado ):
        self.numero=numero
        self.codigo_equipo=codigo_equipo
        self.estudiante=estudiante
        self.cantidad=cantidad
        self.fecha=fecha
        self.estado=estado
    def __str__(self):
        return f"numero: {self.numero} codigo de equipo: {self.codigo_equipo} estudiante: {self.estudiante} cantidad: {self.cantidad} fecha: {self.fecha} estado: {self.estado}"

class Laboratorio:
    def __init__(self):
        self.listaEquipos=[]
        self.listaPrestamos=[]
        self.cargar_datos

    def cargar_datos(self):
        listaE=[
            Equipo(1, "Laptop", 650,8),
            Equipo(2,"Proyector",420,3)
        ]
        for e in listaE:
            self.listaEquipos.append(e)
        listaP=[
            Prestamo(1,2,"Daniela",2, date(2026,11,26),"activo")
        ]
        for p in listaP:
            self.listaPrestamos.append(p)
    #def registrar(self, tipo, valor_reposicion, disponibles):
        #if disponibles <=0:


   
        

        