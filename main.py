from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from kivymd.app import MDApp

fe = fatorEscala = 1.2
Window.size = (360*fe, 640*fe)

class MinhaTopBar(MDTopAppBar):
    def sairApp(self, *args):
        MeuAplicativoApp().stop()

    def fecharDialogo(self, *args):
        self.dialog.dismiss(force=True)

    def callback(self, *args):
        self.dialog = MDDialog(
            title="Fechar Aplicativo?",
            text="Você está prestes a sair do aplicativo.",
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.fecharDialogo(),
                ),
                MDFlatButton(
                    text="SIM",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    on_release=lambda x: self.sairApp(),
                ),
            ],
        )
        self.dialog.open()

class TelaEsqueceuSenha(Screen):
    pass

class TelaLogado(Screen):
    pass

class TelaCadastroSucesso(Screen):
    pass

class TelaCadastro(Screen):
    pass

class TelaPrincipal(Screen):
    pass

class MeuAplicativoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = "./icone-dourado.png"

    def build(self):
        return Builder.load_file("./interface.kv")


if __name__ == "__main__":
    MeuAplicativoApp().run()