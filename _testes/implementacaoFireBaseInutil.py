
# import requests
# import json


# def isBancoDeDadosON(url: str) -> bool:
#     r = requests.get(url)
#     return False if r.status_code != 200 else True 

# def integridadeBancoDeDados() -> None:
#     ok = isBancoDeDadosON(MeuFireBase.url)
#     msg = "online" if ok else "offline"
#     print(f"Banco de Dados: {msg.upper()}!")



# class MeuFireBase:
#     url: str = "https://appcadastro-72250-default-rtdb.firebaseio.com/"
    

# class TipoRequisicao:
#     geral: str = ""
#     usuarios: str = "usuarios"


# class Requisicao:

#     @staticmethod
#     def tipo(_tipo: TipoRequisicao) -> str:
#         return f"{MeuFireBase.url}/{_tipo}.json"
    
#     @staticmethod
#     def editarPorId(_tipo: TipoRequisicao, _id: str) -> str:
#         return f"{MeuFireBase.url}/{_tipo}/{_id}.json"


# class Usuarios:
    
#     @staticmethod
#     def novoUsuario(username: str="", password: str="", email: str="") -> None:
        
#         dados = { "username":username, "password":password, "email":email }
#         req = requests.post(
#             url=Requisicao.tipo(TipoRequisicao.usuarios),
#             data=json.dumps(dados)
#             )
#         print(f"Status: {req} | Valor: {req.text}")
    
#     @staticmethod
#     def listarUsuarios(tipo: TipoRequisicao=TipoRequisicao.usuarios) -> None:
#         """Entra na base dos dados e mostra o tipo especificado de dado."""
        
#         url = Requisicao.tipo(tipo)
#         req = requests.get(url)
#         procs = json.loads(req.text)

#         if isinstance(procs, list):
#             return False, procs[1:]
#         else:
#             return True, procs
        



# if __name__ == "__main__":
    
#     integridadeBancoDeDados()
#     all_users = Usuarios.listarUsuarios(TipoRequisicao.geral)
#     print(all_users)