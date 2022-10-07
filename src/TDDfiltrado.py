import unittest
from baseDatosPrueba import insertarUsuario
from filtrado import *
from firebase_admin import credentials
from firebase_admin import db
class TestFiltrado(unittest.TestCase):

    def test_filtro_zona(self):
        print("empieza test 1\n")
        cred = credentials.Certificate("firebase/evently-key.json")
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
    })
        sentencia = filtrarDiscotecas(1, "centro")
        resultado = ['Independance Club', 'Joy Eslava',
                     'Kapital', 'Medias Puri', 'Shoko', 'Velvet']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre(self):
        print("empieza test 2\n")
        cred = credentials.Certificate("firebase/evently-key.json")
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
        })
        
        sentencia = filtrarDiscotecas(2, "blackhouse")
        resultado = "Blackhouse"
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion(self):
        print("empieza test 3\n")
        cred = credentials.Certificate("firebase/evently-key.json")
        firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
        })
        sentencia = filtrarDiscotecas(4, "buen ambiente")
        resultado = "cats"
        self.assertEqual(sentencia, resultado)


if __name__ == '__main__':
    unittest.main()
