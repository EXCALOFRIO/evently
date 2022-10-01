# pip install git+https://github.com/ozgur/python-firebase
from firebase import firebase
firebase = firebase.FirebaseApplication(
    "https://evently-646a2-default-rtdb.firebaseio.com/", None)


# metodo para insertar un nodo en la base de datos discotecas en firebase
discotecas = {
    'nombre': 'BH',
    'calle': 'Calle de la Palma',
    'numero': 0,
    'zona': 'Centro'
}

# manda el push del dato a la base de datos
result = firebase.post('/data/discotecas', discotecas)

# metodo para leer un nodo en la base de datos discotecas en firebase
# leer = firebase.get('/data/discotecas', '#nodo_de_ejemplo')
# print(leer)

# metodo para devolver el campo nombre de la base de datos discotecas en firebase para todos los nodos


def getNombre():
    discotecas = firebase.get('/data/discotecas', '')
    for i in discotecas:
        print(discotecas[i]['nombre'])


getNombre()
