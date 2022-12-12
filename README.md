# Eventos y discotecas

## Instalación APP

![QR](qr.png)

#### Requisitos

##### Instalar Python 3.10

###### Comando para instalar Python 3.10

-Windows

```python
choco install python
```

-Linux

```python
sudo apt install python3.10
```

-Mac

```python
brew install python3.10
```

##### Instalar pip

###### Comando para instalar pip

-Windows

```python
python -m pip install --upgrade pip
```

-Linux

```python
sudo apt install python3-pip
```

-Mac

```python
brew install pip
```

```python
pip install pyglet
pip install firebase-admin
pip install PyQt5
pip install branca
pip install Jinja2
pip install requests
pip install folium
pip install geopy
pip install pywebview
pip3 install opencv-python
pip install imutils
pip install PySide2
pip install Pyrebase4
pip install kivymd
pip install kivy
pip install mapview
garde install mapview
```

## EXPLICACIÓN METODOS

### Insertar usuario a la base de datos

##### Se comprueba que el usuario no exista en la base de datos, si no existe se inserta al usuario en la base de datos llamando al metodo insertarUsuario.

##### El argumento ruta, sirve para especificar si queremos insertar un usuario en la base de datos [data] o si lo queremos insertar en [test] para hacer pruebas.

```python
    def comprobarUsuario(usuario, nombre, apellido, edad, email, contraseña, ruta):
    if usuario in getItemBaseDatos('usuarios', 'usuario', ruta) or email in getItemBaseDatos('usuarios', 'email', ruta) or '@' not in email or '.' not in email or usuario == '' or nombre == '' or apellido == '' or edad == '' or email == '' or contraseña == '':
        print('El usuario o el email ya existen o no ha rellenado todos los campos o el email no es correcto')
        return False
    insertarUsuario(usuario, nombre, apellido,
                    edad, email, contraseña, ruta)
    return True
```

#### Insertar usuario a la base de datos

```python
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

```

### Inicio de sesión

##### Se comprueba que el usuario exista en la base de datos con el metodo comprobarInicioSesion.

```python
    def comprobarInicioSesion(usuario,      contraseña, ruta):
    if usuario == '' or contraseña == '':
        print('Todos los campos deben estar completos.')
        return False
    indice = getItemBaseDatos('usuarios', 'usuario', ruta).index(usuario)
    if getItemBaseDatos('usuarios', 'contraseña', ruta)[indice] == contraseña:
        variableUsuarioSimp(usuario)
        return True
    print('El usuario o la contraseña no son correctos, o no ha rellenado todos los campos')
    return False
```

##### Si es correcto el usuario y la contraseña se llama al metodo variableUsuarioSimp para guardar el usuario en una variable global y asi poderlo usar más adelante.

```python
    def variableUsuarioSimp(usuario):
    global usuarioSimp
    usuarioSimp = usuario
```

### Insertar Discoteca a la base de datos

##### Se llama al metodo insertarDiscoteca para insertar la discoteca en la base de datos. Se vuelve a usar el argumento ruta para la misma funcion antes mencionada. Creamos un String llamado ubicacion que combina los campos calle, numero y zona, para asi generar correctamente y de forma más eficiente las coordenadas. Para generar las coordenadas usamos la libreria geolocator.

###### Ejemplo de codigo.

```python
location = geolocator.geocode(ubicacion2)
```

```python
    def insertarDiscoteca(nombre, calle, numero, zona, ruta):
    discotecas = {
        'nombre': nombre,
        'calle': calle,
        'numero': numero,
        'zona': zona
    }
    db.reference(ruta).child('discotecas').push(discotecas)
    ubicacion = calle + ', ' + str(numero) + ', ' + zona + ', Madrid España'
    ubicacion2 = ubicacion.replace('C ', 'Calle ').replace('Av ', 'Avenida ').replace(
        'Avda ', 'Avenida ').replace('C.', 'Calle ').replace('PL ', 'Plaza ').replace('c', 'Calle ').replace('av', 'Avenida ').replace('avda', 'Avenida ').replace('c.', 'Calle ').replace('pl', 'Plaza ')

    location = geolocator.geocode(ubicacion2)
    insertarDiscotecaEficiente(
        nombre, ubicacion2, location.longitude, location.latitude, ruta)

```

##### Se llama al metodo insertarDiscotecaEficiente para insertar la discoteca en la base de datos de forma eficiente, es decir, con las coordenadas ya generadas, para luego generar el mapa. Se vuelve a usar el argumento ruta para la misma funcion antes mencionada.

```python
    def insertarDiscotecaEficiente(nombre, ubicacion, longitud, latitud, ruta):
    discotecas = {
        'nombre': nombre,
        'ubicacion': ubicacion,
        'longitud': longitud,
        'latitud': latitud
    }
    db.reference(ruta).child('discotecasEficientes').push(discotecas)
```

### Requisitos para el proyecto

