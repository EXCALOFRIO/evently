# pip install git+https://github.com/ozgur/python-firebase
# pip install python-firebase

from collections import deque
import itertools
import time
import email
from operator import ge
from tkinter import N
from turtle import color
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="evently")
cred = credentials.Certificate("firebase/evently-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
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
    data = db.reference(ruta).child(elemento).get()
    if data is not None:
        # Use the map() function to extract the desired values from the data
        values = map(lambda x: x[variable], data.values())
        return list(values)  # Convert the values to a list and return it
    else:
        return []


def getTodosLosDatos(elemento, ruta):
    data = db.reference(ruta).child(elemento).get()
    if data is not None:
        return list(data.values())  # Return a list of the values in the data
    else:
        return []


def getDatosElementoConcreto(elemento, variable, dato, elementos, ruta):
    temp = getItemBaseDatos(elemento, variable, ruta)
    pos = temp.index(dato)
    array = []
    for elemen in elementos:
        array.append(getItemBaseDatos(elemento, elemen, ruta)[pos])
    return array


# Metodo de para mostrar la carta de las discotecas
# print(getTodosLosDatos('discotecas', 'data'))
# print(get_Todos_Los_Datos('discotecas', 'data'))


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
    # Comprueba si el email está vacío o no tiene un formato válido
    if not email or '@' not in email or '.' not in email:
        return False
    # Comprueba si algún campo obligatorio está vacío
    if not usuario or not nombre or not apellido or not edad or not contraseña:
        return False
    # Comprueba si el usuario o el email ya existen en la base de datos
    usuarios = getItemBaseDatos('usuarios', 'usuario', ruta)
    emails = getItemBaseDatos('usuarios', 'email', ruta)
    if usuario in usuarios or email in emails:
        return False
    # Inserta la información del usuario en la base de datos
    insertarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta)
    return True


def comprobarInicioSesion(usuario, contraseña, ruta):
    if not usuario or not contraseña:
        return False

    user_data = getTodosLosDatos('usuarios', ruta)

    for user in user_data:
        if user['usuario'] == usuario and user['contraseña'] == contraseña:
            variableUsuarioSimp(usuario)
            variableNombreUsuario(user['nombre'])
            variableApellidoUsuario(user['apellido'])
            variableEmailUsuario(user['email'])
            variableEdadUsuario(user['edad'])
            return True

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
