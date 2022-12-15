from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import string

def validaCaracteres(palavra: str) -> bool:
    for l in palavra:
        if l in [i for i in string.punctuation]:
            return False
    return True

class TelaPrincipal(Screen):
    
    _senhaValid = False 
    _usuarioValid = False

    def validacaoOk(self):
        self.app = MDApp.get_running_app()
        if self.app.logarUsuario({
            'username':self.ids.usuarioInput.text,
            'password':self.ids.senhaInput.text,
            }):
            self.app.root.current = "tela_logado"
            self.app.root.transition.direction = "left"
        else:
            self.ids.usuarioTextoErro.text = "[i]Usuario não encontrado.[/i]"
    
    def validarDados(self):
        self._senhaValid = False
        self._usuarioValid = False
        self.validarUsuario()
        self.validarSenha()
        
        if self._usuarioValid and self._senhaValid:
            self.validacaoOk()

    def validarUsuario(self):
        _usuario_valid = True  # usuarioValido

        if self.ids.usuarioInput.text == "":
            self.ids.usuarioTextoErro.text = "[i]Forneça um usuário válido[/i]"
            print(self.ids.usuarioTextoErro.text)
            _usuario_valid = False
        else:
            if not validaCaracteres(self.ids.usuarioInput.text):
                self.ids.usuarioTextoErro.text = "[i]Caracteres especiais não são permitidos[/i]"
                print(self.ids.usuarioTextoErro.text)
                _usuario_valid = False
            else:
                if 3 >= len(self.ids.usuarioInput.text) >= 1:
                    self.ids.usuarioTextoErro.text = "[i]O nome de usuário deve ter pelo menos 4 caracteres[/i]"
                    print(self.ids.usuarioTextoErro.text)
                    _usuario_valid = False
                
                if 20 < len(self.ids.usuarioInput.text):
                    self.ids.usuarioTextoErro.text = "[i]O nome de usuário deve ter no máximo 20 caracteres[/i]"
                    print(self.ids.usuarioTextoErro.text)
                    _usuario_valid = False

        # Validacao Final
        if _usuario_valid:  
            self.ids.usuarioTextoErro.text = ""
            self._usuarioValid = True
            print("self._usuarioValid = True")
            
    def validarSenha(self):
        _senha_valid = True

        if self.ids.senhaInput.text == "":
            self.ids.senhaTextoErro.text = "[i]Forneça uma senha válida[/i]"
            print(self.ids.senhaTextoErro.text)
            _senha_valid = False
        else:
            if 7 >= len(self.ids.senhaInput.text) >= 1:
                self.ids.senhaTextoErro.text = "[i]A senha deve ter pelo menos 8 caracteres[/i]"
                print(self.ids.senhaTextoErro.text)
                _senha_valid = False
            
            if 20 < len(self.ids.senhaInput.text):
                self.ids.senhaTextoErro.text = "[i]A senha deve ter no máximo 32 caracteres[/i]"
                print(self.ids.senhaTextoErro.text)
                _senha_valid = False

        # Validacao Final
        if _senha_valid:
            self.ids.senhaTextoErro.text = ""
            print(self.ids.senhaTextoErro.text)
            self._senhaValid = True
            print("self._senhaValid = True")


    def loginUser(self):
        pass        