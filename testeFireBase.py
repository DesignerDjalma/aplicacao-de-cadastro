import requests
import json



class meuLinkFireBase:
    link: str = "https://appteste01-ca569-default-rtdb.firebaseio.com/"

class MinhaFireBase:
    @staticmethod
    def requisicaoVendas() -> str:
        return f"{meuLinkFireBase.link}Vendas/.json"
    
    @staticmethod
    def requisicaoProdutos() -> str:
        return f"{meuLinkFireBase.link}Produtos/.json"
    
    @staticmethod
    def editarVendasPorId(id_venda: str) -> str:
        return f"{meuLinkFireBase.link}Vendas/{id_venda}/.json"
    
    @staticmethod
    def editarProdutosPorId(id_produto: str) -> str:
        return f"{meuLinkFireBase.link}Produtos/{id_produto}/.json"


class MinhasVendas:
    @staticmethod
    def novaVenda(cliente_nome: str="sem nome", ativo: bool=False) -> json.dumps:
        parametros = {
            "cliente":cliente_nome,
            "ativo":ativo
            }
        print(f"Nova Venda: {parametros}")
        return json.dumps(parametros)

class MeusProdutos:
    @staticmethod
    def novoProduto(nome_produto: str="sem nome", preco: float=0.0, quantidade: int=0) -> json.dumps:
        parametros = {
            "nome":nome_produto,
            "preco":preco,
            "quantidade":quantidade
            }
        print(f"Novo Produto: {parametros}")
        return json.dumps(parametros)
    
    @staticmethod
    def editarProduto(id_produto: str, nome_produto, preco, quantidade):
        novos_param: dict = {}
        if nome_produto: novos_param['nome'] = nome_produto
        if preco: novos_param['preco'] = preco
        if quantidade: novos_param['quantidade'] = quantidade
        return json.dumps(novos_param)


class Requisicoes:

    """Responsavel por administrar as requisições."""

    def novoProduto(nome_produto: str, preco: float, quantidade: int):
        req = requests.post(
            url=MinhaFireBase.requisicaoProdutos(),
            data=MeusProdutos.novoProduto(nome_produto=nome_produto,
                                          preco=preco,
                                          quantidade=quantidade))
        print(f"Status: {req} | Valor: {req.text}")
        return req

    def novaVenda(cliente_nome, ativo):
        req = requests.post(
            url=MinhaFireBase.requisicaoVendas(),
            data=MinhasVendas.novaVenda(cliente_nome=cliente_nome,
                                        ativo=ativo))
        print(f"Status: {req} | Valor: {req.text}")
        return req

    def editarProduto(id_produto: str, nome_produto, preco, quantidade):
        req = requests.patch(
            url=MinhaFireBase.editarProdutosPorId(id_produto=id_produto),
        )

    def editarVenda():
        pass
        





Requisicoes.novaVenda("Jorge", True)
Requisicoes.novoProduto("Shampoo", 11.50, 5)
