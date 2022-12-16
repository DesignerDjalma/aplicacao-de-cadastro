import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from getpass import getuser
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
        if getuser() == "djalmaf":
            self.cred = credentials.Certificate("/home/djalmaf/serviceAccountKey.json")
        else:
            self.cred = credentials.Certificate(R"D:\appcadastroServiceAccountKey.json")

        firebase_admin.initialize_app(self.cred, {"databaseURL":"https://appcadastro-72250-default-rtdb.firebaseio.com/"})
        self.referencia = db.reference('py/')
        self.referencia_usuarios = self.referencia.child('usuarios')
    
    def listarDadosOnline(self) -> dict:
        self.dicionario_users = self.referencia_usuarios.get()
        return self.dicionario_users

    def isUsuarioCadastradoComSenhaCorreta(self, loginInfo: dict) -> bool:
        _dados = self.listarDadosOnline()

        for _id,_ in _dados.items():
            if _dados[_id]['username'] == loginInfo['username']:
                if _dados[_id]['password'] == loginInfo['password']:
                    return 'autorizado'
                else:
                    return 'senha_incorreta'
        return 'usuario_nao_encontrado'

    def cadastrarUsuario(self, dodosUsuario: dict) -> None:
        print(f"Dados: {dodosUsuario}")
        print("Cadastrando usuário...")
        self.referencia_usuarios.push(dodosUsuario)
        print("Usuario cadastrado com sucesso!")

    def logarUsuario(self, loginInfo: dict) -> bool:
        reposta = self.isUsuarioCadastradoComSenhaCorreta(loginInfo)
        if reposta != 'usuario_nao_encontrado':
            print("Usuario Existe")
        else:
            print("Usuário Não existe")
        return reposta



if __name__ == "__main__":
    a = Usuario()
    a.logarUsuario({
        'username':'Djalma Filho',
        'password':'Djalma@12345678',
        })
    


# {
#     '-NJJUc9Zty5-Vr4QvPSg': {'email': 'djalma@gmail.com', 'password': 'Djalm@123456789', 'username': 'djalma '}, '-NJJVdS3QV4yQRlkAIDe': {'email': 'mary@gmail.com', 'password': 'Djalm@123456789', 'username': 'Mary Lee'}, '-NJJc_xQJRaS45egUsKZ': {'email': 'email@email.com.br', 'password': '22222222Dd3@', 'username': 'Jéssica Matos'}}

