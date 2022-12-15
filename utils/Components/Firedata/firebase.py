import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import getpass


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
        self.cred = credentials.Certificate(f'/home/{getpass.getuser()}/serviceAccountKey.json')
        firebase_admin.initialize_app(self.cred, {"databaseURL":"https://appcadastro-72250-default-rtdb.firebaseio.com/"})
        self.referencia = db.reference('py/')
        self.referencia_usuarios = self.referencia.child('usuarios')
    
    def cadastrarUsuario(self, dodosUsuario: dict) -> None:
        print(f"Dados: {dodosUsuario}")
        print("Cadastrando usuário...")
        self.referencia_usuarios.push(dodosUsuario)
        print("Usuario cadastrado com sucesso!")

if __name__ == "__main__":
    pass
    




