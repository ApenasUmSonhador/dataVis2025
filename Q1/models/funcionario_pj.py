from .funcionario import Funcionario

class FuncionarioPJ(Funcionario):
    def __init__(self, nome, cpf, cnpj, salario):
        super().__init__(nome, cpf, salario)
        self.cnpj = cnpj
        self.tipo = "PJ"

    def calcular_beneficios(self):
        return super().calcular_beneficios()  # sem vale-refeição
