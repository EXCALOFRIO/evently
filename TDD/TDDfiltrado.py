import unittest
from src.filtrado import filtrarDiscotecas

class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        sentencia = filtrarDiscotecas(filtro = 1 , consulta = "Centro")
        esperado = "Independance Club\n Joy Eslava\n Kapital\n Medias Puri\n Shoko\n Velvet\n"
        self.assertEqual(sentencia,esperado)
        
    def test_filtro_nombre(self):
        sentencia = filtrarDiscotecas(filtro = 2 , consulta = "Blackhouse")
        esperado = "Blackhouse"
        self.assertEqual(sentencia,esperado)
    
    def test_filtro_valoracion(self):
        sentencia = filtrarDiscotecas(filtro = 1 , consulta = "5")
        esperado = "cats"
        self.assertEqual(sentencia,esperado)
    
    
if __name__ == '__main__':
    unittest.main()
        