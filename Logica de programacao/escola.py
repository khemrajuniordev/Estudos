# 5. Escola
# Crie uma classe Pessoa com atributos nome e idade.
#  Depois crie duas subclasses:
# Professor, com atributo materia.

# Aluno, com atributo serie.

# Faça uma função que imprime uma frase diferente para professor e aluno, tipo:
# "O professor Carlos ensina Matemática."

# "O aluno João está na 5ª série."

# 👉 Exemplo real:
# Pessoa é genérica.

# Professor ensina.

# Aluno estuda.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia

    def falar(self):
        print(f"O professor {self.nome} ensina {self.materia}.")

class Aluno(Pessoa):
    def __init__(self, nome, idade, serie):
        super().__init__(nome, idade)
        self.serie = serie

    def falar(self):
        print(f"O aluno {self.nome} está na {self.serie}.")

Junior = Professor("Junior", 40, "Informática")
Junior.falar()

Ramesar = Aluno("Ramesar", 15, "1º Ano")
Ramesar.falar()