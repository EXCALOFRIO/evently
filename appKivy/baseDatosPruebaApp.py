import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="evently")
firebase_admin.initialize_app(credentials.Certificate({
    "type": "service_account",
    "project_id": "evently-646a2",
    "private_key_id": "4e16c187074ef1ab70c1be4901d03d55e82cf521",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCk6DhtSvEvDsHm\nvFtmsdIZGIirivDL5nVSsN98wgeeu3Y0ITtG8kSfs2D9U21uIbj3DEZ+58TiB2u1\nGXrAioa8Ocf+AhUeGp/VZtRQTntmZ7amPsjbM1vwQVlWyhETyns3Tlc5ivLJ2K15\ntfk//W4UudCb+p5bqbQz9iyUWkZOJZ01hXLQeNqXNhQPKByDulE0CvjPShBjEXka\n9sdjNFsWl3NrG66ltjZrphzwdYib1i5JtA4N42OJ+r1wHs8Eccv9ZWWrEDjisTNq\n9oXxJF+IvgJXWTwBWTmkqgKEXL0LTT5AdIbcS2RFZLvT536vNaX7HbNoiFhWdJsJ\nNvutb413AgMBAAECggEAAUx+QUdxUy8OZ5Gn4KJZkW6y3jMCcYCs/4vlaWH31bq2\nlB4yOCf+qAlYJAv3qoHj0eJMCIItIqCaAGZPzrC980E7P4IRsNfXLBhFZ3qEGKA2\n0o61CJuaHPAkKChVmRkjqPcE0y8HztTWN5qveLRiHRICQBrptgwbShDQH2ep8myb\nLMfR5BNXs7vd0VKkm6hk+1XRKovKK7bW/IdFf0U4deGrgj7d15mcXCRfd9c2YxZT\nKjxFWql2Nxr6sa+WUvot03royLEDZPUWbwbbLatf+v3ZeZDhFAvr576Bscq2lTp2\n5KF4xk+su3YcOVU66IRj8CnQEBzPWct9W479wOeUFQKBgQDY2ae0GZUmhkHBjXPz\ncrIwIYA5xW+i8/4dCgY64AJQndHeXEvKQXl0HMaC2LqRhZNFVGu6yqc2gxi9MO6C\n6yHywlEIaotoVdLnWbRJN03D4iPP+rkuXLoVPWcNJRFVOXEzbylfJKsFIWB+JZ8/\n8zirdxVeErfNRhdKmR4YfQRFXQKBgQDCrd49ElyUsy7nM7ENuNTkncJ1dKwx/7n8\nk2pgw6U87UI0zNP7ThuMnlwzEwMD1Vmukd+h5/yBY9y6O+h1z36REmBdHpAt44Fw\ny26bXBMfud0rIS6SRHzHfkjwwrLLH8j4VkdmUPyul7ylx1nlwGLr27GXv67rJXB/\nnPlnf3F84wKBgFyu8rHUeV5E5df/SH7WF/jgaLjIfUWNuZ/Zx/3j/rlMKwY6Np6U\ny39oSSRl06AdEmwAgCcPNNbkw28hed/09caXbSEGwNzwSbteKONeQtulTR84j2uU\ncGhhnSkOHdFqQsr0CR/EQWBo+qAQHner0h3fQP+7SlnvSkc1GJro3Cl1AoGAR4lA\nSsy+fF3DdG3IN7SddkyKMkLnK5A+tZMt2dTKmTLNyz0hAA1Zjjh6xMHNr9DsHXu4\n43Otk5Ywe7ab2v6eEYzhIBalAFfDLsFyKWCSHmxb2wdcZ58HAv9iqiXBMWbCoI6D\nuhM0ZquXRIuWexhQwT5/abWj/wBI8HusId3ww+UCgYBwraEeyXnUSipmAtDXg+kr\nGq3QRMwNCVS5tBku9ka7RfJpQzCv1y9LwpQ8Kjbzrg2vQAbrwnDVtswrSAiwVSYz\nI6QJWuOZlGkXysBGXWoVOUrEdZIgn3Xp1PI5uwu9h2qrXj96a9ISuhlTDhf3nrO9\n2ZNvMt0yoD78e6x7I2HBtg==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-v8e3j@evently-646a2.iam.gserviceaccount.com",
    "client_id": "113165337138307162527",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-v8e3j%40evently-646a2.iam.gserviceaccount.com",
}), {'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
     })

