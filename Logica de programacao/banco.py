# 4. Banco Digital
# Crie uma classe Conta com atributos titular e saldo.
# Depois crie duas subclasses:
# ContaCorrente, que tem limite de cheque especial.
# ContaPoupanca, que rende juros.
# Crie métodos para depositar() e sacar().
# Depois teste criando uma conta corrente e uma conta poupança.
# Exemplo real:
# Conta é genérica.
# Conta corrente → tem cheque especial.
# Conta poupança → rende juros.

class Conta:
    def __init__(self, titular, saldo, numero_da_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_da_conta = numero_da_conta

    def depositar(self):
        valor = float(input("Qual valor deseja depositar: "))
        self.saldo += valor
        print(f"Valor de {valor} adicionado ao seu saldo, o valor atual é: {self.saldo}")

    def sacar(self):
        valor = float(input("Qual valor você quer sacar: "))
        if self.saldo < valor:
            print("Seu saldo é insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque no valor de: {valor} foi realizado com sucesso")
            print(f"O seu saldo atual é de: {self.saldo}")

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, numero_da_conta, limite_cheque_especial):
        super().__init__(titular, saldo, numero_da_conta)
        self.limite_cheque_especial = limite_cheque_especial

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, numero_da_conta, rende_juros):
        super().__init__(titular, saldo, numero_da_conta)
        self.rende_juros = rende_juros



cc = ContaCorrente("Carlos", 1000, "12345-6", 500)
cc.depositar()
cc.sacar()