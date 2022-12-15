from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import string
import re

def validaCaracteres(palavra: str) -> bool:
    for l in palavra:
        if l in [i for i in string.punctuation]:
            return False
    return True
class TelaCadastro(Screen):
    _senhaCheckValid = False
    _usuarioValid = False
    _senhaValid = False
    _emailValid = False
    _verificarSenha = False

    def validacaoOk(self):
        print("Validação Okay")
        self.app = MDApp.get_running_app()
        self.app.root.current = "tela_cadastro_sucesso"
        self.app.root.transition.direction = "left" 

    def validarDados(self):
        self._senhaCheckValid = False
        self._usuarioValid = False
        self._senhaValid = False
        self._emailValid = False
        self.validarUsuario()
        self.validarSenha()
        self.validarSenhaCheck()
        self.validarEmail()

        if self._senhaCheckValid and (
            self._usuarioValid) and (
            self._senhaValid) and (
            self._emailValid):
            self.validacaoOk()

    def validarEmail(self):
        self._emailValid = False

        self.ids.emailTextoErroReg.text_color = [1, 0, 0, 1]
        _regex_expression = re.compile(R'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        _email_valido = re.fullmatch(_regex_expression, self.ids.emailInputReg.text)
        
        if _email_valido:
            print("Seu e-mail é válido", _email_valido.string)
            self.ids.emailTextoErroReg.text_color = [0, 0.59, 0, 1]
            self.ids.emailTextoErroReg.text = "[i]Esse e-mail é válido.[/i]"
            self._emailValid = True
        else:
            self.ids.emailTextoErroReg.text = "[i]Esse e-mail não é válido.[/i]"

    def validarSenhaCheck(self):
        if self._verificarSenha:
            self.ids.senhaCheckTextoErroReg.text_color = [1, 0, 0, 1]
            if self.ids.senhaCheckInputReg.text != self.ids.senhaInputReg.text:
                self.ids.senhaCheckTextoErroReg.text = "[i]As senhas não são identicas.[/i]"
                self._senhaCheckValid = False
            else:
                self.ids.senhaCheckTextoErroReg.text_color = [0, 0.59, 0, 1]
                self.ids.senhaCheckTextoErroReg.text = "[i]As senhas são identicas.[/i]"
                self._senhaCheckValid = True
        else:
            self.ids.senhaCheckTextoErroReg.text = ""

    def validarUsuario(self):
        _usuario_valid = True  # usuarioValido

        if self.ids.usuarioInputReg.text == "":
            self.ids.usuarioTextoErroReg.text = "[i]Forneça um usuário válido[/i]"
            print(self.ids.usuarioTextoErroReg.text)
            _usuario_valid = False
        else:
            if not validaCaracteres(self.ids.usuarioInputReg.text):
                self.ids.usuarioTextoErroReg.text = "[i]Caracteres especiais não são permitidos[/i]"
                print(self.ids.usuarioTextoErroReg.text)
                _usuario_valid = False
            else:
                if 3 >= len(self.ids.usuarioInputReg.text) >= 1:
                    self.ids.usuarioTextoErroReg.text = "[i]O nome de usuário deve ter pelo menos 4 caracteres[/i]"
                    print(self.ids.usuarioTextoErroReg.text)
                    _usuario_valid = False
                
                if 20 < len(self.ids.usuarioInputReg.text):
                    self.ids.usuarioTextoErroReg.text = "[i]O nome de usuário deve ter no máximo 20 caracteres[/i]"
                    print(self.ids.usuarioTextoErroReg.text)
                    _usuario_valid = False

        # Validacao Final
        if _usuario_valid:  
            self.ids.usuarioTextoErroReg.text = ""
            self._usuarioValid = True
            print("self._usuarioValid = True")
 
    def validarSenha(self):
        _regex_expression = re.compile(R"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$")
        _senha_valid = True
        _senha_forte = False
        self.ids.senhaTextoErroReg.text_color = [1, 0, 0, 1]

        if self.ids.senhaInputReg.text == "":
            self.ids.senhaTextoErroReg.text = "[i]Forneça uma senha válida[/i]"
            print(self.ids.senhaTextoErroReg.text)
            _senha_valid = _senha_forte = self._verificarSenha = False

        else:
            if 7>=len(self.ids.senhaInputReg.text) >= 1:
                self.ids.senhaTextoErroReg.text = "[i]A senha deve contér pelo menos 8 caracteres"
                _senha_valid = _senha_forte =False
            else:
                if 32 < len(self.ids.senhaInputReg.text):
                    self.ids.senhaTextoErroReg.text = "[i]A senha deve ter no máximo 32 caracteres[/i]"
                    print(self.ids.senhaTextoErroReg.text)
                    _senha_valid = _senha_forte = self._verificarSenha = False
                else:
                    _senha_forte = re.fullmatch(_regex_expression, self.ids.senhaInputReg.text)
                    if _senha_forte:
                        print("Sua senha é forte: ", _senha_forte.string)
                        _senha_valid = _senha_forte = self._verificarSenha = True
                    else:
                        self.ids.senhaTextoErroReg.text = "[i]Deve incluir maisculas, minusculas, especiais e números[/i]"
                        _senha_valid = _senha_forte = self._verificarSenha = False

        # Validacao Final
        if _senha_valid:
            self.ids.senhaTextoErroReg.text_color = [0, 0.59, 0, 1]
            self.ids.senhaTextoErroReg.text = "[i]Sua senha é forte[/i]"
            print(self.ids.senhaTextoErroReg.text)
            self._senhaValid = True
            print("self._senhaValid = True")