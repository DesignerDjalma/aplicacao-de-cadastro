import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class BancoDeDados:
    def setdb(self):
        self.referencia_usuarios.set({
            "email":"usuario@email.com",
            "username":"username_usuario",
            "password":"senha_usuario",
            })

class Usuario:
    def __init__(self) -> None:
        self.iniciar()

    def iniciar(self) -> None:
        self.cred = credentials.Certificate(R"D:\appcadastroServiceAccountKey.json")
        firebase_admin.initialize_app(self.cred, {"databaseURL":"https://appcadastro-72250-default-rtdb.firebaseio.com/"})
        self.referencia = db.reference('py/')
        self.referencia_usuarios = self.referencia.child('usuarios')
    
    def listarUsuarios(self) -> dict:
        self.dicionario_users = self.referencia_usuarios.get()
        return self.dicionario_users

    def isUsuarioCadastrado(self, loginInfo: dict) -> bool:
        _dados = self.listarUsuarios()
        _all_users = [_dados[i]['username'] for i in _dados]
        if loginInfo['username'] in _all_users:
            return True
        else:
            return False

    def cadastrarUsuario(self, dodosUsuario: dict) -> None:
        print(f"Dados: {dodosUsuario}")
        print("Cadastrando usuário...")
        self.referencia_usuarios.push(dodosUsuario)
        print("Usuario cadastrado com sucesso!")

    def logarUsuario(self, loginInfo: dict) -> bool:
        if self.isUsuarioCadastrado(loginInfo):
            print("Usuario Existe")
            return True
        else:
            print("Usuario NÃO existe")
            return False



if __name__ == "__main__":
    a = Usuario()
    a.logarUsuario({'username':'Djalma Filho'})
    


# {
#     '-NJJUc9Zty5-Vr4QvPSg': {'email': 'djalma@gmail.com', 'password': 'Djalm@123456789', 'username': 'djalma '}, '-NJJVdS3QV4yQRlkAIDe': {'email': 'mary@gmail.com', 'password': 'Djalm@123456789', 'username': 'Mary Lee'}, '-NJJc_xQJRaS45egUsKZ': {'email': 'email@email.com.br', 'password': '22222222Dd3@', 'username': 'Jéssica Matos'}}

