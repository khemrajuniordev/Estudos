##🚗 Exercício: Sistema de Estacionamento
##Enunciado:

##Crie um programa para gerenciar um estacionamento:

##Crie uma classe Veiculo com os atributos: placa e modelo.

##Crie duas subclasses: Carro e Moto.

##Ambas devem sobrescrever (override) o método tipo():

##Carro → "Carro"

##Moto → "Moto"

##Crie a classe Estacionamento, que deve ter métodos para:

##Adicionar veículo.

##Listar veículos.

##Remover veículo pela placa.

##No programa principal, faça um menu com as opções:

##1 - Estacionar veículo

##2 - Listar veículos

##3 - Retirar veículo

##4 - Sair

#definimos uma classe chamada "veiculo"  para representar qualquer veículo generico.
# Exemplo real: pense na "ficha cadastral padrão" que a administração do estacionamento usa para qualquer tipo de veículo.
class Veiculo:
 # O método especial __init__ é o "construtor"; ele roda quando criamos um novo Veiculo.
    # Exemplo real: é como preencher a ficha do veículo na recepção assim que ele entra.
    def __init__(self, placa, modelo):
        # Guardamos a placa recebida no atributo 'placa' do objeto.
        # Exemplo real: anotar a placa "ABC-1234" na ficha.
        self.placa = placa
        # Guardamos o modelo recebido no atributo 'modelo' do objeto.
        # Exemplo real: anotar o modelo "Fiat Uno" na mesma ficha.
        self.modelo = modelo


  # Definimos um método chamado 'tipo' que descreve que tipo de veículo é.
    # Exemplo real: um campo da ficha dizendo "Tipo do veículo".
    def tipo(self):
        # Retornamos a string "Veículo" como valor padrão (genérico).
        # Exemplo real: se ninguém disser o tipo específico, fica marcado apenas como "Veículo".
        return "Veículo"

# Criamos uma subclasse chamada "Carro" que herda (pega) tudo que existe em Veiculo.
# Exemplo real: é como ter uma ficha padrão, mas com uma etiqueta extra dizendo "Carro".
class Carro(Veiculo):
    # Sobrescrevemos (override) o método 'tipo' para retornar "Carro".
    # Exemplo real: na ficha do carro, o campo "Tipo do veículo" fica sempre "Carro".
    def tipo(self):
        # Devolve a palavra "Carro" quando perguntarem o tipo.
        # Exemplo real: o atendente olha a ficha e lê "Tipo: Carro".
        return "Carro"


# Criamos outra subclasse chamada "Moto" que também herda de Veiculo.
# Exemplo real: outra ficha com etiqueta extra dizendo "Moto".
class Moto(Veiculo):
    # Também sobrescrevemos o método 'tipo', agora para "Moto".
    # Exemplo real: na ficha da moto, o campo "Tipo do veículo" fica sempre "Moto".
    def tipo(self):
        # Devolve a palavra "Moto" quando perguntarem o tipo.
        # Exemplo real: o atendente confere e lê "Tipo: Moto".
        return "Moto"


# Este bloco garante que o código abaixo só rode quando o arquivo for executado diretamente.
# Exemplo real: como uma ordem de serviço que só é executada quando você abre esse formulário específico,
# e não quando ele é apenas anexado por outro setor.
if __name__ == "__main__":
    # Criamos um objeto 'carro1' da classe Carro com placa e modelo.
    # Exemplo real: um carro chega ao estacionamento e a recepção cria a ficha dele: placa "ABC-1234", modelo "Fiat Uno".
    carro1 = Carro("ABC-1234", "Fiat Uno")

    # Criamos um objeto 'moto1' da classe Moto com placa e modelo.
    # Exemplo real: uma moto chega e ganha a própria ficha: placa "XYZ-5678", modelo "Honda CG".
    moto1 = Moto("XYZ-5678", "Honda CG")

    # Imprimimos as informações do carro, consultando também o método tipo() sobrescrito.
    # Exemplo real: o atendente imprime uma etiqueta para colocar no para-brisa: "ABC-1234 | Fiat Uno | Carro".
    print(f"Placa: {carro1.placa} | Modelo: {carro1.modelo} | Tipo: {carro1.tipo()}")

    # Imprimimos as informações da moto, consultando o método tipo() da classe Moto.
    # Exemplo real: a etiqueta da moto mostra "XYZ-5678 | Honda CG | Moto".
    print(f"Placa: {moto1.placa} | Modelo: {moto1.modelo} | Tipo: {moto1.tipo()}")

    # Saída esperada no terminal:
    # Placa: ABC-1234 | Modelo: Fiat Uno | Tipo: Carro
    # Placa: XYZ-5678 | Modelo: Honda CG | Tipo: Moto