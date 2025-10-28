from models.funcionario_clt import FuncionarioCLT
from models.funcionario_pj import FuncionarioPJ
from models.folha_salarial import FolhaSalarial

def exibir_menu():
    print("\n=== SISTEMA DE FOLHA SALARIAL ===")
    print("1. Adicionar funcionário CLT")
    print("2. Adicionar funcionário PJ")
    print("3. Listar funcionários")
    print("4. Mostrar total da folha")
    print("5. Mostrar total de benefícios")
    print("0. Sair")

def main():
    folha = FolhaSalarial()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            salario = float(input("Salário: "))
            try:
                f = FuncionarioCLT(nome, cpf, salario)
                folha.adicionar_funcionario(f)
                print(f"Funcionário CLT {nome} adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            cnpj = input("CNPJ: ")
            salario = float(input("Salário: "))
            f = FuncionarioPJ(nome, cpf, cnpj, salario)
            folha.adicionar_funcionario(f)
            print(f"Funcionário PJ {nome} adicionado com sucesso!")

        elif opcao == "3":
            print("\n--- Funcionários cadastrados ---")
            for func in folha.funcionarios:
                dados = folha.obter_funcionario(func.cpf)
                print(f"{func.nome} | CPF: {dados['cpf']} | "
                      f"Salário: R$ {dados['salario']:.2f} | "
                      f"Benefícios: R$ {dados['beneficios']:.2f} | "
                      f"Tipo: {dados['tipo']}")

        elif opcao == "4":
            print(f"\n Total da folha: R$ {folha.total_folha():.2f}")

        elif opcao == "5":
            print(f"\n Total de benefícios: R$ {folha.total_beneficios():.2f}")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
