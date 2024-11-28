class Candidato:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome
        self.votos = 0


def votar(candidatos):
    try:
        voto = int(input("Digite o número do candidato (1 a 99): "))
    except ValueError:
        print("Número inválido! Digite apenas números.")
        return 0

    encontrado = False
    for candidato in candidatos:
        if candidato.numero == voto:
            candidato.votos += 1
            encontrado = True
            print(f"Voto computado para {candidato.nome}")
            return 1  

    if not encontrado:
        print("Número de candidato inválido!")  

    return 0  


def apurar_votos(candidatos):
    print("\nResultado da apuração de votos:")
    for candidato in candidatos:
        print(f"{candidato.nome} (Número {candidato.numero}): {candidato.votos} votos")


def percentual_votos(candidatos, total_votos):
    if total_votos == 0:
        print("Nenhum voto computado ainda.")  
        return

    print("\nPercentual de votos:")
    for candidato in candidatos:
        percentual = (candidato.votos * 100) / total_votos  
        print(f"{candidato.nome}: {percentual:.2f}% dos votos")


def main():
    candidatos = [
        Candidato(1, "Candidato A"),
        Candidato(2, "Candidato B"),
        Candidato(3, "Candidato C")
    ]

    total_votos = 0

    while True:
        print("\nMenu:")
        print("1. Votar")
        print("2. Apurar votos")
        print("3. Emitir percentual de votos")
        print("4. Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite apenas números.")
            continue

        if opcao == 1:
            total_votos += votar(candidatos)  
        elif opcao == 2:
            apurar_votos(candidatos)
        elif opcao == 3:
            percentual_votos(candidatos, total_votos)
        elif opcao == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
