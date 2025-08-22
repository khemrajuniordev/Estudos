# 3. Veículos
# Crie uma classe Veiculo com atributos marca e modelo.
#  Depois crie duas subclasses:
# Carro, que tem também portas.

# Moto, que tem também cilindradas.

# Crie métodos para mostrar as informações de cada veículo.
# Exemplo real:
# Todo veículo tem marca e modelo.

# Mas só carro tem portas, e só moto tem cilindradas.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def info_carro(self):
        print(f"O Carro da marca {self.marca} do modelo {self.modelo} com {self.portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def info_moto(self):
        print(f"A Moto da marca {self.marca} do modelo {self.modelo} com {self.cilindradas} cilindradas.")

Carro1 = Carro("Wolksvagem", "Modelo-S", "4 Portas")
Carro1.info_carro()

Moto1 = Moto("Yamaha", "Modelo-X", 150)
Moto1.info_moto()


