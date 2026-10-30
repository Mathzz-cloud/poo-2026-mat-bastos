
class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.pedidos = []  # 0..*

    def realizar_pedido(self, pedido):
        self.pedidos.append(pedido)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto  # 1
        self.quantidade = quantidade

    def calcular_subtotal(self):
        return self.produto.preco * self.quantidade


class Pedido:
    def __init__(self):
        self.itens = []  # 1..* após a criação do pedido

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(
            item.calcular_subtotal()
            for item in self.itens
        )


class Carrinho:
    def __init__(self):
        self.produtos = []  # Agregação: 0..*

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
