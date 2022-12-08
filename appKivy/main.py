import requests
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivymd.uix.list import OneLineListItem
from baseDatosPruebaApp import *
import webview

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
            self.ids.MDListFiltrado.add_widget(OneLineListItem(text=element))

    def borrarBusquedaFiltrado(self):
        try:
            self.ids.MDListFiltrado.clear_widgets()
        except AttributeError:
            pass
    
    def mostrar_mapa(self):
        webview.create_window('Evently - Mapa de discotecas', '../mapa.html')
        webview.start()


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Blue'
        self.url = 'https://evently-646a2-default-rtdb.firebaseio.com/.json'
        self.key = 'f56cws1P0VqbWLLiquVOReDvJONfKtq9qzeWDSIl'
        Builder.load_file('design.kv')

        return Ui()

    def change_style(self, checked, value):
        if value:
            self.theme_cls.theme_style = 'Light'
        else:
            self.theme_cls.theme_style = 'Dark'


if __name__ == '__main__':
    MainApp().run()
