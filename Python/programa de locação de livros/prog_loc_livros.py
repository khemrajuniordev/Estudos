# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Alugado"
        return f"{self.titulo} - {self.autor} ({status})"


# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_alugados = []

    def __str__(self):
        return f"Usuário: {self.nome}, Livros alugados: {[livro.titulo for livro in self.livros_alugados]}"


# Classe Sistema (responsável por gerenciar tudo)
class SistemaLocadora:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    # Cadastrar usuário
    def cadastrar_usuario(self, nome):
        usuario = Usuario(nome)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    # Listar usuários
    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios:
                print(usuario)
        pause()

    # Cadastrar livro
    def cadastrar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso!")

    # Listar livros
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
        else:
            for livro in self.livros:
                print(livro)
        pause()

    # Alugar livro
    def alugar_livro(self, nome_usuario, titulo_livro):
        # Buscar usuário
        usuario = next((u for u in self.usuarios if u.nome == nome_usuario), None)
        # Buscar livro
        livro = next((l for l in self.livros if l.titulo == titulo_livro and l.disponivel), None)

        if usuario and livro:
            livro.disponivel = False
            usuario.livros_alugados.append(livro)
            print(f"{usuario.nome} alugou o livro '{livro.titulo}'")
        else:
            print("Usuário ou livro inválido, ou livro indisponível.")


# ---------------- PROGRAMA PRINCIPAL ----------------
def main():
    sistema = SistemaLocadora()

    while True:
        print("\n===== LOCADORA DE LIVROS =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Cadastrar livro")
        print("4 - Listar livros")
        print("5 - Alugar livro")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do usuário: ")
            sistema.cadastrar_usuario(nome)
        elif opcao == "2":
            sistema.listar_usuarios()
        elif opcao == "3":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            sistema.cadastrar_livro(titulo, autor)
        elif opcao == "4":
            sistema.listar_livros()
        elif opcao == "5":
            nome_usuario = input("Nome do usuário: ")
            titulo_livro = input("Título do livro: ")
            sistema.alugar_livro(nome_usuario, titulo_livro)
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


# Executar o programa
if __name__ == "__main__":
    main()
