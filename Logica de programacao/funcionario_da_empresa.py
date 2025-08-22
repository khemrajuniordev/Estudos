class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

class Programador(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

#criando objetos
Principal = Funcionario("Junior", 1500)
Diretor = Gerente("Ramesar", 2500, "Masculino")
Lider = Programador("Khemraj", 5500, "Javascript" )


print(f"Nome do Principal: {Principal.nome}, Seu salário é de: {Principal.salario}")
print(f"Nome do Diretor é:  {Diretor.nome}, Seu salário é de: {Diretor.salario} e trabalha no departamento: {Diretor.departamento}")
print(f"Nome do Lider é:  {Lider.nome}, Seu salário é de: {Lider.salario} e trabalha no departamento:{Lider.linguagem}")