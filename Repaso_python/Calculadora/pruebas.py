import unittest

from Calculadora import calculadora

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        print("Realizamos la prueba")
        self.calculadora = calculadora(8,2)
    
    
    def test_suma(self):
        print("Prueba de suma correcta: ")
        self.assertEqual(self.calculadora.Sumar(),10,"La suma NO es correcta")
        
    def test_suma_erronea(self):
        print("Prueba de suma erronea: ")
        self.assertNotEqual(self.calculadora.Sumar(),11,"La suma NO es correcta")
    
        
    def test_resta(self):
        print("Prueba de resta correcta: ")
        self.assertEqual(self.calculadora.Restar(),6,"La resta NO es correcta")
        
    def test_resta_erronea(self):
        print("Prueba de resta erronea: ")
        self.assertNotEqual(self.calculadora.Restar(),11,"La resta NO es correcta")
        
        
    def test_multiplicacion(self):
        print("Prueba de multiplicacion correcta: ")
        self.assertEqual(self.calculadora.Multiplicar(),16,"La multiplicacion NO es correcta")
    
    def test_multiplicacion_erronea(self):
        print("Prueba de multiplicacion erronea: ")
        self.assertNotEqual(self.calculadora.Multiplicar(),11,"La multiplicacion NO es correcta")
        
    def test_dividir(self):
        print("Prueba de dividir correcta: ")
        self.assertEqual(self.calculadora.Dividir(),4,"La division NO es correcta")
        
    def test_multiplicacion_erronea(self):
        print("Prueba de dividir erronea: ")
        self.assertNotEqual(self.calculadora.Dividir(),None,"La multiplicacion NO es correcta")
        
      
if __name__ == '__main__':
    unittest.main()
