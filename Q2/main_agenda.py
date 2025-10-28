from models.telefone import Telefone
from models.contato import Contato
from models.agenda import Agenda

def exibir_menu():
    print("\n=== AGENDA TELEFÔNICA ===")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Remover contato")
    print("4. Buscar contato")
    print("0. Sair")

def main():
    agenda = Agenda()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do contato: ")
            contato = Contato(nome)

            while True:
                identificador = input("Identificador (ex: casa, trabalho): ")
                numero = input("Número (ex: 88 99999-8888): ")
                contato.adicionar_telefone(identificador, numero)
                mais = input("Adicionar outro telefone? (s/n): ").lower()
                if mais != "s":
                    break

            try:
                agenda.adicionar_contato(contato)
                print(f"Contato {nome} adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif opcao == "2":
            contatos = agenda.listar_contatos()
            if not contatos:
                print("Nenhum contato na agenda.")
            else:
                print("\n--- Lista de contatos ---")
                for c in contatos:
                    print(c)

        elif opcao == "3":
            nome = input("Nome do contato a remover: ")
            agenda.remover_contato(nome)
            print(f"Contato '{nome}' removido (se existia).")

        elif opcao == "4":
            nome = input("Nome para buscar: ")
            contato = agenda.buscar_contato(nome)
            if contato:
                print(f"\n{contato}")
            else:
                print("Contato não encontrado.")

        elif opcao == "0":
            print("Encerrando a agenda...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
