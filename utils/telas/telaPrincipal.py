from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import string

class TelaPrincipal(Screen):

    _senhaValida = None
    _usuarioValido = None

    def validacaoOk(self):
        self.app = MDApp.get_running_app()
        self.app.root.current = "tela_logado"
        self.app.root.transition.direction = "left"
    
    def validarUsuario(self):
        def validaCaracteres(palavra: str) -> bool:
            for l in palavra:
                if l in [i for i in string.punctuation]:
                    return False
            return True

        _uV = True  # usuarioValido
        _uTxtE = self.ids.usuarioTextoErro.text
        _uI = self.ids.usuarioInput.text
        

        if not validaCaracteres(_uI):
            _uTxtE = "[i]Caracteres especiais não são permitidos[/i]"
            _uV = False

        if _uI == "":
            _uTxtE = "[i]Forneça um usuário válido[/i]"
            _uV = False

        if 5 > len(_uI) > 1:
            _uTxtE = "[i]O nome de usuário deve ter pelo menos 4 letras[/i]"
            _uV = False

        if _uV:
            _uTxtE = ""
            

    def validarSenha(self):
        if self.ids.senhaInput.text == "":
            self.ids.senhaTextoErro.text = "[i]Forneça um usuário válido[/i]"
            
        