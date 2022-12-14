from utils.telas.telaCadastro import TelaCadastro
from utils.telas.telaCadastroSucesso import TelaCadastroSucesso
from utils.telas.telaEsqueceuSenha import TelaEsqueceuSenha
from utils.telas.telaLogado import TelaLogado
from utils.telas.telaPrincipal import TelaPrincipal
from utils.widgets.minhaTopBar import MinhaTopBar
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp



fe = fatorEscala = 1.2 # ideal=1.2
Window.size = (360*fe, 640*fe)



class MeuAplicativoApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.icon = "./assets/imagens/icone-dourado.ico"

    def build(self):
        return Builder.load_file("./interface.kv")



if __name__ == "__main__":
    MeuAplicativoApp().run()
    