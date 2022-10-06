import unittest
from filtrado import *

class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        sentencia = filtrarDiscotecas(1, "centro")
        resultado = (f"Independance Club\nJoy Eslava\nKapital\nMedias Puri\nShoko\nVelvet")
        self.assertEqual(sentencia,resultado)
      
    def test_filtro_nombre(self):
        print("empieza test2")
        sentencia = filtrarDiscotecas(2,"blackhouse")
        resultado = "Blackhouse"
        self.assertEqual(sentencia,resultado)
    
    def test_filtro_valoracion(self):
        print("empieza test3")
        sentencia = filtrarDiscotecas(4, "buena")
        resultado = "cats"
        self.assertEqual(sentencia,resultado)
    
    
if __name__ == '__main__':
    unittest.main()
        