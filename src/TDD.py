import unittest
from baseDatosPrueba import filtrarDiscotecas, insertarUsuario, borrarDatos, borrarTodo, comprobarInicioSesion, getItemBaseDatos, insertarDiscoteca, insertarFiesta, insertarUsuario, insertarValoracion, comprobarUsuario, mostrar_carta


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

    def test_filtro_zona_false(self):
        sentencia = filtrarDiscotecas(1, 'carabanchel')
        self.assertEqual(sentencia, [])

    def test_filtro_nombre_minuscula(self):
        sentencia = filtrarDiscotecas(2, "blackhouse")
        resultado = ['Blackhouse']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre_mayuscula(self):
        sentencia = filtrarDiscotecas(2, "BLACKHOUSE")
        resultado = ['Blackhouse']
        self.assertEqual(sentencia, resultado)

    def test_filtro_nombre_false(self):
        sentencia = filtrarDiscotecas(2, 'evently')
        self.assertEqual(sentencia, [])

    def test_filtro_calle_con_mayusculas(self):
        sentencia = filtrarDiscotecas(3, "Calle de Atocha")
        resultado = ['Independance Club', 'Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_calle_con_minusculas(self):
        sentencia = filtrarDiscotecas(3, "calle de atocha")
        resultado = ['Independance Club', 'Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_calle_false(self):
        sentencia = filtrarDiscotecas(3, 'Calle de las cariñosas')
        self.assertEqual(sentencia, [])

    def test_filtro_valoracion_minuscula(self):
        sentencia = filtrarDiscotecas(4, "ambiente")
        resultado = ['Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion_mayuscula(self):
        sentencia = filtrarDiscotecas(4, "AMBIENTE")
        resultado = ['Kapital']
        self.assertEqual(sentencia, resultado)

    def test_filtro_valoracion_false(self):
        sentencia = filtrarDiscotecas(4, "cariñosas")
        self.assertEqual(sentencia, [])

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
        
    def test_registroUsuarioExistente(self):
        borrarDatos('usuarios')
        insertarUsuario('usuario', 'nombre', 'apellido',
                        '8', 'email@email.es', 'contraseña', 'test')
        usuario_valido = comprobarUsuario('usuario', 'nombre', 'apellido',
                        '8', 'email@email.es', 'contraseña', 'test')
        self.assertFalse(usuario_valido)
        
    def test_registroEmailIncorrecto(self):
        borrarDatos('usuarios')
        insertarUsuario('usuario', 'nombre', 'apellido', '10', 'usuario', 'contraseña', 'test')
        usuario_valido = comprobarUsuario('usuario', 'nombre', 'apellido', '10', 'usuario', 'contraseña', 'test')
        self.assertFalse(usuario_valido)
        
    def test_inicioSesionCamposVacios(self):
        datosValidos = comprobarInicioSesion('', '', 'test')
        self.assertFalse(datosValidos)
        
    def test_inicioSesionContrasenaIncorrecta(self):
        borrarDatos('usuarios')
        insertarUsuario('usuario', 'nombre', 'apellido', '10', 'usuario@gmail.com', 'contraseña', 'test')
        inicio_sesion_correcto = comprobarInicioSesion('usuario', 'contraseñaIncorrecta', 'test')
        self.assertFalse(inicio_sesion_correcto)

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
                           'nota', 'texto', 'fecha', 'test')
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
        
    def test_insertar_valoracion_fecha(self):
        insertarValoracion('usuario', 'nombre_discoteca', 'nota', 'texto', 'fecha', 'test')
        self.assertEqual(getItemBaseDatos('valoraciones', 'fecha', 'test')[0], 'fecha')
        borrarDatos('fecha')

    def test_mostrar_carta(self):
        resultado = mostrar_carta('B12','data')
        esperado = 'En B12 encontrarás una lista de los mejores alcoholes. Ron: Barceló, Cacique, Legendario, Brugal. Whisky: J&B, Johnny Walker, Jack Daniels. Ginebra: Larios, Beefeater, Tanquerai. Cervezas: Águila, Alhambra, Mahou, Estrella Galicia, Cruzcampo. Vinos: Sangre de Judas, Catena, Torres, 19 Crimes, Antinori'
        self.assertEqual(resultado, esperado)
        
if __name__ == '__main__':
    unittest.main()
