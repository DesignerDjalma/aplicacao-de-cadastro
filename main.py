from utils.Components.Telas.telaCadastro import TelaCadastro
from utils.Components.Telas.telaCadastroSucesso import TelaCadastroSucesso
from utils.Components.Telas.telaEsqueceuSenha import TelaEsqueceuSenha
from utils.Components.Telas.telaLogado import TelaLogado
from utils.Components.Telas.telaPrincipal import TelaPrincipal
from utils.Components.Widgets.minhaTopBar import MinhaTopBar
from utils.Components.Telas.telaCarregamento import TelaCarregamento
from utils.Components.Firedata.firebase import Usuario
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

    @staticmethod
    def cadastrarUsuario(dodosUsuario: dict) -> None:
        users.cadastrarUsuario(dodosUsuario)
    
    
    def logarUsuario(self, loginInfo: dict) -> None:
        return users.logarUsuario(loginInfo)
            



if __name__ == "__main__":
    users = Usuario()
    MeuAplicativoApp().run()
    

