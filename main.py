from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp

fe = fatorEscala = 1.2
Window.size = (360*fe, 640*fe)


class TelaCadastro(Screen):
    pass

class TelaPrincipal(Screen):
    pass

class MeuAplicativoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = "./icone-azul.png"

    def build(self):
        return Builder.load_file("./interface.kv")


if __name__ == "__main__":
    MeuAplicativoApp().run()