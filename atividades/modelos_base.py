
# ==============================================================================
# PROJETO FINAL - BIMESTRE
# Classe Base: Produto
# ==============================================================================

class Produto:

    # Construtor
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)

    # Getter do nome
    def get_nome(self):
        return self.__nome

    # Setter do nome com validação
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Erro: O nome deve possuir pelo menos 3 caracteres.")

    # Getter do preço
    def get_preco(self):
        return self.__preco

    # Setter do preço com validação
    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and not isinstance(preco, bool) and preco >= 0:
            self.__preco = float(preco)
        else:
            print("Erro: O preço não pode ser negativo ou inválido.")


# ==============================================================================
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==============================================================================

if __name__ == "__main__":

    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste de instanciação com dados VÁLIDOS
    objeto_valido = Produto("Cadeira Gamer", 850.00)

    print(
        f"Objeto Criado: {objeto_valido.get_nome()} "
        f"- R$ {objeto_valido.get_preco():.2f}"
    )

    # 2. Teste de instanciação com dados INVÁLIDOS
    print("\n--- Teste 1: Tentativa de criar com preço negativo ---")

    objeto_invalido = Produto("Mesa", -150.00)

    print(
        f"Resultado mantido com segurança: "
        f"R$ {objeto_invalido.get_preco():.2f}"
    )

    # 3. Teste de alteração via Setter com dado INVÁLIDO
    print("\n--- Teste 2: Tentativa de alterar o nome para um texto muito curto ---")

    objeto_valido.set_nome("AB")

    print(f"Nome do objeto protegido: {objeto_valido.get_nome()}")