# THEME
# Array de colores
# metodo para cambiar el tema
fuentePrincipal = "ABeeZee"


def colorTema(numero):
    listaColores = ["#8b9dc3", "#57E389", "#F2A365", "#E3F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2",
                    "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3", "#A6F2A6", "#F2A6A6", "#A6F2F2", "#E3A6F2", "#A6E3F2", "#F2E3A6", "#F2A6E3"]
    return listaColores[numero]


def color2Tema(numero):
    listaColores = ["#241f31", "#16151a"]
    return listaColores[numero]

# funcion cambiar de hex a rgb


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


color = colorTema(0)
color2 = color2Tema(1)


##############################################################################
#METODOS PARA INSERTAR LOS DIFERENTES DATOS EN LAS TABLAS DE LA BASE DE DATOS#
##############################################################################


def insertarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta):
    usuarios = {
        'usuario': usuario,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'email': email,
        'contraseña': contraseña
    }
    db.reference(ruta).child('usuarios').push(usuarios)


def insertarMensaje(usuario, mensaje, chat, ruta):
    mensajes = {
        'usuario': usuario,
        # 'chat': chat,
        'mensaje': mensaje
    }
    db.reference(ruta).child('chats').child(chat).push(mensajes)


# enviarMensaje('Daguerre','hola','DaguerreAlejandro')

def insertarDiscotecaEficiente(nombre, ubicacion, longitud, latitud, ruta):
    discotecas = {
        'nombre': nombre,
        'ubicacion': ubicacion,
        'longitud': longitud,
        'latitud': latitud
    }
    db.reference(ruta).child('discotecasEficientes').push(discotecas)


def insertarDiscoteca(nombre, calle, numero, zona, ruta):
    discotecas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    db.reference(ruta).child('discotecas').push(discotecas)
    ubicacion = calle + ', ' + str(numero) + ', ' + zona + ', Madrid España'
    ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
        'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c', 'Calle ').replace('av', 'Avenida ').replace('avda', 'Avenida ').replace('c.', 'Calle ').replace('pl', 'Plaza ')

    location = geolocator.geocode(ubicacion2)
    insertarDiscotecaEficiente(
        nombre, ubicacion2, location.longitude, location.latitude, ruta)

# crea un metodo que de la base de datos extraiga todos los datos de las discotecas y llame a la funcion insertarDiscotecaEficiente


def insertarDiscotecasEficienteScript(ruta):
    discotecas = db.reference(ruta+'/discotecas')
    for k, v in discotecas.get().items():
        nombre = v['nombre']
        calle = v['calle']
        numero = v['numero']
        zona = v['zona']
        ubicacion = calle + ', ' + \
            str(numero) + ', Madrid España'
        ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
            'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c ', 'Calle ').replace('av ', 'Avenida ').replace('avda ', 'Avenida ').replace('c.', 'Calle ').replace('pl ', 'Plaza ')
        location = geolocator.geocode(ubicacion2)
        insertarDiscotecaEficiente(
            nombre, ubicacion2, location.longitude, location.latitude, ruta)


def insertarFiestaEficiente(nombre, ubicacion, longitud, latitud, ruta):
    fiestas = {
        'nombre': nombre,
        'ubicacion': ubicacion,
        'longitud': longitud,
        'latitud': latitud
    }
    db.reference(ruta).child('fiestasEficientes').push(fiestas)


