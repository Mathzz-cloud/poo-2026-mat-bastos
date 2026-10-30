
# ==========================================
# PROJETO FINAL - HERANÇA E POLIMORFISMO
# ==========================================

# SUPERCLASSE
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco(self):
        return self.preco

    def exibir_informacoes(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")


# SUBCLASSE 1
class ProdutoFisico(Produto):
    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    # Sobrescrita de método
    def calcular_preco(self):
        return self.preco + 15.00

    def exibir_informacoes(self):
        print(f"Produto Físico: {self.nome}")
        print(f"Preço com frete: R$ {self.calcular_preco():.2f}")
        print(f"Peso: {self.peso} kg")


# SUBCLASSE 2
class ProdutoDigital(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    # Sobrescrita de método
    def calcular_preco(self):
        return self.preco

    def exibir_informacoes(self):
        print(f"Produto Digital: {self.nome}")
        print(f"Preço: R$ {self.calcular_preco():.2f}")
        print(f"Tamanho: {self.tamanho} MB")


# ==========================================
# TESTE DE HERANÇA E POLIMORFISMO
# ==========================================

if __name__ == "__main__":

    # Criando objetos
    produto1 = ProdutoFisico("Cadeira Gamer", 850.00, 12)
    produto2 = ProdutoDigital("Curso Python", 120.00, 500)

    # Lista heterogênea: objetos de classes diferentes
    produtos = [produto1, produto2]

    print("=== TESTANDO HERANÇA E POLIMORFISMO ===")

    # Polimorfismo
    for produto in produtos:
        produto.exibir_informacoes()
        print("-----------------------------")
