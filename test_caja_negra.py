def suma(num1,num2):
    return num1 + num2


def multiplicacion(num_1,num_2):
    return num_1 * num_2

#PASO 1: Importar unittest
import unittest

#PASO2: crear una clase y al nombre pasarle los 
#parametros "unittest.testcase"

class CajaNegraTest(unittest.TestCase):
    #Paso 3: crear la función para el test
    #iniciando con test y pasandole como
    #parametros la función "self"
    def test_suma_dos_enteros(self):
        num1 = 5
        num2 = 10

        result = suma(num1,num2)
        #UTILIZAR LA FUNCION self.assertEqual(var,"resultado_esperado") 
        self.assertEqual(result,15) 

    def test_multiplicacion_dos_enteros(self):
        num_1 = 12
        num_2 = 2

        result = multiplicacion(num_1,num_2)
        self.assertEqual(result,24)

#DEBEMOS DEFINIR QUE LA FUNCIÓN CREADA
#ES UN MÓDULO PRINCIPAL PARA ELLO---
if __name__ == '__main__':
    unittest.main(verbosity=2 )
