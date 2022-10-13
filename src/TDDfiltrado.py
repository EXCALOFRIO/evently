import unittest
from baseDatosPrueba import filtrarDiscotecas, insertarUsuario


class TestFiltrado(unittest.TestCase):

    def test_filtro_zona_minuscula(self):
        sentencia = filtrarDiscotecas(1, "centro")
        resultado = ['Independance Club', 'Joy Eslava',
                     'Kapital', 'Medias Puri', 'Shoko', 'Velvet']
        self.assertEqual(sentencia, resultado)

    def test_filtro_zona_mayuscula(self):
        sentencia = filtrarDiscotecas(1, "CENTRO")
        resultado = ['Independance Club', 'Joy Eslava',
                     'Kapital', 'Medias Puri', 'Shoko', 'Velvet']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre_minuscula(self):
        sentencia = filtrarDiscotecas(2, "blackhouse")
        resultado = ['Blackhouse']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre_mayuscula(self):
        sentencia = filtrarDiscotecas(2, "BLACKHOUSE")
        resultado = ['Blackhouse']
        self.assertEqual(sentencia, resultado)

    def test_filtro_calle_con_mayusculas(self):
        sentencia = filtrarDiscotecas(3, "Calle de Atocha")
        resultado = ['Independance Club', 'Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_calle_con_minusculas(self):
        sentencia = filtrarDiscotecas(3, "calle de atocha")
        resultado = ['Independance Club', 'Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion(self):
        sentencia = filtrarDiscotecas(4, "ambiente")
        resultado = ['Kapital']
        self.assertEqual(sentencia, resultado)


if __name__ == '__main__':
    unittest.main()
