import os
import platform
import time

# ======== Config ========
APP_TITLE = "LOCADORA DE LIVROS"
BOX_WIDTH = 64
USE_COLORS = True  # desative para 100% preto-e-branco

# ======== Cores (opcional) ========
try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
except Exception:
    USE_COLORS = False
    class Fore:
        GREEN = YELLOW = RED = CYAN = ""
    class Style:
        BRIGHT = RESET_ALL = ""

# ======== Util ========
def limpar_tela():
    os.system("cls" if platform.system() == "Windows" else "clear")

def linha_horizontal(char="-"):
    return char * BOX_WIDTH

def box_top():
    return "+" + ("-" * (BOX_WIDTH - 2)) + "+"

def box_bottom():
    return "+" + ("-" * (BOX_WIDTH - 2)) + "+"

def box_line(text=""):
    # recorta ou preenche com espaços
    txt = text[:(BOX_WIDTH - 4)]
    padding = " " * ((BOX_WIDTH - 4) - len(txt))
    return f"| {txt}{padding} |"

def box_titulo(titulo):
    limpar_tela()
    print(box_top())
    mid = (BOX_WIDTH - 2 - len(titulo)) // 2
    esquerda = " " * mid
    direita = " " * ((BOX_WIDTH - 2) - len(titulo) - mid)
    print(f"|{esquerda}{titulo}{direita}|")
    print(box_bottom())

def box_bloco(titulo, linhas):
    print(box_top())
    print(box_line(titulo))
    print(box_line(linha_horizontal("=")))
    for ln in linhas:
        for sub in quebrar_linha(ln, BOX_WIDTH - 4):
            print(box_line(sub))
    print(box_bottom())

def quebrar_linha(texto, largura):
    # quebra palavras para caber no box
    palavras = str(texto).split()
    linhas, atual = [], ""
    for p in palavras:
        if len(atual) + (1 if atual else 0) + len(p) <= largura:
            atual = (atual + " " + p) if atual else p
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)
    if not linhas:
        linhas = [""]
    return linhas

def pause():
    print()
    input("[ENTER] para voltar ao menu...")

def ok(msg):
    if USE_COLORS:
        print(Fore.GREEN + msg + Style.RESET_ALL)
    else:
        print(msg)

def warn(msg):
    if USE_COLORS:
        print(Fore.YELLOW + msg + Style.RESET_ALL)
    else:
        print(msg)

def error(msg):
    if USE_COLORS:
        print(Fore.RED + msg + Style.RESET_ALL)
    else:
        print(msg)

# ======== Domínio ========
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponivel" if self.disponivel else "Alugado"
        return f"{self.titulo} - {self.autor} ({status})"

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_alugados = []

    def __str__(self):
        alugados = [livro.titulo for livro in self.livros_alugados]
        return f"Usuario: {self.nome} | Livros: {alugados}"

class SistemaLocadora:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_usuario(self, nome):
        if not nome.strip():
            error("Nome invalido.")
            return
        if any(u.nome.lower() == nome.lower() for u in self.usuarios):
            warn(f"Usuario '{nome}' ja existente.")
            return
        self.usuarios.append(Usuario(nome))
        ok(f"Usuario '{nome}' cadastrado com sucesso.")

    def listar_usuarios(self):
        if not self.usuarios:
            warn("Nenhum usuario cadastrado.")
            return
        for u in self.usuarios:
            print(f"- {u.nome} (alugados: {len(u.livros_alugados)})")

    def cadastrar_livro(self, titulo, autor):
        if not titulo.strip() or not autor.strip():
            error("Titulo/Autor invalidos.")
            return
        if any(l.titulo.lower() == titulo.lower() for l in self.livros):
            warn(f"Livro '{titulo}' ja cadastrado.")
            return
        self.livros.append(Livro(titulo, autor))
        ok(f"Livro '{titulo}' cadastrado com sucesso.")

    def listar_livros(self):
        if not self.livros:
            warn("Nenhum livro cadastrado.")
            return
        for l in self.livros:
            print(f"- {l}")

    def alugar_livro(self, nome_usuario, titulo_livro):
        usuario = next((u for u in self.usuarios if u.nome.lower() == nome_usuario.lower()), None)
        if not usuario:
            error("Usuario nao encontrado.")
            return
        livro = next((l for l in self.livros if l.titulo.lower() == titulo_livro.lower()), None)
        if not livro:
            error("Livro nao encontrado.")
            return
        if not livro.disponivel:
            warn("Livro indisponivel (ja alugado).")
            return
        livro.disponivel = False
        usuario.livros_alugados.append(livro)
        ok(f"'{livro.titulo}' alugado para {usuario.nome}.")

# ======== UI ========
def menu_principal():
    box_titulo(APP_TITLE)
    linhas = [
        "1 - Cadastrar usuario",
        "2 - Listar usuarios",
        "3 - Cadastrar livro",
        "4 - Listar livros",
        "5 - Alugar livro",
        "6 - Sair"
    ]
    box_bloco("MENU PRINCIPAL", linhas)
    print()
    return input("Selecione uma opcao: ").strip()

def tela_cadastrar_usuario(sis):
    box_titulo(APP_TITLE)
    box_bloco("CADASTRAR USUARIO", ["Informe os dados solicitados."])
    nome = input("Nome do usuario: ").strip()
    print()
    sis.cadastrar_usuario(nome)
    pause()

def tela_listar_usuarios(sis):
    box_titulo(APP_TITLE)
    linhas = []
    if not sis.usuarios:
        linhas.append("Nenhum usuario cadastrado.")
    else:
        for u in sis.usuarios:
            linhas.append(f"- {u.nome} | Alugados: {len(u.livros_alugados)}")
    box_bloco("USUARIOS", linhas)
    pause()

def tela_cadastrar_livro(sis):
    box_titulo(APP_TITLE)
    box_bloco("CADASTRAR LIVRO", ["Informe os dados solicitados."])
    titulo = input("Titulo do livro: ").strip()
    autor = input("Autor do livro: ").strip()
    print()
    sis.cadastrar_livro(titulo, autor)
    pause()

def tela_listar_livros(sis):
    box_titulo(APP_TITLE)
    if not sis.livros:
        box_bloco("LIVROS", ["Nenhum livro cadastrado."])
    else:
        linhas = [f"- {str(l)}" for l in sis.livros]
        box_bloco("LIVROS", linhas)
    pause()

def tela_alugar_livro(sis):
    box_titulo(APP_TITLE)
    box_bloco("ALUGAR LIVRO", ["Preencha os campos abaixo."])
    nome_usuario = input("Nome do usuario: ").strip()
    titulo_livro = input("Titulo do livro: ").strip()
    print()
    sis.alugar_livro(nome_usuario, titulo_livro)
    pause()

# ======== Main Loop ========
def main():
    sis = SistemaLocadora()
    while True:
        opcao = menu_principal()
        if   opcao == "1": tela_cadastrar_usuario(sis)
        elif opcao == "2": tela_listar_usuarios(sis)
        elif opcao == "3": tela_cadastrar_livro(sis)
        elif opcao == "4": tela_listar_livros(sis)
        elif opcao == "5": tela_alugar_livro(sis)
        elif opcao == "6":
            box_titulo(APP_TITLE)
            box_bloco("SAIR", ["Encerrando o sistema..."])
            time.sleep(0.6)
            break
        else:
            box_titulo(APP_TITLE)
            error("Opcao invalida.")
            pause()

if __name__ == "__main__":
    main()
