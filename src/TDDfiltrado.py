import unittest
from filtrado import *

class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        #firebase = firebase.FirebaseApplication("https://evently-646a2-default-rtdb.firebaseio.com/", None)
        resultado = filtrarDiscotecas(filtro = 1 , consulta = "Centro")
        esperado = "Independance Club\n Joy Eslava\n Kapital\n Medias Puri\n Shoko\n Velvet\n"
        self.assertEqual(resultado,esperado)
        
if __name__ == '__main__':
    unittest.main()
        