def insertarFiesta(nombre, calle, numero, zona, usuario, ruta):
    fiestas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona,
        'usuario': usuario

    }
    db.reference(ruta).child('fiestas').push(fiestas)
    ubicacion = calle + ', ' + str(numero) + ', ' + zona + ', Madrid España'
    ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
        'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c ', 'Calle ').replace('av ', 'Avenida ').replace('avda ', 'Avenida ').replace('c.', 'Calle ').replace('pl ', 'Plaza ')
    location = geolocator.geocode(ubicacion2)
    # print(ubicacion2)
    insertarFiestaEficiente(
        nombre, ubicacion2, location.longitude, location.latitude, ruta)


def borrarDatos(datos):
    db.reference('test').child(datos).delete()


def borrarTodo(ruta):
    db.reference(ruta).delete()


def getItemBaseDatos(elemento, variable, ruta):
    lista = []
    if db.reference(ruta).child(elemento).get() != None:
        for k, v in db.reference(ruta).child(elemento).get().items():
            lista.append(v[variable])
        return lista
    else:
        return lista


def getTodosLosDatos(elemento, ruta):
    lista = []
    if db.reference(ruta).child(elemento).get() != None:
        for k, v in db.reference(ruta).child(elemento).get().items():
            lista.append(v)
        return lista
    else:
        return lista

# Metodo de para mostrar la carta de las discotecas


def mostrar_carta(elemento, variable, ruta):
    elemento = db.reference(ruta+'/'+elemento)
    lista = []
    for v, k in elemento.get().items():
        if v == variable:
            lista.append(k)
    return lista[0]

# TODO  crea un metodo que devuelava la key sabiendo la posocion en el array

################################################################
#METODO PARA COMPROBAR SI EL USUARIO EXISTE EN LA BASE DE DATOS#
################################################################


def variableUsuario(usuario, nombre, apellido, edad, email, contraseña):
    global usuarioActual
    usuarioActual = {
        'usuario': usuario,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'email': email,
        'contraseña': contraseña
    }


def variableUsuarioSimp(usuario):
    global usuarioActualSimp
    usuarioActualSimp = {
        'usuario': usuario,
    }


def variableNombreUsuario(nombre):
    global nombreUsuarioActual
    nombreUsuarioActual = {
        'nombre': nombre,
    }


def variableApellidoUsuario(apellido):
    global apellidoUsuarioActual
    apellidoUsuarioActual = {
        'apellido': apellido,
    }


def variableEmailUsuario(email):
    global emailUsuarioActual
    emailUsuarioActual = {
        'email': email,
    }


def variableEdadUsuario(edad):
    global edadUsuarioActual
    edadUsuarioActual = {
        'edad': edad,
    }


def datosUsuario(datos):
    return usuarioActualSimp[datos]


def nombreUsuario(datos):
    return nombreUsuarioActual[datos]


def apellidoUsuario(datos):
    return apellidoUsuarioActual[datos]


def emailUsuario(datos):
    return emailUsuarioActual[datos]


def edadUsuario(datos):
    return edadUsuarioActual[datos]


def comprobarValoracion(fecha, usuario, nombre_discoteca, ruta):

    fechasArray = getItemBaseDatos('valoraciones', 'fecha', 'data')
    nombresArray = getItemBaseDatos('valoraciones', 'nombre_discoteca', 'data')
    usuarioArray = getItemBaseDatos('valoraciones', 'usuario', 'data')
    posicionesNombres = ([indice for indice, dato in enumerate(
        nombresArray) if dato == nombre_discoteca])
    for posicion in posicionesNombres:
        if(usuarioArray[posicion] == usuario):
            if(fechasArray[posicion] == fecha):
                return False

    return True


def insertarValoracion(fecha, usuario, nombre_discoteca, nota, texto, ruta):
    if(comprobarValoracion(fecha, usuario, nombre_discoteca, ruta)):
        valoraciones = {
            'fecha': fecha,
            'usuario': usuario,
            'nombre_discoteca': nombre_discoteca,
            'nota': nota,
            'texto': texto

        }
        db.reference(ruta).child('valoraciones').push(valoraciones)


