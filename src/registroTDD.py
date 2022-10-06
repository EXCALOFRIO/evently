import unittest
import sqlite3
from registro import insertarUsuario
from registro import comprobarUsuario


class TestRegistro(unittest.TestCase):

    miConexion = sqlite3.connect("BBDDpruebaReg")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "CREATE TABLE IF NOT EXISTS usuarios (usuario VARCHAR(100), nombre VARCHAR(100), apellido VARCHAR(100), edad INTEGER, email VARCHAR(100), contraseña VARCHAR(100))")

    def test_registro(self):

        sentencia = insertarUsuario(
            "usr", "name", "srname", 18, "name@gmail.com", "123abc")
        resultado = comprobarUsuario(
            "usr", "name", "srname", 18, "name@gmail.com", "123abc")

        self.assertTrue(resultado)

    miConexion.close()


if __name__ == '__main__':
    unittest.main()
