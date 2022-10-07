import unittest
from baseDatosPrueba import insertarUsuario
from filtrado import *

#--------------NO TERMINADO--DA ERROR----------------------------#


class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        print("empieza test 1\n")
        sentencia = filtrarDiscotecas(1, "centro")
        resultado = ['Independance Club', 'Joy Eslava',
                     'Kapital', 'Medias Puri', 'Shoko', 'Velvet']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre(self):
        print("empieza test 2\n")
        sentencia = filtrarDiscotecas(2, "blackhouse")
        resultado = "Blackhouse"
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion(self):
        print("empieza test 3\n")
        sentencia = filtrarDiscotecas(4, "buen ambiente")
        resultado = "cats"
        self.assertEqual(sentencia, resultado)


if __name__ == '__main__':
    unittest.main()
