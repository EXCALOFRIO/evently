import unittest
from src.filtrado import filtrarDiscotecas

class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        sentencia = filtrarDiscotecas(filtro = 1 , consulta = "Centro")
        resultado = "Independance Club\n Joy Eslava\n Kapital\n Medias Puri\n Shoko\n Velvet\n"
        self.assertEqual(sentencia,resultado)
        
    def test_filtro_nombre(self):
        sentencia = filtrarDiscotecas(filtro = 2 , consulta = "Blackhouse")
        resultado = "Blackhouse"
        self.assertEqual(sentencia,resultado)
    
    def test_filtro_valoracion(self):
        sentencia = filtrarDiscotecas(filtro = 4, consulta = "5")
        resultado = "cats"
        self.assertEqual(sentencia,resultado)
    
    
if __name__ == '__main__':
    unittest.main()
        