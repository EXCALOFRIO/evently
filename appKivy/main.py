from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image


class Ui(ScreenManager):
    pass


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
