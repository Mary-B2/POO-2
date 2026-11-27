from estudiante import Estudiante
from docente import Docente

estudiante1=Estudiante("Maria", "Bravo", "0107009508", "0997544690", "mary540026@gmail.com", 20, "Gualaceo", "TSUDS", [7,8,8,7,9])
print(estudiante1.validar_edad())
print(f"Promedio: {e.promedio()}")

estudiante2=Estudiante("Andrea", "Ulloa", "0105088978", "099896690", "andy5786@gmail.com", 21, "Mira Flores", "Big Data", [7,8,9,10,9])
print(estudiante2.validar_edad())
print(f"Promedio: {e.promedio()}")

estudiante3=Estudiante("Diego", "Fajardo", "0102586308", "0994789621", "diego2548@gmail.com", 18, "Av Gran Colombia", "Ciberseguridad", [6,8,10,7,9])
print(estudiante3.validar_edad())
print(f"Promedio: {e.promedio()}")

estudiante4=Estudiante("Katherin", "Lopez", "0107040509", "0987965432", "katty98736@gmail.com", 16, "Av Jaime Roldos", "Tributacion", [9,5,8,7,10])
print(estudiante4.validar_edad())
print(f"Promedio: {e.promedio()}")

estudiante5=Estudiante("Juan", "Torres", "0101245637", "0912548763", "juan9852@gmail.com", 17, "Av Americas", "Mecatronica", [7,5,8,7,6])
print(estudiante5.validar_edad())
print(f"Promedio: {e.promedio()}")

print("Docente")
docente1=Docente("Julio", "Torres", "0112559348", "0968456721", "julio98@gmail.com", 35, "Av España", "Base de Datos", 8)
print(docente1.validar_edad())
print(docente1.calcular_salario())

docente2=Docente("Marcela", "Gomez", "010899652", "0968456721", "marce47@gmail.com", 35, "Av Americas", "POO", 8)
print(docente2.validar_edad())
print(docente2.calcular_salario())

docente3=Docente("Mayra", "Guzman", "0104542366", "0968456721", "mayra25@gmail.com", 35, "Davila Chica", "Calculo", 8)
print(docente3.validar_edad())
print(docente3.calcular_salario())

docente4=Docente("Norma", "Tigre", "014792223", "0968456721", "norma65@gmail.com", 35, "Antonio Cordero", "Redes", 8)
print(docente4.validar_edad())
print(docente4.calcular_salario())

docente5=Docente("Miguel", "Calle", "0125478236", "0968456721", "migue336@gmail.com", 35, "Av Gran Colombia", "Desarrollo Web", [8])
print(docente5.validar_edad())
print(docente5.calcular_salario())

print("Estudiante")
estudiantes=[estudiante1, estudiante2, estudiante3, estudiante4, estudiante5]
for e in estudiantes:
    print(e.validar_edad())
    print(f"Promedio: {e.promedio()}")
print("Docente")
docentes=[docente1, docente2, docente3, docente4, docente5]
for d in docentes:
    print(d.validar_edad())
    print(f"Salario: {d.calcular_salario()}")
