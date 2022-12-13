from datetime import date
import time
from kivy.clock import Clock
import webbrowser
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem, ThreeLineListItem
from kivy_garden.mapview import MapView
from kivy_garden.mapview import MapMarker
from kivy.uix.image import AsyncImage


from baseDatosPruebaApp import *


class OneLineListItemAligned(OneLineListItem):
    def __init__(self, halign, **kwargs):
        super(OneLineListItemAligned, self).__init__(**kwargs)
        self.ids._lbl_primary.halign = halign


class Ui(ScreenManager):

    usernameText = ''
    nombre = ''
    apellido = ''
    edad = ''
    email = ''

    def botonBusquedaFiltrado(self, texto, textoFiltro):
        if textoFiltro == 'Zona':
            numeroFiltro = 1
        elif textoFiltro == 'Nombre':
            numeroFiltro = 2
        elif textoFiltro == 'Calle':
            numeroFiltro = 3
        elif textoFiltro == 'Valoracion':
            numeroFiltro = 4

        out = filtrarDiscotecas(numeroFiltro, texto)

        self.borrarBusquedaFiltrado()
        for element in out:
            item = OneLineListItem(
                text=str(element), width=300, on_release=lambda x: self.cartaDiscoteca(x.text))
            self.ids.MDListFiltrado.add_widget(item)

    def borrarBusquedaFiltrado(self):
        try:
            self.ids.MDLabelFiltrado.text = ''
            self.ids.MDLabelFiltrado.opacity = 0
            self.ids.MDLabelFiltrado.size_hint = (None, None)
            self.ids.MDLabelFiltrado.size = (0, 0)
            self.ids.MDListFiltrado.clear_widgets()
        except AttributeError:
            pass

    def cartaDiscoteca(self, discoteca):
        self.borrarBusquedaFiltrado()
        print(discoteca)
        carta = mostrar_carta("carta", discoteca, 'data')
        self.ids.MDLabelFiltrado.text = carta
        self.ids.MDLabelFiltrado.opacity = 1
        self.ids.MDLabelFiltrado.font_size = 30
        self.ids.MDLabelFiltrado.size_hint = (1, 1)

    def botonBusquedaChat(self, texto):
        self.ids.other_user_list.clear_widgets()
        self.ids.this_user_list.clear_widgets()
        self.borrarBusquedaChat()
        out = filtrarDiscotecas(5, texto)
        for element in out:
            item = OneLineListItem(
                text=str(element), width=300, on_release=lambda x: self.crearChat(x.text, ''))
            self.ids.MDListFiltradoChat.add_widget(item)

    def crearChat(self, usuario, texto):
        self.ids.scrollChat.scroll_y = 0
        self.ids.message_input.text = texto
        self.ids.other_user_list.clear_widgets()
        self.ids.this_user_list.clear_widgets()
        self.borrarBusquedaChat()
        self.current = 'chatDm'
        self.ids.user_label.text = usuario

        usuario2 = datosUsuario('usuario')
        usuario1 = usuario
        if usuario1 < usuario2:
            chat = usuario1+usuario2
        else:
            chat = usuario2+usuario1

        rutaChat = 'chats/'+chat
        chatsAnteriores = getTodosLosDatos(rutaChat, 'data')
        if chatsAnteriores == []:
            insertarMensaje(
                usuario2, 'Hola, quieres usar Evently conmigo :)', chat, 'data')
        else:
            for chatAnterior in chatsAnteriores:
                if chatAnterior['usuario'] == usuario1:
                    item = OneLineListItemAligned(
                        text=str(chatAnterior['mensaje']), bg_color=('292828'), halign="left")
                    self.ids.other_user_list.add_widget(item)
                    item2 = OneLineListItem(text=str(''), opacity=0)
                    self.ids.this_user_list.add_widget(item2)
                else:
                    item = OneLineListItemAligned(
                        text=str(chatAnterior['mensaje']), bg_color=('b84814'), halign="right")
                    self.ids.this_user_list.add_widget(item)
                    item = OneLineListItem(text=str(''), opacity=0)
                    self.ids.other_user_list.add_widget(item)
            Clock.schedule_once(self.actualizarChat, 5)

        self.ids.scrollChat.scroll_y = 0

        # espera 5 segundos y actualiza el chat

    def pararTimer(self):
        Clock.unschedule(self.actualizarChat)

    def actualizarChat(self, dt):
        self.ids.scrollChat.scroll_y = 0
        self.crearChat(self.ids.user_label.text, self.ids.message_input.text)

    def send_message(self, mensaje, usuario1):
        self.ids.message_input.text = ''
        self.ids.other_user_list.clear_widgets()
        self.ids.this_user_list.clear_widgets()
        if(str(mensaje) != ''):
            usuario2 = datosUsuario('usuario')
            if usuario1 < usuario2:
                chat = usuario1+usuario2
            else:
                chat = usuario2+usuario1
            insertarMensaje(datosUsuario('usuario'),
                            str(mensaje), chat, 'data')
            self.crearChat(usuario1, '')
        else:
            self.crearChat(usuario1, '')

    def borrarBusquedaChat(self):
        try:
            self.ids.MDListFiltradoChat.clear_widgets()
        except AttributeError:
            pass

    def generate_markers(self):
        loc = getTodosLosDatos('discotecasEficientes', 'data')
        locFiestas = getTodosLosDatos('fiestasEficientes', 'data')
        for location in loc:
            marker = MapMarker(
                lat=location['latitud'], lon=location['longitud'])
            marker.marker_name = location['nombre']+','+location['ubicacion']

            # Función que se ejecutará al presionar el marcador

            def open_location(marker):
                # Abrir el navegador en la ubicación del marcador
                url = f'https://www.google.com/maps/search/?api=1&query={marker.lat},{marker.lon}'
                query = marker.marker_name
                url2 = f"https://www.google.com/maps/search/?api=1&query={query}"
                webbrowser.open(url2)
                print(url)
                print(url2)

            marker.bind(on_release=open_location)
            self.ids.mapview.add_marker(marker)

        for locationF in locFiestas:
            marker2 = MapMarker(
                lat=locationF['latitud'], lon=locationF['longitud'], color=(
                    0, 0, 1, 1))
            marker2.marker_name = locationF['nombre'] + \
                ','+locationF['ubicacion']

            def open_location2(marker2):
                # Abrir el navegador en la ubicación del marcador
                url = f'https://www.google.com/maps/search/?api=1&query={marker.lat},{marker.lon}'
                query = marker2.marker_name
                url2 = f"https://www.google.com/maps/search/?api=1&query={query}"
                webbrowser.open(url2)
                print(url)
                print(url2)

            marker2.bind(on_release=open_location2)
            self.ids.mapview.add_marker(marker2)
        self.current = 'Mapa'

    def inicioSesion(self, usuario, password):
        # self.current = 'screen_principal'
        # QUITAR LOS COMENTARIOS PARA QUE FUNCIONE EL LOGIN Y REGISTRO
        if comprobarInicioSesion(usuario, password, 'data'):
            print("hola")

            datos = getTodosLosDatos('usuarios', 'data')
            username = datosUsuario('usuario')
            for dato in datos:
                if dato['usuario'] == username:
                    self.nombre = dato['nombre']
                    self.apellido = dato['apellido']
                    self.edad = dato['edad']
                    self.email = dato['email']

            self.usernameText = datosUsuario('usuario')
            self.current = 'screen_principal'
        else:
            self.ids.signal_login.text = 'Usuario o contraseña incorrectos'

    def agregar_usuario(self, ap, cont, ed, mail, nombre, usuario):
        resultado = comprobarUsuario(
            usuario, nombre, ap, ed, mail, cont, 'data')

        if resultado == True:
            self.ids.error_registro.text = ("Usuario registrado correctamente")
            self.current = 'login'
        elif resultado == False:
            self.ids.error_registro.text = "El usuario ya existe"
        else:
            errorText = ''
            for error in resultado:
                errorText = errorText+error+' '
            self.ids.error_registro.text = "Los siguientes campos están incompletos: "+errorText

    def cargarDatos(self):
        self.ids.userText.text = self.usernameText
        self.ids.nombre.text = self.nombre
        self.ids.apellido.text = self.apellido
        self.ids.edad.text = str(self.edad)
        self.ids.email.text = self.email

    def borrarBusquedaUsuario(self):
        try:
            self.ids.MDListBuscadorUsuarios.clear_widgets()
        except AttributeError:
            pass

    def dataUsuarioBuscado(self, usuario):
        datos = getTodosLosDatos('usuarios', 'data')
        for dato in datos:
            if dato['usuario'] == usuario:
                self.ids.userTextUsuarioBuscado.text = usuario
                self.ids.nombreTextUsuarioBuscado.text = dato['nombre']
                self.ids.apellidoTextUsuarioBuscado.text = dato['apellido']
                self.ids.edadTextUsuarioBuscado.text = str(dato['edad'])
                self.ids.emailTextUsuarioBuscado.text = dato['email']
        self.current = 'datosUsuarioBuscado'

    def botonBusquedaUsuarios(self, texto):
        self.borrarBusquedaUsuario()
        out = filtrarDiscotecas(5, texto)
        for element in out:
            item = OneLineListItem(
                text=str(element), width=300, on_release=lambda x: self.dataUsuarioBuscado(x.text))
            self.ids.MDListBuscadorUsuarios.add_widget(item)

    def borrarBusquedaFiltradoResenas(self):
        try:
            self.ids.MDLabelFiltradoRsenaUno.text = ''
            self.ids.MDLabelFiltradoRsenaUno.opacity = 0
            self.ids.MDLabelFiltradoRsenaUno.size_hint = (None, None)
            self.ids.MDLabelFiltradoRsenaUno.size = (0, 0)
            self.ids.MDLabelFiltradoRsenaDos.text = ''
            self.ids.MDLabelFiltradoRsenaDos.opacity = 0
            self.ids.MDLabelFiltradoRsenaDos.size_hint = (None, None)
            self.ids.MDLabelFiltradoRsenaDos.size = (0, 0)
            self.ids.MDLabelFiltradoRsenaTres.text = ''
            self.ids.MDLabelFiltradoRsenaTres.opacity = 0
            self.ids.MDLabelFiltradoRsenaTres.size_hint = (None, None)
            self.ids.MDLabelFiltradoRsenaTres.size = (0, 0)
            self.ids.MDListFiltradoResena.clear_widgets()
        except AttributeError:
            pass

    def botonBusquedaFiltradoResenas(self, texto, textoFiltro):
        self.borrarBusquedaFiltradoResenas()
        if textoFiltro == 'Nombre':
            numeroFiltro = 6
        elif textoFiltro == 'Usuario':
            numeroFiltro = 7
        elif textoFiltro == 'Valoración':
            numeroFiltro = 8
        elif textoFiltro == 'Nota':
            numeroFiltro = 9

        out = filtrarDiscotecas(numeroFiltro, texto)

        self.borrarBusquedaFiltradoResenas()
        for element in out:
            item = ThreeLineListItem(
                text=str(element[0]), secondary_text=str(element[3]+': '+element[2]), tertiary_text=str('Nota:'+str(element[1])+' Fecha:'+str(element[4])), width=300, on_release=lambda x: self.resenaFocus(x.text, x.secondary_text, x.tertiary_text))
            self.ids.MDListFiltradoResena.add_widget(item)

    def resenaFocus(self, texto1, texto2, texto3):
        self.borrarBusquedaFiltradoResenas()
        self.ids.MDListFiltradoResena.clear_widgets()
        self.ids.MDLabelFiltradoRsenaUno.text = texto1
        self.ids.MDLabelFiltradoRsenaUno.opacity = 1
        self.ids.MDLabelFiltradoRsenaUno.size_hint = (1, 1)
        self.ids.MDLabelFiltradoRsenaDos.text = texto3
        self.ids.MDLabelFiltradoRsenaDos.opacity = 1
        self.ids.MDLabelFiltradoRsenaDos.size_hint = (1, 1)
        self.ids.MDLabelFiltradoRsenaTres.text = texto2
        self.ids.MDLabelFiltradoRsenaTres.opacity = 1
        self.ids.MDLabelFiltradoRsenaTres.size_hint = (1, 1)

    def cargarDiscotecasSpinner(self):
        discotecas = getItemBaseDatos('discotecas', 'nombre', 'data')
        for discoteca in discotecas:
            self.ids.discoteca.values.append(discoteca)
        self.ids.discoteca.text = discotecas[0]
        self.current = 'annadirReseñaScreen'

    def annadirReseña(self, discoteca, estrellas, texto):
        if discoteca == '' or estrellas == '' or texto == '':
            self.ids.error.text = 'Rellena todos los campos'
            self.ids.error.opacity = 1
            self.ids.error.size_hint = (1, 1)
        else:
            fecha_actual = date.today().strftime("%d/%m/%Y")
            usuario = datosUsuario('usuario')
            if(comprobarValoracion(fecha_actual, usuario, discoteca, 'data')):
                insertarValoracion(fecha_actual, usuario,
                                   discoteca, estrellas, texto, 'data')
                self.current = 'reseña'
            else:
                self.ids.error.text = 'Ya has valorado esta discoteca, espera 24 horas para volver a valorarla'
                self.ids.error.opacity = 1
                self.ids.error.size_hint = (1, 1)

    def botonAñadirDiscoteca(self, nombre, zona, calle, numero):
        self.ids.MDLabelAñadirDiscoteca.text = 'Añadir discoteca'
        # comprueba que devuelve el insertarDiscoteca, si devuelve un array imprimir un error en la pantalla, si devuelve false otra cosa
        resultado = insertarDiscoteca(nombre, calle, numero, zona, 'data')
        if(resultado == False):
            self.ids.MDLabelAñadirDiscoteca.text = 'No se puede obtener la localización de la discoteca'
            self.ids.MDLabelAñadirDiscoteca.color = (1, 0, 0, 1)
        elif(resultado == True):
            self.ids.MDLabelAñadirDiscoteca.text = 'Se ha añadido la discoteca correctamente'
            self.ids.MDLabelAñadirDiscoteca.color = (1, 1, 1, 1)
        else:
            errorText = ''
            for error in resultado:
                errorText = errorText+error+' '
            self.ids.MDLabelAñadirDiscoteca.text = 'Los siguientes campos estan sin completar: '+errorText+'.'
            self.ids.MDLabelAñadirDiscoteca.color = (1, 0, 0, 1)

        self.ids.MDTextFieldNombreDiscoteca.text = ''
        self.ids.MDTextFieldZonaDiscoteca.text = ''
        self.ids.MDTextFieldCalleDiscoteca.text = ''
        self.ids.MDTextFieldNumeroDiscoteca.text = ''

    def botonAñadirFiesta(self, nombre, zona, calle, numero):
        usuarioFiesta = datosUsuario('usuario')
        self.ids.MDLabelFiesta.text = 'Añadir discoteca'
        # comprueba que devuelve el insertarDiscoteca, si devuelve un array imprimir un error en la pantalla, si devuelve false otra cosa
        resultado = insertarFiesta(
            nombre, calle, numero, zona, usuarioFiesta, 'data')
        if(resultado == False):
            self.ids.MDLabelFiesta.text = 'No se puede obtener la localización de la fiesta'
            self.ids.MDLabelFiesta.color = (1, 0, 0, 1)
        elif(resultado == True):
            self.ids.MDLabelFiesta.text = 'Se ha añadido la fiesta correctamente'
            self.ids.MDLabelFiesta.color = (1, 1, 1, 1)
        else:
            errorText = ''
            for error in resultado:
                errorText = errorText+error+' '
            self.ids.MDLabelFiesta.text = 'Los siguientes campos estan sin completar: '+errorText+'.'
            self.ids.MDLabelFiesta.color = (1, 0, 0, 1)

        self.ids.MDTextFieldNombre.text = ''
        self.ids.MDTextFieldZona.text = ''
        self.ids.MDTextFieldCalle.text = ''
        self.ids.MDTextFieldNumero.text = ''

    def cargarImagenes(self):
        self.ids.gridGallery.clear_widgets()
        imgArray = ver_mis_fotos(datosUsuario('usuario'))
        # por cada imagen en el array de imagenes añadir a gridGallery una imagen
        for imgUrl in imgArray:
            img = AsyncImage(source=imgUrl, keep_ratio=True,
                             allow_stretch=True)
            img.size_hint_y = None
            self.ids.gridGallery.add_widget(img)
        print(imgArray)

    def cargarImagenes2(self, user):
        self.current = 'galeria2'
        self.ids.gridGallery2.clear_widgets()
        imgArray = ver_mis_fotos(user)
        # por cada imagen en el array de imagenes añadir a gridGallery una imagen
        for imgUrl in imgArray:
            img = AsyncImage(source=imgUrl, keep_ratio=True,
                             allow_stretch=True)
            img.size_hint_y = None
            self.ids.gridGallery2.add_widget(img)
        print(imgArray)

        
    def clear_signal(self):
        self.ids.signal_register.text = ''
        self.ids.signal_login.text = ''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'DeepOrange'
        Builder.load_file('design.kv')

        return Ui()

    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'


if __name__ == '__main__':
    MainApp().run()
