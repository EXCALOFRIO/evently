import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("firebase/evently-key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://evently-646a2-default-rtdb.firebaseio.com/'
})

def filtrarDiscotecas(opcion, consulta):
    #print("1. Zona")
    #print("2. Nombre")
    #print("3. Calle")
    #print("4. Valoracion")
    #print("5. Nota")
    #opcion = int(input("Introduzca el numero de la opcion que desea: "))
    if opcion == 1:
        #zona = input("Introduzca la zona: ")
        discotecas = db.reference('data/discotecas')
        for i in discotecas.get():
            if discotecas.get()[i]['zona'].lower().startswith(consulta):
                return(discotecas.get()[i]['nombre'])
    elif opcion == 2:
                #nombre = input("Introduzca el nombre: ")
                discotecas = db.reference('data/discotecas')
                for i in discotecas.get():
                    if discotecas.get()[i]['nombre'].lower().startswith(consulta):
                        return(discotecas.get()[i]['nombre'])
    elif opcion == 3:
                #calle = input("Introduzca la calle: ")
                discotecas = db.reference('data/discotecas')
                for i in discotecas.get():
                    if discotecas.get()[i]['calle'].lower().startswith(consulta):
                        return(discotecas.get()[i]['nombre'])
    elif opcion == 4:
                #valoracion = input("Introduzca la valoracion: ")
                valoraciones = db.reference('data/valoraciones')
                for i in valoraciones.get():
                    if valoraciones.get()[i]['texto'].lower().__contains__(consulta):
                        return(valoraciones.get()[i]['nombre_discoteca'])
    elif opcion == 5:
            #ESTA OPCION NO FUNCIONA
            #MODIFICAR
            print("1. Mayor a menor")
            print("2. Menor a mayor")
            opcion = int(input("Introduzca el numero de la opcion que desea: "))
            if opcion == 1:
                valoraciones = db.reference('data/valoraciones')
                lista = []
                for i in valoraciones.get():
                    lista.append(valoraciones.get()[i]['nota'])
                lista.sort(reverse=True)
                print(lista)
            elif opcion == 2:
                valoraciones = db.reference('data/valoraciones')
                lista = []
                for i in valoraciones.get():
                    lista.append(valoraciones.get()[i]['nota'])
                lista.sort()
                print(lista)
                
print(f"Independance Club\nJoy Eslava\nKapital\nMedias Puri\nShoko\nVelvet")

filtrarDiscotecas(1, "centro")

                