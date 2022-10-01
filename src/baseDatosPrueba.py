# pip install git+https://github.com/ozgur/python-firebase
from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://evently-646a2-default-rtdb.firebaseio.com/", None)


# metodo instertar un nodo en la base de datos usuarios en firebase con los campos usuario,nombre,apellido,edad, email, contraseña


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

# metodo para insertar un nodo en la base de datos discotecas en firebase con los campos nombre, calle, numero y zona


def insertarDiscoteca(nombre, calle, numero, zona):
    discotecas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    firebase.post('/data/discotecas', discotecas)

# metodo para insertar un nodo en la base de datos valoracones en firebase con los campos nombre_discoteca, nota, texto


def insertarValoracion(nombre_discoteca, nota, texto):
    valoraciones = {
        'nombre_discoteca': nombre_discoteca,
        'nota': nota,
        'texto': texto
    }
    firebase.post('/data/valoraciones', valoraciones)


insertarDiscoteca('cats', 'calle Lavanfa', 22, 'moncloa')
insertarValoracion('cats', 5, 'muy buena')
# comprobar mediante un metodo que no se puede insertar un usuario con el mismo nombre de usuario y email


def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña):
    usuarios = firebase.get('/data/usuarios', '')
    for i in usuarios:
        if usuarios[i]['usuario'] == usuario or usuarios[i]['email'] == email:
            print('El usuario ya existe')
            return False
    return insertarUsuario(usuario, nombre, apellido, edad, email, contraseña)


comprobarUsuario('EXCALOFRIO2', 'Alejandro', 'Ramirez',
                 20, 'aleramlar2@gmail.com', 'perro69')
# metodo para leer un nodo en la base de datos discotecas en firebase
# leer = firebase.get('/data/discotecas', '#nodo_de_ejemplo')
# print(leer)

# metodo para devolver el campo nombre de la base de datos discotecas en firebase para todos los nodos


def getNombre():
    discotecas = firebase.get('/data/discotecas', '')
    for i in discotecas:
        print(discotecas[i]['nombre'])


# getNombre()
