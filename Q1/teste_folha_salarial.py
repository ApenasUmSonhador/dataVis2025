import unittest
from models.funcionario_clt import FuncionarioCLT
from models.funcionario_pj import FuncionarioPJ
from models.folha_salarial import FolhaSalarial

class TestFolhaSalarial(unittest.TestCase):

    def test_salario_minimo_clt(self):
        with self.assertRaises(ValueError):
            FuncionarioCLT("Arthur", "123", 1200)

    def test_beneficios_clt(self):
        f = FuncionarioCLT("Isaack", "111", 2000)
        self.assertAlmostEqual(f.calcular_beneficios(), 500 + 0.06 * 2000)

    def test_beneficios_pj(self):
        f = FuncionarioPJ("Gleidistonny", "222", "33.444.555/0001-00", 4000)
        self.assertEqual(f.calcular_beneficios(), 500)

    def test_folha_total(self):
        folha = FolhaSalarial()
        folha.adicionar_funcionario(FuncionarioCLT("Wesley", "111", 2000))
        folha.adicionar_funcionario(FuncionarioPJ("Victor", "222", "33.444.555/0001-00", 4000))
        self.assertEqual(folha.total_folha(), 6000)

    def test_total_beneficios(self):
        folha = FolhaSalarial()
        folha.adicionar_funcionario(FuncionarioCLT("Wesley", "111", 2000))
        folha.adicionar_funcionario(FuncionarioPJ("Victor", "222", "33.444.555/0001-00", 4000))
        total = (500 + 0.06 * 2000) + 500
        self.assertAlmostEqual(folha.total_beneficios(), total)

if __name__ == "__main__":
    unittest.main()
