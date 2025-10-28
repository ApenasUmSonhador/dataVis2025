class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf # Todo funcionário tem um CPF
        self.salario = salario

    def calcular_beneficios(self):
        return 500.0  # auxílio-saúde
