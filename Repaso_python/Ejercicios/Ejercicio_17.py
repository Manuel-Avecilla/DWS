class FiguraGeometrica():
    def __init__(self,ancho=0,altura=0,nombre=""):
        self.ancho = ancho
        self.altura = altura
        self.nombre = nombre
        
    def CalcularArea(self):
        pass
    
    def __str__(self):
        return f"Figura: {self.nombre}, | Ancho: {self.ancho} | Altura: {self.altura}"
    
    
class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho=0, altura=0):
        super().__init__(ancho, altura,"Rectangulo")
        
    def CalcularArea(self):
        return self.ancho*self.altura
    
class Triangulo(FiguraGeometrica):
    def __init__(self, ancho=0, altura=0):
        super().__init__(ancho, altura, "Triangulo")
        
    def CalcularArea(self):
        return (self.ancho * self.altura)/2
    

R1 = Rectangulo(10,5)
R2 = Rectangulo(4,13)
R3 = Rectangulo(12,4)

T1 = Triangulo(10,5)
T2 = Triangulo(4,13)
T3 = Triangulo(12,4)

lista = [R1,R2,R3,T1,T2,T3]

for FiguraGeometrica in lista:
    print(FiguraGeometrica,"| El area es: ",FiguraGeometrica.CalcularArea())

