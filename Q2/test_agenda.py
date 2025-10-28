import unittest
from models.agenda import Agenda
from models.contato import Contato

class TestAgenda(unittest.TestCase):

    def test_nao_adicionar_contato_sem_telefone(self):
        contato = Contato("Maicon")
        agenda = Agenda()
        with self.assertRaises(ValueError):
            agenda.adicionar_contato(contato)

    def test_adicionar_e_listar_contato(self):
        contato = Contato("Fulano de Tal")
        contato.adicionar_telefone("casa", "88 99999-8888")
        agenda = Agenda()
        agenda.adicionar_contato(contato)
        contatos = agenda.listar_contatos()
        self.assertEqual(len(contatos), 1)
        self.assertEqual(contatos[0].nome, "Fulano de Tal")

    def test_remover_contato(self):
        contato = Contato("Fulano")
        contato.adicionar_telefone("trabalho", "85 88888-7777")
        agenda = Agenda()
        agenda.adicionar_contato(contato)
        agenda.remover_contato("Fulano")
        self.assertEqual(len(agenda.contatos), 0)

    def test_remover_telefone_do_contato(self):
        contato = Contato("Daniella")
        contato.adicionar_telefone("casa", "85 11111-2222")
        contato.adicionar_telefone("trabalho", "85 33333-4444")
        contato.remover_telefone("casa")
        telefones = contato.listar_telefones()
        self.assertEqual(len(telefones), 1)
        self.assertIn("trabalho", telefones[0])

    def test_listar_contatos_ordenados(self):
        c1 = Contato("Zezin")
        c1.adicionar_telefone("casa", "11 1111-1111")
        c2 = Contato("Daniella")
        c2.adicionar_telefone("trabalho", "22 2222-2222")

        agenda = Agenda()
        agenda.adicionar_contato(c1)
        agenda.adicionar_contato(c2)
        contatos = agenda.listar_contatos()
        nomes = [c.nome for c in contatos]
        self.assertEqual(nomes, ["Daniella", "Zezin"])

if __name__ == "__main__":
    unittest.main()
