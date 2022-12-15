from utils.telas.telaCadastro import TelaCadastro
from utils.telas.telaCadastroSucesso import TelaCadastroSucesso
from utils.telas.telaEsqueceuSenha import TelaEsqueceuSenha
from utils.telas.telaLogado import TelaLogado
from utils.telas.telaPrincipal import TelaPrincipal
from utils.widgets.minhaTopBar import MinhaTopBar
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp


window_size, fatorEscala =  (360, 640), 1.2 
Window.size = tuple(map(lambda x: x*fatorEscala, window_size))

 
class MeuAplicativoApp(MDApp):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.icon = "./assets/imagens/icone-dourado.ico"

    def build(self) -> Builder.load_file:
        return Builder.load_file("./interface.kv")


if __name__ == "__main__":
    MeuAplicativoApp().run()
    