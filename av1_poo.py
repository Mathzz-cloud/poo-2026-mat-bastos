# AV1 - AVALIAÇÃO PRÁTICA EM LABORATÓRIO
# Disciplina: Programação Orientada a Objetos (POO)
# Aluno: [Seu Nome]
# Data: 2026-08-21

# ============================================================================
# REQUISITO 1: CLASSE BASE (Funcionario) - 1.25 pontos
# ============================================================================

class Funcionario:
    """
    Classe base para representar um funcionário da empresa TechCorp.
    Implementa encapsulamento do atributo salário base.
    """
    
    def __init__(self, nome, matricula, salario_base):
        """
        Construtor que inicializa os atributos do funcionário.
        
        Args:
            nome (str): Nome do funcionário
            matricula (str): Matrícula do funcionário
            salario_base (float): Salário base (privado)
        """
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base
    
    def get_salario_base(self):
        """
        Getter: Retorna o valor do salário base.
        
        Returns:
            float: O salário base do funcionário
        """
        return self.__salario_base
    
    def set_salario_base(self, novo_salario):
        """
        Setter: Altera o salário base apenas se o valor for maior que zero.
        
        Args:
            novo_salario (float): Novo valor do salário base
        """
        if novo_salario > 0:
            self.__salario_base = novo_salario
        else:
            print(f"⚠️ Erro: Salário deve ser maior que zero. Valor não foi alterado.")
    
    def calcular_salario_final(self):
        """
        Calcula o salário final do funcionário.
        Método base que retorna apenas o salário base.
        
        Returns:
            float: O salário final
        """
        return self.__salario_base


# ============================================================================
# REQUISITO 2: SUBCLASSE (Gerente) - 1.25 pontos
# ============================================================================

class Gerente(Funcionario):
    """
    Classe que representa um gerente, herdando de Funcionario.
    Inclui um bônus de gestão no cálculo do salário final.
    """
    
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        """
        Construtor que inicializa um gerente usando super().
        
        Args:
            nome (str): Nome do gerente
            matricula (str): Matrícula do gerente
            salario_base (float): Salário base
            bonus_gestao (float): Bônus de gestão
        """
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao
    
    def calcular_salario_final(self):
        """
        Sobrescreve o método da classe mãe.
        Calcula o salário final como salário base + bônus de gestão.
        
        Returns:
            float: Salário final (base + bônus)
        """
        return self.get_salario_base() + self.bonus_gestao


# ============================================================================
# REQUISITO 3: SUBCLASSE (Desenvolvedor) - 1.25 pontos
# ============================================================================

class Desenvolvedor(Funcionario):
    """
    Classe que representa um desenvolvedor, herdando de Funcionario.
    Inclui um nível (Junior, Pleno ou Senior) que afeta o cálculo do salário.
    """
    
    def __init__(self, nome, matricula, salario_base, nivel):
        """
        Construtor que inicializa um desenvolvedor usando super().
        
        Args:
            nome (str): Nome do desenvolvedor
            matricula (str): Matrícula do desenvolvedor
            salario_base (float): Salário base
            nivel (str): Nível profissional ("Junior", "Pleno" ou "Senior")
        """
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel
    
    def calcular_salario_final(self):
        """
        Sobrescreve o método da classe mãe.
        Se Senior: adiciona R$ 1.500,00 ao salário base.
        Caso contrário: retorna apenas o salário base.
        
        Returns:
            float: Salário final (base ou base + 1500 se Senior)
        """
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500.00
        else:
            return self.get_salario_base()


# ============================================================================
# REQUISITO 4: INSTANCIAÇÃO, TESTES E EXECUÇÃO - 1.25 pontos
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("SISTEMA DE GESTÃO DE FUNCIONÁRIOS - TechCorp")
    print("=" * 70)
    print()
    
    # Teste 1: Criar instância de Gerente
    print("📋 TESTE 1: Instanciando um Gerente")
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
    
    # Teste 2: Criar instância de Desenvolvedor Senior
    print("📋 TESTE 2: Instanciando um Desenvolvedor Senior")
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
    
    # Teste 3: Demonstrar encapsulamento
    # Tentar alterar o salário base diretamente (sem usar o setter)
    print("📋 TESTE 3: Verificando Encapsulamento")
    print("-" * 70)
    print(f"Salário base inicial do gerente: R$ {gerente.get_salario_base():,.2f}")
    print()
    print("❌ Tentando alterar salário_base diretamente para -100...")
    gerente.__salario_base = -100  # Isso cria um novo atributo, não altera o privado
    print(f"Verificando via getter (get_salario_base()): R$ {gerente.get_salario_base():,.2f}")
    print("✅ Atributo privado protegido! O valor não foi alterado.")
    print()
    
    # Teste 4: Tentar alterar com setter para valor negativo
    print("❌ Tentando alterar com setter (set_salario_base) para -100...")
    gerente.set_salario_base(-100)
    print(f"Verificando via getter: R$ {gerente.get_salario_base():,.2f}")
    print()
    
    # Teste 5: Alterar com setter para valor positivo válido
    print("✅ Alterando com setter (set_salario_base) para R$ 9.000,00...")
    gerente.set_salario_base(9000.00)
    print(f"Verificando via getter: R$ {gerente.get_salario_base():,.2f}")
    print(f"Novo salário final do gerente: R$ {gerente.calcular_salario_final():,.2f}")
    print()
    
    # Teste 6: Desenvolvedor Junior (sem adicional)
    print("📋 TESTE 4: Desenvolvedor Junior (contraste com Senior)")
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
    print(f"  Adicional Senior: R$ 0,00 (não é Senior)")
    print(f"  Salário Final: R$ {dev_junior.calcular_salario_final():,.2f}")
    print()
    
    # Resumo final
    print("=" * 70)
    print("📊 RESUMO FINAL - SALÁRIOS DOS FUNCIONÁRIOS")
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
