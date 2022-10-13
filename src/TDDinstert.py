import unittest

from baseDatosPrueba import borrarDatos, borrarTodo, comprobarInicioSesion, getItemBaseDatos, insertarDiscoteca, insertarFiesta, insertarUsuario, insertarValoracion

# test para ver si el metodo insertarUsuario de la clase baseDatosPrueba funciona correctamente


class TestInsertarUsuario(unittest.TestCase):

    def test_insertarUsuario(self):
        borrarDatos('usuarios')
        insertarUsuario('usuario', 'nombre', 'apellido',
                        '8', 'email@email.es', 'contraseña', 'test')
        self.assertEqual(getItemBaseDatos(
            'usuarios', 'usuario', 'test')[0], 'usuario')
        self.assertEqual(getItemBaseDatos(
            'usuarios', 'nombre', 'test')[0], 'nombre')
        self.assertEqual(getItemBaseDatos(
            'usuarios', 'apellido', 'test')[0], 'apellido')
        self.assertEqual(getItemBaseDatos('usuarios', 'edad', 'test')[0], '8')
        self.assertEqual(getItemBaseDatos(
            'usuarios', 'email', 'test')[0], 'email@email.es')
        self.assertEqual(getItemBaseDatos(
            'usuarios', 'contraseña', 'test')[0], 'contraseña')
        borrarDatos('usuarios')

    def test_insertarDiscoteca(self):
        borrarDatos('discotecas')
        insertarDiscoteca('B12', 'Calle de Joaquín Costa', '27', 'Tetuán', 'test')
        self.assertEqual(getItemBaseDatos(
            'discotecas', 'nombre', 'test')[0], 'B12')
        self.assertEqual(getItemBaseDatos(
            'discotecas', 'zona', 'test')[0], 'Tetuán')
        self.assertEqual(getItemBaseDatos(
            'discotecas', 'calle', 'test')[0], 'Calle de Joaquín Costa')
        self.assertEqual(getItemBaseDatos(
            'discotecas', 'numero', 'test')[0], '27')
        borrarDatos('discotecas')

    def test_insertatFiesta(self):
        insertarFiesta('Mana', 'Calle de Maldonado', '55', 'Castellana', 'test')
        self.assertEqual(getItemBaseDatos(
            'fiestas', 'nombre', 'test')[0], 'Mana')
        self.assertEqual(getItemBaseDatos(
            'fiestas', 'calle', 'test')[0], 'Calle de Maldonado')
        self.assertEqual(getItemBaseDatos(
            'fiestas', 'numero', 'test')[0], '55')
        self.assertEqual(getItemBaseDatos(
            'fiestas', 'zona', 'test')[0], 'Castellana')
        borrarDatos('fiestas')

    def test_insertarValoracion(self):
        insertarValoracion('usuario', 'nombre_discoteca',
                           'nota', 'texto', 'test')
        self.assertEqual(getItemBaseDatos(
            'valoraciones', 'usuario', 'test')[0], 'usuario')
        self.assertEqual(getItemBaseDatos(
            'valoraciones', 'nombre_discoteca', 'test')[0], 'nombre_discoteca')
        self.assertEqual(getItemBaseDatos(
            'valoraciones', 'nota', 'test')[0], 'nota')
        self.assertEqual(getItemBaseDatos(
            'valoraciones', 'texto', 'test')[0], 'texto')
        borrarDatos('valoraciones')

    def test_inicioSession(self):
        borrarDatos('usuarios')
        insertarUsuario('usuario', 'nombre', 'apellido', '8',
                        'email@gmail.com', 'contraseña', 'test')
        self.assertEqual(comprobarInicioSesion(
            'usuario', 'contraseña', 'test'), True)
        borrarDatos('usuarios')


if __name__ == '__main__':
    unittest.main()
    borrarTodo('test')

