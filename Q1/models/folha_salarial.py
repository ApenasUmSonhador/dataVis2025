class FolhaSalarial:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def obter_funcionario(self, cpf):
        for f in self.funcionarios:
            if f.cpf == cpf:
                return {"cpf": f.cpf, "salario": f.salario, "beneficios": f.calcular_beneficios()}
        return None

    def total_folha(self):
        return sum(f.salario for f in self.funcionarios)

    def total_beneficios(self):
        return sum(f.calcular_beneficios() for f in self.funcionarios)
