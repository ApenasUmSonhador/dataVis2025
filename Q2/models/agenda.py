from .contato import Contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        # 4.1: não pode adicionar contato sem telefone
        if not contato.telefones:
            raise ValueError("Não é possível adicionar um contato sem telefone.")
        self.contatos.append(contato)

    def remover_contato(self, nome):
        self.contatos = [c for c in self.contatos if c.nome != nome]

    def listar_contatos(self):
        # 4.2: listar em ordem alfabética
        return sorted(self.contatos, key=lambda c: c.nome)

    def buscar_contato(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                return c
        return None
