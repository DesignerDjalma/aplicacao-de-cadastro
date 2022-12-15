import requests
import json


def isBancoDeDadosON(url: str) -> bool:
    r = requests.get(url)
    return False if r.status_code != 200 else True 

def integridadeBancoDeDados() -> None:
    ok = isBancoDeDadosON(MeuFireBase.url)
    msg = "online" if ok else "offline"
    print(f"Banco de Dados: {msg.upper()}!")



class MeuFireBase:
    url: str = "https://dadositerpa-default-rtdb.firebaseio.com/"
    

class TipoRequisicao:
    geral: str = ""
    processos: str = "Processos"


class Requisicao:
    @staticmethod
    def tipo(_tipo: TipoRequisicao) -> str:
        return f"{MeuFireBase.url}/{_tipo}.json"
    
    @staticmethod
    def editarPorId(_tipo: TipoRequisicao, _id: str) -> str:
        return f"{MeuFireBase.url}/{_tipo}/{_id}.json"


class Processos:
    
    @staticmethod
    def novoProcesso(nome: str="", denominacao: str="",
                    municipio: str="", situacao: str="",
                    zee: str="", data: str="") -> None:
        processos = Processos.verProcessos()
        if processos[0]: id = len(processos[1].items()) + 1
        else: id = len(processos[1]) + 1
        dados = { 
            "nome":nome,"denominacao":denominacao,
            "municipio":municipio,"situacao":situacao,
            "zee":zee,"data":data, "id":id
            }
        print(f"Novo Processo: {dados}")
        req = requests.post(
            url=Requisicao.tipo(TipoRequisicao.processos),
            data=json.dumps(dados))
        print(f"Status: {req} | Valor: {req.text}")
    
    @staticmethod
    def verProcessos(tipo: TipoRequisicao = TipoRequisicao.processos) -> None:
        """Entra na base dos dados e mostra o tipo especificado de dado."""
        
        url = Requisicao.tipo(tipo)
        req = requests.get(url)
        procs = json.loads(req.text)

        if isinstance(procs, list):
            return False, procs[1:]
        else:
            return True, procs
        



if __name__ == "__main__":
    
    integridadeBancoDeDados()
    tudo = Processos.verProcessos(TipoRequisicao.geral)
    print(tudo)