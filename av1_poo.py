class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print("⚠️ Erro: Salário deve ser maior que zero. Valor não foi alterado.")

    def calcular_salario_final(self):
        return self.__salario_base


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500.00
        return self.get_salario_base()


if __name__ == "__main__":
    print("=" * 70)
    print("SISTEMA DE GESTÃO DE FUNCIONÁRIOS - TechCorp")
    print("=" * 70)
    print()

    print("TESTE 1: Instanciando um Gerente")
    print("-" * 70)

    gerente = Gerente(
        nome="Carlos Silva",
        matricula="MAT001",
        salario_base=8000.00,
        bonus_gestao=2000.00
    )

    print(f"Gerente criado: {gerente.nome}")
    print(f"  Matrícula: {gerente.matricula}")
    print(f"  Salário Base: R$ {gerente.get_salario_base():,.2f}")
    print(f"  Bônus de Gestão: R$ {gerente.bonus_gestao:,.2f}")
    print(f"  Salário Final: R$ {gerente.calcular_salario_final():,.2f}")
    print()

    print("TESTE 2: Instanciando um Desenvolvedor Senior")
    print("-" * 70)

    dev_senior = Desenvolvedor(
        nome="Ana Costa",
        matricula="MAT002",
        salario_base=6000.00,
        nivel="Senior"
    )

    print(f"Desenvolvedor criado: {dev_senior.nome}")
    print(f"  Matrícula: {dev_senior.matricula}")
    print(f"  Nível: {dev_senior.nivel}")
    print(f"  Salário Base: R$ {dev_senior.get_salario_base():,.2f}")
    print(f"  Adicional Senior: R$ 1.500,00")
    print(f"  Salário Final: R$ {dev_senior.calcular_salario_final():,.2f}")
    print()

    print("TESTE 3: Verificando Encapsulamento")
    print("-" * 70)

    print(f"Salário base inicial do gerente: R$ {gerente.get_salario_base():,.2f}")
    print()
    print("Tentando alterar salário_base diretamente para -100...")

    gerente.__salario_base = -100

    print(f"Verificando via getter: R$ {gerente.get_salario_base():,.2f}")
    print("Atributo privado protegido!")
    print()

    print("Tentando alterar com setter para -100...")
    gerente.set_salario_base(-100)
    print(f"Verificando via getter: R$ {gerente.get_salario_base():,.2f}")
    print()

    print("Alterando com setter para R$ 9.000,00...")
    gerente.set_salario_base(9000.00)
    print(f"Verificando via getter: R$ {gerente.get_salario_base():,.2f}")
    print(f"Novo salário final do gerente: R$ {gerente.calcular_salario_final():,.2f}")
    print()

    print("TESTE 4: Desenvolvedor Junior")
    print("-" * 70)

    dev_junior = Desenvolvedor(
        nome="João Silva",
        matricula="MAT003",
        salario_base=4000.00,
        nivel="Junior"
    )

    print(f"Desenvolvedor criado: {dev_junior.nome}")
    print(f"  Nível: {dev_junior.nivel}")
    print(f"  Salário Base: R$ {dev_junior.get_salario_base():,.2f}")
    print(f"  Adicional Senior: R$ 0,00")
    print(f"  Salário Final: R$ {dev_junior.calcular_salario_final():,.2f}")
    print()

    print("=" * 70)
    print("RESUMO FINAL - SALÁRIOS DOS FUNCIONÁRIOS")
    print("=" * 70)

    funcionarios = [gerente, dev_senior, dev_junior]
    total_folha = 0

    for i, func in enumerate(funcionarios, 1):
        salario_final = func.calcular_salario_final()
        total_folha += salario_final
        print(f"{i}. {func.nome:20s} → Salário Final: R$ {salario_final:>10,.2f}")

    print("-" * 70)
    print(f"{'TOTAL DA FOLHA':20s} → R$ {total_folha:>10,.2f}")
    print("=" * 70)