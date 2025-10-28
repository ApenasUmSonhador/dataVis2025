from .funcionario import Funcionario

class FuncionarioCLT(Funcionario):
    SALARIO_MINIMO = 1320.00

    def __init__(self, nome, cpf, salario):
        if salario < self.SALARIO_MINIMO:
            raise ValueError("Salário CLT não pode ser menor que o mínimo.")
        super().__init__(nome, cpf, salario)
        self.tipo = "CLT"

    def calcular_beneficios(self):
        return super().calcular_beneficios() + (0.06 * self.salario)
