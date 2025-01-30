import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
ARQUIVO_CSV = ROOT_PATH / "lista_mercado.csv"

COLUNA_ITEM = 0
COLUNA_QUANTIDADE = 1

def adicionar_itens():
    print("\n-- Adicionar itens a lista --")
    item = input("Item: ")
    quantidade = input("Quantidade: ")

    try:
        with open(ARQUIVO_CSV, "a", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            escritor.writerow ([item, quantidade])
        print("Item adicionado com sucesso")
    except IOError as exc:
        print(f"Erro ao adicionar o item. {exc}")

def contar_itens():
    try:
        with open (ARQUIVO_CSV, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            registros = list(leitor)
            total = len(registros)
            print(f"\nTotal de itens cadastrados: {total}")
    except IOError as exc:
        print(f"Erro ao contar os itens. {exc}")

def mostrar_itens():
    try:
        with open(ARQUIVO_CSV, "r", newline="", encoding="utf-8") as arqruivo:
            leitor = csv.reader(arqruivo)
            registros = list(leitor)
            if not registros:
                print("\nNenhum registro encontrado.")
                return
            print("\n-- Lista de itens presentes na lista --")
            for idx, row in enumerate(registros):
                print(f"Registro {idx + 1}:")
                print(f"ID: {row[COLUNA_ITEM]}")
                print(f"Nome: {row[COLUNA_QUANTIDADE]}")
                print("-" * 20)
    except IOError as exc:
        print(f"Erro ao ler o arquivo. {exc}")

def menu():
    while True:
        print("\n-- Menu --")
        print("1. Adicionar Item")
        print("2. Contar Itens")
        print("3. Mostrar lista do mercado")
        print("4. Sair")
        opcao = input("Escolha uma das opções: ").strip()

        if opcao == "1":
            adicionar_itens()
        elif opcao == "2":
            contar_itens()
        elif opcao == "3":
            mostrar_itens()
        elif opcao == "4":
            print("Fechando o sistema...")
            print("Sistema fechado!")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    menu()
