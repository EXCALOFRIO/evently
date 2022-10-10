# pip install git+https://github.com/ozgur/python-firebase
# pip install python-firebase

import itertools
import time
import email
from operator import ge
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("firebase/evently-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
})

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


def insertarDiscotecaEficiente(nombre, ubicacion, ruta):
    discotecas = {
        'nombre': nombre,
        'ubicacion': ubicacion
    }
    db.reference(ruta).child('discotecasEficientes').push(discotecas)


def insertarDiscoteca(nombre, zona, calle, numero, ruta):
    discotecas = {
        'nombre': nombre,
        'zona': zona,
        'calle': calle,
        'numero': numero
    }
    db.reference(ruta).child('discotecas').push(discotecas)
    ubicacion = calle + ', ' + str(numero) + ', ' + zona + ', Madrid España'
    ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
        'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c', 'Calle ').replace('av', 'Avenida ').replace('avda', 'Avenida ').replace('c.', 'Calle ').replace('pl', 'Plaza ')
    insertarDiscotecaEficiente(nombre, ubicacion2, ruta)

# crea un metodo que de la base de datos extraiga todos los datos de las discotecas y llame a la funcion insertarDiscotecaEficiente


def insertarDiscotecasEficientes(ruta):
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
        insertarDiscotecaEficiente(nombre, ubicacion2, ruta)


def insertarFiestaEficiente(nombre, ubicacion, ruta):
    fiestas = {
        'nombre': nombre,
        'ubicacion': ubicacion
    }
    db.reference(ruta).child('fiestasEficientes').push(fiestas)


def insertarFiesta(nombre, calle, numero, zona, ruta):
    fiestas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    db.reference(ruta).child('fiestas').push(fiestas)
    ubicacion = calle + ', ' + str(numero) + ', ' + zona + ', Madrid España'
    ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
        'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c', 'Calle ').replace('av', 'Avenida ').replace('avda', 'Avenida ').replace('c.', 'Calle ').replace('pl', 'Plaza ')
    insertarFiestaEficiente(nombre, ubicacion2, ruta)


def insertarValoracion(usuario, nombre_discoteca, nota, texto, ruta):
    valoraciones = {
        'usuario': usuario,
        'nombre_discoteca': nombre_discoteca,
        'nota': nota,
        'texto': texto
    }
    db.reference(ruta).child('valoraciones').push(valoraciones)


def borrarDatos(datos):
    db.reference('test').child(datos).delete()


def getItemBaseDatos(elemento, variable, ruta):
    elemento = db.reference(ruta+'/'+elemento)
    lista = []
    for k, v in elemento.get().items():
        lista.append(v[variable])
    return lista

# crea un metodo que devuelava la key sabiendo la posocion en el array

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


def datosUsuario(datos):
    return usuarioActualSimp[datos]


def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta):
    if usuario in getItemBaseDatos('usuarios', 'usuario', ruta) or email in getItemBaseDatos('usuarios', 'email', ruta) or '@' not in email or '.' not in email or usuario == '' or nombre == '' or apellido == '' or edad == '' or email == '' or contraseña == '':
        print('El usuario o el email ya existen o no ha rellenado todos los campos o el email no es correcto')
        return False
    insertarUsuario(usuario, nombre, apellido,
                    edad, email, contraseña, ruta)
    return True


def comprobarInicioSesion(usuario, contraseña, ruta):
    indice = getItemBaseDatos('usuarios', 'usuario', ruta).index(usuario)
    if getItemBaseDatos('usuarios', 'contraseña', ruta)[indice] == contraseña:
        variableUsuarioSimp(usuario)
        return True
    print('El usuario o la contraseña no son correctos, o no ha rellenado todos los campos')
    return False


def filtrarDiscotecas(opcion, consulta):
    if opcion == 1:
        # FILTRADO DE ZONA
        discotecas = db.reference('data/discotecas')
        temp = []
        for k, v in discotecas.get().items():
            if v['zona'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp

    elif opcion == 2:
        # FILTRADO DE NOMBRE
        discotecas = db.reference('data/discotecas')
        temp = []
        for k, v in discotecas.get().items():
            if v['nombre'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp
    elif opcion == 3:
        # FILTRADO DE CALLE
        discotecas = db.reference('data/discotecas')
        temp = []
        for k, v in discotecas.get().items():
            if v['calle'].lower().startswith(consulta):
                resultado = v['nombre']
                temp.append(resultado)
        return temp

    elif opcion == 4:
        # FILTRADO DE VALORACION
        valoraciones = db.reference('data/valoraciones')
        temp = []
        for k, v in valoraciones.get().items():
            if v['texto'].lower().__contains__(consulta):
                resultado = v['nombre_discoteca']
                temp.append(resultado)
        return temp
