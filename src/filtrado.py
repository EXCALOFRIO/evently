import sys
import MySQLdb

opciones = "Presiona 1 para comenzar el filtrado \nPresiona 2 para ver las opciones de filtrado \nRespuesta: "
op_filtrado = "zona"
print('HAS ENTRADO AL FILTRADO DE DISCOTECAS\n')

paso = 1
if paso == 1:
    print(opciones)
    opcion = input()
    print(opcion)
    if opcion == "1":
        paso = 2
    if opcion == "2":
        paso = 3
    if opcion < "1" or opcion > "3":
        paso = 4
elif paso == 2:
    print("Que quieres filtrar: ")
    filtrado = input()

    try:
        db = MySQLdb.connect("localhost", "alberto", "ADTduty_45", "evently")
    except MySQLdb.Error as e:
        print("No puedo conectar a la base de datos:", e)
        sys.exit(1)
    print("Conexión correcta.")

    # Para hacer alguna consulta
    cursor = db.cursor()
    cursor.execute("select " + filtrado + " from dicotecas")
    for consulta in cursor:
        print(consulta)
    db.close()

elif paso == 3:
    print("estoy en el paso {}".format(paso))
    print("Las opciones que tienes para filtrar son: \n{}".format(op_filtrado))
    paso = 1
    print("Paso al paso {}".format(paso))

elif paso == 4:
    print("seleccione la opcion correcta")
    paso = 1
