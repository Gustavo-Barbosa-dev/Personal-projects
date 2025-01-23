class Livro:
    def __init__(self, codigo, titulo, autor, area, ano, editora):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.area = area
        self.ano = ano
        self.editora = editora

def cadastrar_livro():
    print("Digite o código do livro: ")
    codigo = int(input())
    print("Digite o título do livro: ")
    titulo = input().strip()
    print("Digite o nome do autor: ")
    autor = input().strip()
    print("Digite a área do livro: ")
    area = input().strip()
    print("Digite o ano: ")
    ano = int(input())
    print("Digite o nome da editora: ")
    editora = input().strip()
    return Livro(codigo, titulo, autor, area, ano, editora)

def imprimir_livros(ficha):
    for livro in ficha:
        print(f"CÓDIGO: {livro.codigo}")
        print(f"TÍTULO: {livro.titulo}")
        print(f"AUTOR: {livro.autor}")
        print(f"ÁREA: {livro.area}")
        print(f"ANO: {livro.ano}")
        print(f"EDITORA: {livro.editora}\n")

def pesquisar_livro_por_codigo(ficha, busca):
    for livro in ficha:
        if livro.codigo == busca:
            print(f"CÓDIGO: {livro.codigo}")
            print(f"TÍTULO: {livro.titulo}")
            print(f"AUTOR: {livro.autor}")
            print(f"ÁREA: {livro.area}")
            print(f"ANO: {livro.ano}")
            print(f"EDITORA: {livro.editora}\n")
            return
    print("Livro não encontrado.")

def ordenar_livros_por_ano(ficha):
    ficha.sort(key=lambda livro: livro.ano)

def main():
    ficha = []
    op = 0
    while op != 5:
        print("1 - Cadastrar um livro")
        print("2 - Imprimir os livros cadastrados")
        print("3 - Pesquisar livros por código")
        print("4 - Ordenar os livros por ano")
        print("5 - Sair")
        op = int(input("Digite a opção desejada: "))

        if op == 1:
            livro = cadastrar_livro()
            ficha.append(livro)
        elif op == 2:
            imprimir_livros(ficha)
        elif op == 3:
            busca = int(input("Digite o código que deseja buscar: "))
            pesquisar_livro_por_codigo(ficha, busca)
        elif op == 4:
            ordenar_livros_por_ano(ficha)

if __name__ == "__main__":
    main()
