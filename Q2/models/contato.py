from .telefone import Telefone

class Contato:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = []

    def adicionar_telefone(self, identificador, numero):
        telefone = Telefone(identificador, numero)
        self.telefones.append(telefone)

    def remover_telefone(self, identificador):
        self.telefones = [t for t in self.telefones if t.identificador != identificador]

    def listar_telefones(self):
        return [f"{t.identificador}: {t.numero}" for t in self.telefones]

    def __str__(self):
        telefones_str = ", ".join(self.listar_telefones())
        return f"{self.nome} -> {telefones_str}"
