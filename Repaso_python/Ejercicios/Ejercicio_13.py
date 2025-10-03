class Estudiante():
    def __init__(self,nombre="Desconocido",edad=0,curso="Desconocido"):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    def mostrarNombre(self):
        print("Nombre: ",self.nombre,"| Edad: ",self.edad,"| Curso: ",self.curso)
        
E1 = Estudiante("Pepe", 19, "2º de DAW")
E2 = Estudiante("Lucía", 20, "1º de DAM")
E3 = Estudiante("Carlos", 22, "2º de ASIR")
E4 = Estudiante("Marta", 18, "1º de DAW")
E5 = Estudiante("Javier", 21, "2º de DAM")

lista = [E1,E2,E3,E4,E5]

for Estudiante in lista:
    Estudiante.mostrarNombre()