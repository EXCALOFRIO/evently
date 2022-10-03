# pip install git+https://github.com/ozgur/python-firebase
#pip install python-firebase

from firebase import firebase
firebase= firebase.FirebaseApplication(
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


#insertarDiscoteca('cats', 'calle Lavanfa', 22, 'moncloa')
#insertarValoracion('cats', 5, 'muy buena')


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

# crea una funcion que pregunte por que variable de dicoetca quieres filtrar mostrando las opciones de filtrado y te devuelve un diccionario con las discotecas que cumplen con el filtro
# que no importe las mayusculas y minusculas
# que no importe si es una calle o una avenida
# tambien se pueda filtrar por las valoraciones usando el campo nombre_discoteca o por la nota de la valoracion


def filtrarDiscotecas():
    discotecas = firebase.get('/data/discotecas', '')
    print('¿Por que quieres filtrar las discotecas?')
    print('1. Por zona')
    print('2. Por nombre')
    print('3. Por calle')
    print('4. Por valoraciones')
    print('5. Por nota de valoracion')
    filtro = input('Elige una opcion: ')
    if filtro == '1':
        zona = input('Introduce la zona: ')
        for i in discotecas:
            if discotecas[i]['zona'].lower() == zona.lower():
                print(discotecas[i]['nombre'])
    elif filtro == '2':
        nombre = input('Introduce el nombre: ')
        for i in discotecas:
            if discotecas[i]['nombre'].lower() == nombre.lower():
                print(discotecas[i]['nombre'])
    elif filtro == '3':
        calle = input('Introduce la calle: ')
        for i in discotecas:
            if discotecas[i]['calle'].lower() == calle.lower():
                print(discotecas[i]['nombre'])
    elif filtro == '4':
        nombre_discoteca = input('Introduce el nombre de la discoteca: ')
        valoraciones = firebase.get('/data/valoraciones', '')
        for i in valoraciones:
            if valoraciones[i]['nombre_discoteca'].lower() == nombre_discoteca.lower():
                print(valoraciones[i]['nombre_discoteca'])
    elif filtro == '5':
        nota = input('Introduce la nota: ')
        # transforma a int nota
        nota = int(nota)
        valoraciones = firebase.get('/data/valoraciones', '')
        for i in valoraciones:
            if valoraciones[i]['nota'] >= nota:
                print(valoraciones[i]['nombre_discoteca'])

    else:
        print('Opcion incorrecta')


filtrarDiscotecas()