def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta):
    if usuario in getItemBaseDatos('usuarios', 'usuario', ruta) or email in getItemBaseDatos('usuarios', 'email', ruta) or '@' not in email or '.' not in email or usuario == '' or nombre == '' or apellido == '' or edad == '' or email == '' or contraseña == '':
        # print('El usuario o el email ya existen o no ha rellenado todos los campos o el email no es correcto')
        return False
    insertarUsuario(usuario, nombre, apellido,
                    edad, email, contraseña, ruta)
    return True


def comprobarInicioSesion(usuario, contraseña, ruta):
    if usuario == '' or contraseña == '':
        # print('Todos los campos deben estar completos.')
        return False
    indice = getItemBaseDatos('usuarios', 'usuario', ruta).index(usuario)
    if getItemBaseDatos('usuarios', 'contraseña', ruta)[indice] == contraseña:
        variableUsuarioSimp(usuario)
        nombreUsr = getItemBaseDatos('usuarios', 'nombre', ruta)[indice]
        variableNombreUsuario(nombreUsr)
        apellidoUsr = getItemBaseDatos('usuarios', 'apellido', ruta)[indice]
        variableApellidoUsuario(apellidoUsr)
        emailUsr = getItemBaseDatos('usuarios', 'email', ruta)[indice]
        variableEmailUsuario(emailUsr)
        edadUsr = getItemBaseDatos('usuarios', 'edad', ruta)[indice]
        variableEdadUsuario(edadUsr)
        return True
    # print('El usuario o la contraseña no son correctos, o no ha rellenado todos los campos')
    return False


def valoracionesUsuario(usuario):
    valoraciones = db.reference('data/valoraciones')
    temp = []
    for k, v in valoraciones.get().items():
        if v['usuario'].lower().__contains__(str(usuario)+'·º·'):
            resultado = 'FECHA: ', v['fecha'], 'DISCOTECA: ', v['nombre_discoteca'], 'RESEÑA: ', v['texto'], 'ESTRELLAS: ', v['nota']
            temp.append(resultado)
    return temp


def fiestasUsuario(usuario):
    fiestas = db.reference('data/fiestas')
    temp = []
    for k, v in fiestas.get().items():
        if v['usuario'].lower().__contains__(str(usuario)+'·º·'):
            resultado = 'FIESTA: ', v['nombre'], 'ZONA: ', v['zona'], 'CALLE: ', v['calle'], 'NÚMERO: ', v['numero']
            temp.append(resultado)
    return temp


def filtrarDiscotecas(opcion, consulta):
    if opcion == 1:
        # FILTRADO DE ZONA
        discotecas = db.reference('data/discotecas')
        consulta = consulta.lower()
        temp = []
        for k, v in discotecas.get().items():
            if v['zona'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp

    elif opcion == 2:
        # FILTRADO DE NOMBRE
        discotecas = db.reference('data/discotecas')
        consulta = consulta.lower()
        temp = []
        for k, v in discotecas.get().items():
            if v['nombre'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp
    elif opcion == 3:
        # FILTRADO DE CALLE
        discotecas = db.reference('data/discotecas')
        consulta = consulta.lower()
        temp = []
        for k, v in discotecas.get().items():
            if v['calle'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp

    elif opcion == 4:
        # FILTRADO DE VALORACION
        valoraciones = db.reference('data/valoraciones')
        consulta = consulta.lower()
        temp = []
        for k, v in valoraciones.get().items():
            if v['texto'].lower().__contains__(consulta):
                resultado = v['nombre_discoteca']
                temp.append(resultado)
        return temp
    elif opcion == 5:
        # FILTRADO DE NOMBRE DE USUARIO, filtra los usuarios que hay en la base de datos
        usuarios = db.reference('data/usuarios')
        consulta = consulta.lower()
        temp = []
        for k, v in usuarios.get().items():
            if v['usuario'].lower().startswith(consulta):
                resultado = v['usuario']
                temp.append(resultado)
        return temp
