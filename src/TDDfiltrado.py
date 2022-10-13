import unittest
from baseDatosPrueba import filtrarDiscotecas, insertarUsuario


class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        sentencia = filtrarDiscotecas(1, "centro")
        resultado = ['Independance Club', 'Joy Eslava',
                     'Kapital', 'Medias Puri', 'Shoko', 'Velvet']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre(self):
        sentencia = filtrarDiscotecas(2, "blackhouse")
        resultado = ['Blackhouse']
        self.assertEqual(sentencia, resultado)

    def test_filtro_calle(self):
        sentencia = filtrarDiscotecas(3, "calle de atocha")
        resultado = ['Independance Club', 'Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion(self):
        sentencia = filtrarDiscotecas(4, "ambiente")
        resultado = ['Kapital']
        self.assertEqual(sentencia, resultado)


if __name__ == '__main__':
    unittest.main()
