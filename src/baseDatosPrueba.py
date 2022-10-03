# pip install git+https://github.com/ozgur/python-firebase
# pip install python-firebase

import re
from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://evently-646a2-default-rtdb.firebaseio.com/", None)

##############################################################################
#METODOS PARA INSERTAR LOS DIFERENTES DATOS EN LAS TABLAS DE LA BASE DE DATOS#
##############################################################################


def insertarUsuario(usuario, nombre, apellido, edad, email, contraseña):
    usuarios = {
        'usuario': usuario,
        'nombre': nombre,
        'apellido': apellido,
        'edad': edad,
        'email': email,
        'contraseña': contraseña
    }
    firebase.post('/data/usuarios', usuarios)


def insertarDiscoteca(nombre, calle, numero, zona, codigo_postal):
    discotecas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona,
        'codigo_postal': codigo_postal
    }
    firebase.post('/data/discotecas', discotecas)


def insertarFiesta(nombre, calle, numero, zona, codigo_postal):
    fiestas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona,
        'codigo_postal': codigo_postal
    }


def insertarValoracion(usuario, nombre_discoteca, nota, texto):
    valoraciones = {
        'usuario': usuario,
        'nombre_discoteca': nombre_discoteca,
        'nota': nota,
        'texto': texto
    }
    firebase.post('/data/valoraciones', valoraciones)

################################################################
#METODO PARA COMPROBAR SI EL USUARIO EXISTE EN LA BASE DE DATOS#
################################################################


def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña):
    usuarios = firebase.get('/data/usuarios', '')
    for i in usuarios:
        if usuarios[i]['usuario'] == usuario or usuarios[i]['email'] == email:
            print('El usuario ya existe')
            return False

    insertarUsuario(usuario, nombre, apellido, edad, email, contraseña)
    return True

# metodo comprueba que el usuario y la contraseña son correctos


def comprobarInicioSesion(usuario, contraseña):
    usuarios = firebase.get('/data/usuarios', '')
    for i in usuarios:
        if usuarios[i]['usuario'] == usuario and usuarios[i]['contraseña'] == contraseña:
            print('Inicio de sesion correcto, bienvenido: ', usuario)
            return True
    print('El usuario o la contraseña son incorrectos')
    return False


#comprobarUsuario('EXCALOFRIO2', 'Alejandro', 'Ramirez',20, 'aleramlar2@gmail.com', 'perro69')

# metodo para leer un nodo en la base de datos discotecas en firebase
# leer = firebase.get('/data/discotecas', '#nodo_de_ejemplo')
# print(leer)

# metodo para devolver el campo nombre de la base de datos discotecas en firebase para todos los nodos


def getNombre():
    discotecas = firebase.get('/data/discotecas', '')
    for i in discotecas:
        print(discotecas[i]['nombre'])


# getNombre()

# metodo para iniciar sesion, pide el usuario y la contraseña y comprueba si existe en la base de datos
def inicioSesion(usuario, contraseña):
    usuarios = firebase.get('/data/usuarios', '')
    for i in usuarios:
        if usuarios[i]['usuario'] == usuario and usuarios[i]['contraseña'] == contraseña:
            print('Inicio de sesion correcto, bienvenido: ',
                  usuarios[i]['usuario'])
            return True
    print('El usuario o la contraseña son incorrectos')
    return False

# metodo para añadir a la base de datos,tiene que preguntar que queremos añadir y los campos a añadir
# tiene que comprobar que no se puede añadir un usuario con el mismo nombre de usuario y email usando la funcion comprobarUsuario


def añadir():
    print('¿Que quieres añadir?')
    print('1. Discoteca')
    print('2. Usuario')
    print('3. Valoracion')
    print('4. Fiesta')
    opcion = input('Elige una opcion: ')
    if opcion == '1':
        nombre = input('Introduce el nombre: ')
        calle = input('Introduce la calle: ')
        zona = input('Introduce la zona: ')
        codigo_postal = input('Introduce codigo postal')
        insertarDiscoteca(nombre, calle, zona, codigo_postal)
    elif opcion == '2':
        usuario = input('Introduce el usuario: ')
        nombre = input('Introduce el nombre: ')
        apellido = input('Introduce el apellido: ')
        edad = input('Introduce la edad: ')
        email = input('Introduce el email: ')
        contraseña = input('Introduce la contraseña: ')
        comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña)
    elif opcion == '3':
        nombre_discoteca = input('Introduce el nombre de la discoteca: ')
        nota = input('Introduce la nota: ')
        texto = input('Introduce el texto: ')
        insertarValoracion(nombre_discoteca, nota, texto)
    elif opcion == '4':

        nombre = input('Introduce el nombre: ')
        calle = input('Introduce la calle: ')
        zona = input('Introduce la zona: ')
        codigo_postal = input('Introduce el codigo postal')
        insertarFiesta(nombre, calle, zona, codigo_postal)
    else:
        print('Opcion incorrecta')

# añadir()
