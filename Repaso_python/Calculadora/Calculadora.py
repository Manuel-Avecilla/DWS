class calculadora():
    def __init__(self, num1=0,num2=0):
        self.num1 = num1
        self.num2 = num2

    def Sumar(self):
        return self.num1 + self.num2
    
    def Restar(self):
        return self.num1 - self.num2
    
    def Multiplicar(self):
        return self.num1 * self.num2
    
    def Dividir(self):
        if (self.num1 == 0) or (self.num2 == 0):
            print("ERROR: No se puede dividir entre 0")
            return None
        else:
            return self.num1 / self.num2

    
