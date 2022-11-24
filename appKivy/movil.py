from kivymd.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image


class MainApp(App):
    def build(self):

        return Builder.load_string(KV)


KV = '''

<FormaButton@Button>:
    font_size: self.width/5
    color: '#FFFFFF'
GridLayout
    pantalla: entry
    rows: 3
    padding: 5
    spacing: 5
    BoxLayout:
        TextInput:
            text : "Bienvenido a Evently"
            id: entry
            halign: 'right'
            font_size: 35
            background_color: '#93A9EB'
           # multiline: False
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "Mapa"
            background_color: '#93A9EB' 
        FormaButton:
            text: "Carta"
            background_color: '#93A9EB'
        FormaButton:
            text: "Filtrado"
            background_color: '#93A9EB'
    BoxLayout:
        spacing: 5
        FormaButton:
            text: "Perfil"
            background_color: '#93A9EB'
        FormaButton:
            text: "Resenas"
            background_color: '#93A9EB'
        FormaButton:
            text: "Valoracion"
            background_color: '#93A9EB'
'''

if __name__ == '__main__':
    MainApp().run()