- [ ] Crear un repositorio para garantizar el control de versiones.
- [ ] Crear una guia que explique el proyecto.
- [ ] Crear un servicio donde puedas añadir a tus amigos a la aplicación
- [ ] Crear un mapa donde se pueda ver todas las discoteca y eventos que tienes cerca de ti y donde se encuentran las personas a las que tengas agregadas a la aplicación
- [ ] Crear un algoritmo que te genere la mejor ruta y la más fácil para llegar a tu destino teniendo en cuenta tanto transporte público como coche como otros medios de transporte (uber, cabyfy ...)
- [ ] Crear un servicio de mensajería para la comunicación entre los usuarios
- [ ] Crear un servicio de valoración tanto para los locales como para los usuarios
- [ ] Crear un medio para poder sacar desde la misma aplicación las entradas a las discotecas
- [ ] Crear un servicio donde se puedan hacer solicitudes para participar en eventos particulares creados por otros usuarios
- [ ] Crear un servicio donde aparezcan todos los eventos creados por otras personas
- [ ] Crear un servicio donde aparezcan todas las dicotecas donde exista la posibilidad de realizar filtros (mayor cantidad de personas, cercanía mejor valoración ...)
- [ ] Crear un medio donde puedas ver más o menos la cantidad de gente que hay
- [ ] Crear un servicio donde la gente ponga a disposición su coche para ir a discotecas o eventos
- [ ] Crear un servicio donde la gente pueda subir fotos desde dentro del local
- [ ] Crear un servicio de notificaciones sobre cierta información de las discotecas o de la creación de eventos de tus amigos
- [ ] Crear un servicio de comentarios en directo dentro de cada discoteca para que te puedas comunicar
- [ ] Creación de servicio donde aparezcan todos los perfiles de las personas que están en la discoteca que tengan la aplicación (como un tinder adaptado a la aplicación)
- [ ] Crear un servicio de cartera donde los usuarios puedan meter dinero en la app para pagar directamente desde la app las entradas a los locales

### Criterios de validación

- [ ] Crear un repositorio en el cual el cliente pueda entrar y ver todos los cambios
- [ ] La guía debe contener todos los requisitos y todos los criterios de validación bien detallados
- [ ] La aplicación debe ser capaz de conectar cuentas de distintos usuarios mediante el sistema de amigos, la interfaz debe de ser lo más sencilla para el usuario
- [ ] La aplicación debe ser capaz de crear un evento permitiendo invitación de amigos ya sea el evento tanto público como privado
- [ ] La aplicación debe ser capaz de crear un evento al que se puedan unir usuarios fuera de la lista de amigos, siempre que dicho evento sea público
- [ ] La aplicación debe ser capaz de distinguir a la hora de crear eventos entre públicos y privados
- [ ] El sistema de mensajería ha de ser eficaz, confiable y casi instantáneo
- [ ] Proporcionar un servicio de alquiler de plazas en un coche así como el pago del mismo
- [ ] La aplicación de tener un mapa donde aparezcan la localización de tus amigos
- [ ] El mapa debe tener opciones de búsqueda de: Discotecas y de eventos por separado
- [ ] La aplicación debe ser capaz de poder realizar transacciones correctamente
- [ ] La aplicación debe ser capaz de encontrar el camino objetivamente más corto al sitio al que el usuario queire legar
- [ ] La aplicación debe ser capaz de filtrar según las características de la discoteca
- [ ] El sistema de valoración de las discotecas se hará mediante estrellitas y podrán votar de 0 a 5 estrellitas una vez por usuario teniendo la opción de poder editar su valoración y con la opción de poder dejar o no un comentario de su experiencia
- [ ] Dentro de cada discoteca habrá una interfaz donde podrás sacar las entradas en esa interfaz aparecerán el número de entradas que quieres compras, el precio unitario de cada entrada y el precio final
- [ ] La aplicación debe haber un apartado donde aparezcan todos los eventos creados por otras personas y un botón donde aparezca la opción de poder solicitar la entrada a dicho evento
- [ ] En el mapa debe haber en todo momento la cantidad de gente que hay en la discoteca representado por colores: verde = poca gente, amarillo = bastante gente, rojo = lleno
- [ ] Dentro de la aplicación debe haber un lugar llamado "social" donde cada usuario debe poder subir fotos e historias desde dentro de la discoteca
- [ ] Las notificaciones de la aplicación deben aparecer como un pop-up desde la parte superior de la aplicación ese pop-up estará acompañado de un sonido de notificación
- [ ] Dentro de cada discoteca habrá un apartado de "chat" donde cualquier usuario puede escribir por dicho chat en directo
- [ ] En la interfaz del chat arriba del todo aparecerá unas luces intermitentes de "discoteca" para saber que el chat está activo
- [ ] Se tendrá que crear una sección denominada "perreo" en esa sección aparecerán de uno en uno los usuarios que hay en dicha discoteca que tengan la aplicación. Ahi si desplazas la foto a la izquierda rechazas a la persona y si la desplazas a la derecha la aceptas. En el momento en que dos usuarios se acepten mutuamente se les notificará y se abrirá un chat exclusivo para dichas personas de forma automática

### Descripción del proyecto

- [ ] Crear una aplicación movil que permita a los usuarios ver los eventos y discotecas disponibles y la creación de eventos privados o públicos.

### KIVY DEBUG

- Hay que tener instalado el ADB de Android Studio
- Con esto nos muestra los errores de Kivy

#### WINDOWS

```shell
	adb devices
	adb disconnect 172.22.63.148:5555
	adb tcpip 5555
```

#### UBUNTU

```shell
	adb connect 192.168.31.143:5555
	adb devices
	adb -s 192.168.31.143:5555 logcat *:S python:D
```

### Autores

- `<span style="color:grey">`**@serenablanco -> Serena Blanco García**
- `<span style="color:grey">`**@Daguerre45 -> Alberto Daguerre Torres**
- `<span style="color:grey">`**@EXCALOFRIO -> Alejandro Ramírez Larena**
- `<span style="color:grey">`**@pblrvo -> Pablo Rivero**
- `<span style="color:grey">`**@juaki0315 -> Joaquin Moreno Guzman**
