# pip install git+https://github.com/ozgur/python-firebase
# pip install python-firebase

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


def insertarDiscoteca(nombre, zona, calle, numero, ruta):
    discotecas = {
        'nombre': nombre,
        'zona': zona,
        'calle': calle,
        'numero': numero
    }
    db.reference(ruta).child('discotecas').push(discotecas)


def insertarFiesta(nombre, calle, numero, zona, ruta):
    fiestas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    db.reference(ruta).child('fiestas').push(fiestas)


def insertarValoracion(usuario, nombre_discoteca, nota, texto, ruta):
    valoraciones = {
        'usuario': usuario,
        'nombre_discoteca': nombre_discoteca,
        'nota': nota,
        'texto': texto
    }
    db.reference(ruta).child('valoraciones').push(valoraciones)

################################################################
#METODO PARA COMPROBAR SI EL USUARIO EXISTE EN LA BASE DE DATOS#
################################################################


def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta):

    usuarios = db.reference('data/usuarios')
    # comprueba que no estan en uso ni el usuario y el email introducidos por el usuario estan en la base de datos y tambien q los campos no esten vacios
    for i in usuarios.get():
        if usuarios.get()[i]['usuario'] == usuario:
            print('El usuario ya existe')
            return False
        elif usuarios.get()[i]['email'] == email:
            print('El email ya existe')
            return False
        elif usuario == '' or nombre == '' or apellido == '' or edad == '' or email == '' or contraseña == '':
            print('No puede haber campos vacios')
            return False
        # comprobar que el email esta en buen formato con el @ y el . email
        elif '@' not in email or '.' not in email:
            print('El email no es correcto')
            return False
    insertarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta)
    return True


def comprobarInicioSesion(usuario, contraseña, ruta):
    # añade el valor de ruta a /usuarios
    rutaDatabase = ruta + '/usuarios'
    usuarios = db.reference(rutaDatabase)
    # comprobar para cada usuario si el usuario y la contraseña son correctos
    if usuario == '':
        print('Necesita indicar el usuario')
        return False
    elif contraseña == '':
        print('Necesita escribir la contraseña')
        return False

    for i in usuarios.get():
        if usuarios.get()[i]['usuario'] == usuario and usuarios.get()[i]['contraseña'] == contraseña:
            print('Inicio de sesion correcto, bienvenido: ',
                  usuarios.get()[i]['usuario'])
            return True
    print('El usuario o la contraseña son incorrectos')
    return False
