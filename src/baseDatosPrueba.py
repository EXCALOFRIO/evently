# pip install git+https://github.com/ozgur/python-firebase
from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://evently-646a2-default-rtdb.firebaseio.com/", None)


# metodo para insertar un nodo en la base de datos discotecas en firebase con los campos nombre, calle, numero y zona
def insertarDiscoteca(nombre, calle, numero, zona):
    discotecas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    firebase.post('/data/discotecas', discotecas)

insertarDiscoteca('cats', 'calle Lavanfa', 22, 'moncloa')
# metodo para leer un nodo en la base de datos discotecas en firebase
# leer = firebase.get('/data/discotecas', '#nodo_de_ejemplo')
# print(leer)

# metodo para devolver el campo nombre de la base de datos discotecas en firebase para todos los nodos


def getNombre():
    discotecas = firebase.get('/data/discotecas', '')
    for i in discotecas:
        print(discotecas[i]['nombre'])


getNombre()
