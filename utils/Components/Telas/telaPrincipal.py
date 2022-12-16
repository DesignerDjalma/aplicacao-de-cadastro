from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
import string

def validaCaracteres(palavra: str) -> bool:
    for l in palavra:
        if l in [i for i in string.punctuation]:
            return False
    return True

class TelaPrincipal(Screen):
    
    _usuario_valid = False
    _senha_valid = False
    _senhaValid = False 
    _usuarioValid = False

    def irParaTela(self, tela: str, direcao: str) -> None:
        self.app = MDApp.get_running_app()
        self.app.root.current = tela
        self.app.root.transition.direction = direcao

    def limparErros(self) -> None:
        self.ids.usuarioTextoErro.text = ""
        self.ids.senhaTextoErro.text = ""

    def limparTudo(self) -> None:
        self.ids.usuarioTextoErro.text = ""
        self.ids.senhaTextoErro.text = ""
        self.ids.usuarioInput.text = ""
        self.ids.senhaInput.text = ""

    def limparSenha(self) -> None:
        self.ids.senhaInput.text = ""

    def validacaoOk(self) -> None:
        self.app = MDApp.get_running_app()
        self._senhaValid = False
        self._usuarioValid = False
        
        resposta = self.app.logarUsuario({
            'username':self.ids.usuarioInput.text,
            'password':self.ids.senhaInput.text,
            })

        self.ids.usuarioTextoErro.text = ""
        self.ids.senhaTextoErro.text = ""

        if resposta == 'senha_incorreta':
            self.ids.usuarioTextoErro.text = ""
            self.ids.senhaTextoErro.text = "[i]Senha incorreta.[/i]"
        elif resposta == 'usuario_nao_encontrado':
            self.ids.usuarioTextoErro.text = "[i]Usuario não encontrado.[/i]"
            self.ids.senhaTextoErro.text = ""
        elif resposta == 'autorizado':
            self.irParaTelaLogado()
        else:
            self.ids.usuarioTextoErro.text = "[i]Erro.[/i]"
            self.ids.senhaTextoErro.text = "[i]Erro.[/i]"

    def validarDados(self) -> None:
        
        self._senhaValid = False
        self._usuarioValid = False

        self.validarUsuario()
        self.validarSenha()
        
        if self._usuarioValid and self._senhaValid:
            self.validacaoOk()

    def validarUsuario(self) -> None:
        self._usuario_valid = True  # usuarioValido

        if self.ids.usuarioInput.text == "":
            self.ids.usuarioTextoErro.text = "[i]Forneça um usuário válido[/i]"
            print(self.ids.usuarioTextoErro.text)
            self._usuario_valid = False
        else:
            if not validaCaracteres(self.ids.usuarioInput.text):
                self.ids.usuarioTextoErro.text = "[i]Caracteres especiais não são permitidos[/i]"
                print(self.ids.usuarioTextoErro.text)
                self._usuario_valid = False
            else:
                if 3 >= len(self.ids.usuarioInput.text) >= 1:
                    self.ids.usuarioTextoErro.text = "[i]O nome de usuário deve ter pelo menos 4 caracteres[/i]"
                    print(self.ids.usuarioTextoErro.text)
                    self._usuario_valid = False
                
                if 20 < len(self.ids.usuarioInput.text):
                    self.ids.usuarioTextoErro.text = "[i]O nome de usuário deve ter no máximo 20 caracteres[/i]"
                    print(self.ids.usuarioTextoErro.text)
                    self._usuario_valid = False

        # Validacao Final
        if self._usuario_valid:  
            self.ids.usuarioTextoErro.text = ""
            self._usuarioValid = True
            print("self._usuarioValid = True")
            
    def validarSenha(self) -> None:
        print("Validando Senha!")
        self._senha_valid = True

        # Se a senha for vazia
        if self.ids.senhaInput.text == "":
            self.ids.senhaTextoErro.text = "[i]Forneça uma senha válida[/i]"
            print(self.ids.senhaTextoErro.text)
            self._senha_valid = False
        else:
            # Se a senha tem de 1 a 7 caracteres 
            if 7 >= len(self.ids.senhaInput.text) >= 1:
                self.ids.senhaTextoErro.text = "[i]A senha deve ter pelo menos 8 caracteres[/i]"
                print(self.ids.senhaTextoErro.text)
                self._senha_valid = False
            
            # Se a senha for maior quie 20
            if 32 < len(self.ids.senhaInput.text):
                self.ids.senhaTextoErro.text = "[i]A senha deve ter no máximo 32 caracteres[/i]"
                print(self.ids.senhaTextoErro.text)
                self._senha_valid = False

        # Validacao Final
        if self._senha_valid:
            self.ids.senhaTextoErro.text = ""
            print(self.ids.senhaTextoErro.text)
            self._senhaValid = True
            print("self._senhaValid = True")

    def irParaTelaCadastro(self) -> None:
        self.limparErros()
        self.irParaTela(direcao="left",
            tela="tela_cadastro")

    def irParaTelaEsqueceuSenha(self) -> None:
        self.limparErros()
        self.irParaTela(direcao="left",
            tela="tela_esqueceu_senha")

    def irParaTelaLogado(self) -> None:
        self.limparErros()
        self.limparSenha()
        self.irParaTela(direcao="left",
            tela="tela_logado")



