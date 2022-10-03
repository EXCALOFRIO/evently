from firebase import firebase
firebase= firebase.FirebaseApplication(
    "https://evently-646a2-default-rtdb.firebaseio.com/", None)

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
        if discotecas[i]['zona'].lower().startswith(zona.lower()): #Me busca en la BBDD todos aquellos inserts que empiecen por la palabra introducida 
            print(discotecas[i]['nombre'])
elif filtro == '2':
    nombre = input('Introduce el nombre: ')
    for i in discotecas:
        if discotecas[i]['nombre'].lower().startswith(nombre.lower()):
            print(discotecas[i]['nombre'])
elif filtro == '3':
    calle = input('Introduce la calle: ')
    for i in discotecas:
        if discotecas[i]['calle'].lower().startswith(calle.lower()):
            print(discotecas[i]['nombre'])
elif filtro == '4':
    nombre_discoteca = input('Introduce el nombre de la discoteca: ')
    valoraciones = firebase.get('/data/valoraciones', '')
    for i in valoraciones:
        if valoraciones[i]['nombre_discoteca'].lower().startswith(nombre_discoteca.lower()):
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