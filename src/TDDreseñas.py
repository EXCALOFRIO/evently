import unittest
import sqlite3
from reseñas import *


class TestResennas(unittest.TestCase):
    miConexion = sqlite3.connect("BBDDpruebaReg")
    miCursor = miConexion.cursor()
    miCursor.execute(
        "CREATE TABLE IF NOT EXISTS valoraciones (nombre_discoteca VARCHAR(100), nota int NOT NULL, texto VARCHAR(500) DEFAULT NULL")

    def test_validarResenna(self):
        pass

    def test_getValoraciones(self):
        pass

    miConexion.close()


if __name__ == '__main__':
    unittest.main()
