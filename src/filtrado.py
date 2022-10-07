import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


def filtrarDiscotecas(opcion, consulta):

    if opcion == 1:
        # FILTRADO DE ZONA
        discotecas = db.reference('data/discotecas')
        temp = []
        for i in discotecas.get():
            if discotecas.get()[i]['zona'].lower().startswith(consulta):
                resultado = (discotecas.get()[i]['nombre'])
                temp.append(resultado)
        return temp

    elif opcion == 2:
        # FILTRADO DE NOMBRE
        discotecas = db.reference('data/discotecas')
        for i in discotecas.get():
            if discotecas.get()[i]['nombre'].lower().startswith(consulta):
                return(discotecas.get()[i]['nombre'])
    elif opcion == 3:
        # FILTRADO DE CALLE
        discotecas = db.reference('data/discotecas')
        for i in discotecas.get():
            if discotecas.get()[i]['calle'].lower().startswith(consulta):
                return(discotecas.get()[i]['nombre'])
    elif opcion == 4:
        # FILTRADO DE VALORACION
        valoraciones = db.reference('data/valoraciones')
        for i in valoraciones.get():
            if valoraciones.get()[i]['texto'].lower().__contains__(consulta):
                return(valoraciones.get()[i]['nombre_discoteca'])
    elif opcion == 5:
        # ESTA OPCION NO FUNCIONA
        # MODIFICAR
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

