import unittest
from filtrado import *

from baseDatosPrueba import comprobarInicioSesion, comprobarUsuario, insertarDiscoteca, insertarFiesta, insertarUsuario, insertarValoracion

# test para ver si el metodo insertarUsuario de la clase baseDatosPrueba funciona correctamente


class TestInsertarUsuario(unittest.TestCase):

    def test_insertarUsuario(self):
        db.reference('test').child('usuarios').delete()
        print("empieza test 1\n")
        insertarUsuario('usuario', 'nombre', 'apellido',
                        '8', 'email@email.es', 'contraseña', 'test')

        # imprime los usuarios de la base de datos y comprueba que las variable son correctas
        usuarios = db.reference('test/usuarios')
        for i in usuarios.get():
            self.assertEqual(usuarios.get()[i]['usuario'], 'usuario')
            self.assertEqual(usuarios.get()[i]['nombre'], 'nombre')
            self.assertEqual(usuarios.get()[i]['apellido'], 'apellido')
            self.assertEqual(usuarios.get()[i]['edad'], '8')
            self.assertEqual(usuarios.get()[i]['email'], 'email@email.es')
            self.assertEqual(usuarios.get()[i]['contraseña'], 'contraseña')
            db.reference('test').child(i).delete()


    def test_insertarDiscoteca(self):
        print("empieza test 2\n")
        insertarDiscoteca('nombre', 'zona', 'calle', '8', 'test')
        discotecas = db.reference('test/discotecas')
        for i in discotecas.get():
            self.assertEqual(discotecas.get()[i]['nombre'], 'nombre')
            self.assertEqual(discotecas.get()[i]['zona'], 'zona')
            self.assertEqual(discotecas.get()[i]['calle'], 'calle')
            self.assertEqual(discotecas.get()[i]['numero'], '8')
            db.reference('test').child('discotecas').delete()

    def test_insertatFiesta(self):
        print("empieza test 3\n")
        insertarFiesta('nombre', 'calle', 'numero', 'zona', 'test')
        fiestas = db.reference('test/fiestas')
        for i in fiestas.get():
            self.assertEqual(fiestas.get()[i]['nombre'], 'nombre')
            self.assertEqual(fiestas.get()[i]['zona'], 'zona')
            self.assertEqual(fiestas.get()[i]['calle'], 'calle')
            self.assertEqual(fiestas.get()[i]['numero'], 'numero')
            db.reference('test').child('fiestas').delete()

    def test_insertarValoracion(self):
        print("empieza test 4\n")
        insertarValoracion('usuario', 'nombre_discoteca',
                           'nota', 'texto', 'test')
        valoraciones = db.reference('test/valoraciones')
        for i in valoraciones.get():
            self.assertEqual(valoraciones.get()[i]['usuario'], 'usuario')
            self.assertEqual(valoraciones.get()[
                             i]['nombre_discoteca'], 'nombre_discoteca')
            self.assertEqual(valoraciones.get()[i]['nota'], 'nota')
            self.assertEqual(valoraciones.get()[i]['texto'], 'texto')
            db.reference('test').child('valoraciones').delete()

    def test_inicioSession(self):
        db.reference('test/usuarios').child('usuarios').delete()
        print("empieza test 5\n")
        insertarUsuario('usuario', 'nombre', 'apellido',
                        '8', 'email@gmail.com', 'contraseña', 'test')
        self.assertEqual(comprobarInicioSesion(
            'usuario', 'contraseña', 'test'), True)
        db.reference('test').child('usuarios').delete()


if __name__ == '__main__':
    unittest.main()
