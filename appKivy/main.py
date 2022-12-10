from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem


from baseDatosPruebaApp import *


class Ui(ScreenManager):
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
        self.ids.MDLabelFiltrado.size_hint = (1, 1)

    def botonBusquedaChat(self, texto):
        self.borrarBusquedaChat()
        out = filtrarDiscotecas(5, texto)
        for element in out:
            item = OneLineListItem(
                text=str(element), width=300, on_release=lambda x: self.crearChat(x.text))
            self.ids.MDListFiltradoChat.add_widget(item)

    def crearChat(self, usuario):
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
                    item = OneLineListItem(
                        text=str(chatAnterior['mensaje']), bg_color=('FF5A1E'))
                    self.ids.other_user_list.add_widget(item)
                    item2 = OneLineListItem(text=str(''), opacity=0)
                    self.ids.this_user_list.add_widget(item2)
                else:
                    item = OneLineListItem(
                        text=str(chatAnterior['mensaje']), bg_color=('FF5A1E'))
                    self.ids.this_user_list.add_widget(item)
                    item = OneLineListItem(text=str(''), opacity=0)
                    self.ids.other_user_list.add_widget(item)
        self.ids.scrollChat.scroll_y = 0
        self.ids.message_input.text = ''

    def send_message(self, mensaje, usuario1):

        if(str(mensaje) != ''):
            usuario2 = datosUsuario('usuario')
            if usuario1 < usuario2:
                chat = usuario1+usuario2
            else:
                chat = usuario2+usuario1
            insertarMensaje(datosUsuario('usuario'),
                            str(mensaje), chat, 'data')
            self.crearChat(usuario1)
        else:
            self.crearChat(usuario1)

    def borrarBusquedaChat(self):
        try:
            self.ids.MDListFiltradoChat.clear_widgets()
        except AttributeError:
            pass

    def mostrar_mapa(self):
        print('Mostrar mapa')

    def inicioSesion(self, usuario, password):
        #self.current = 'screen_principal'
        # QUITAR LOS COMENTARIOS PARA QUE FUNCIONE EL LOGIN Y REGISTRO
        if comprobarInicioSesion(usuario, password, 'data'):
            self.current = 'screen_principal'
        else:
            self.ids.signal_login.text = 'Usuario o contraseña incorrectos'

    def clear_signal(self):
        self.ids.signal_register.text = ''
        self.ids.signal_login.text = ''


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        Builder.load_file('design.kv')

        return Ui()

    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'


if __name__ == '__main__':
    MainApp().run()
