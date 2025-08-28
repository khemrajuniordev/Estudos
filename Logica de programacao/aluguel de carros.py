TABELA_PRECOS = {
    "economico": {"diaria": 120.0, "por_km": 0.5},
    "suv": {"diaria": 200.0, "por_km": 0.8},
    "luxo": {"diaria": 350.0, "por_km": 1.2},
}

class Carro:
    def __init__(self, placa, modelo, categoria, odometro=0):
        self.placa = placa.strip().upper()
        self.modelo = modelo.strip()
        self.categoria = categoria.strip().lower()
        self.odometro = float(odometro)
        self.disponivel = True

    def __str__(self):
        s = "Disponível" if self.disponivel else "Indisponível"
        return f"[{self.placa}] {self.modelo} | {self.categoria} | {self.odometro:.0f} km | {s}"

class Cliente:
    def __init__(self, nome, documento):
        self.nome = nome.strip()
        self.documento = documento.strip().upper()

    def __str__(self):
        return f"{self.nome} (doc: {self.documento})"

class Aluguel:
    def __init__(self, carro, cliente, dias_contratados):
        self.carro = carro
        self.cliente = cliente
        self.dias_contratados = int(dias_contratados)
        self.km_inicial = carro.odometro
        self.km_final = None
        self.valor_total = None
        self.aberto = True

    def calcular_valor(self, km_final):
        p = TABELA_PRECOS[self.carro.categoria]
        km_rodados = km_final - self.km_inicial
        if km_rodados < 0:
            km_rodados = 0
        return (self.dias_contratados * p["diaria"]) + (km_rodados * p["por_km"])

    def devolver(self, km_final):
        self.km_final = float(km_final)
        self.valor_total = self.calcular_valor(self.km_final)
        self.aberto = False
        self.carro.odometro = self.km_final
        self.carro.disponivel = True

    def __str__(self):
        s = "ABERTO" if self.aberto else "FECHADO"
        base = f"Aluguel [{s}] - Carro: {self.carro.placa} - Cliente: {self.cliente.documento}"
        if not self.aberto:
            base += f" | Dias: {self.dias_contratados} | Km: {self.km_inicial:.0f}->{self.km_final:.0f} | Total: R$ {self.valor_total:.2f}"
        return base

class SistemaLocadora:
    def __init__(self):
        self.frota = {}
        self.clientes = {}
        self.alugueis = []

    def cadastrar_carro(self, placa, modelo, categoria, odometro=0):
        if categoria.strip().lower() not in TABELA_PRECOS:
            print("Categoria inválida.")
            return None
        if placa.strip().upper() in self.frota:
            print("Placa já cadastrada.")
            return None
        c = Carro(placa, modelo, categoria, odometro)
        self.frota[c.placa] = c
        return c

    def listar_carros_disponiveis(self):
        return [c for c in self.frota.values() if c.disponivel]

    def cadastrar_cliente(self, nome, documento):
        doc = documento.strip().upper()
        if doc in self.clientes:
            print("Cliente já cadastrado.")
            return None
        cli = Cliente(nome, doc)
        self.clientes[doc] = cli
        return cli

    def alugar(self, placa, documento, dias_contratados):
        p = placa.strip().upper()
        d = documento.strip().upper()
        if p not in self.frota:
            print("Carro não encontrado.")
            return None
        if d not in self.clientes:
            print("Cliente não encontrado.")
            return None
        carro = self.frota[p]
        if not carro.disponivel:
            print("Carro indisponível.")
            return None
        alg = Aluguel(carro, self.clientes[d], dias_contratados)
        carro.disponivel = False
        self.alugueis.append(alg)
        return alg

    def devolver(self, placa, km_final):
        p = placa.strip().upper()
        alvo = None
        for a in self.alugueis:
            if a.carro.placa == p and a.aberto:
                alvo = a
                break
        if not alvo:
            print("Não há aluguel aberto para essa placa.")
            return None
        alvo.devolver(float(km_final))
        return alvo

    def listar_alugueis(self, somente_abertos=False):
        if somente_abertos:
            return [a for a in self.alugueis if a.aberto]
        return list(self.alugueis)

def menu():
    s = SistemaLocadora()
    while True:
        print("\n=== LOCADORA ===")
        print("1) Cadastrar carro")
        print("2) Cadastrar cliente")
        print("3) Listar carros disponíveis")
        print("4) Alugar carro")
        print("5) Devolver carro")
        print("6) Listar aluguéis")
        print("0) Sair")
        op = input("Escolha: ").strip()

        if op == "1":
            placa = input("Placa: ")
            modelo = input("Modelo: ")
            cat = input("Categoria (economico/suv/luxo): ")
            od = float(input("Odômetro (km): ") or "0")
            c = s.cadastrar_carro(placa, modelo, cat, od)
            if c: print("Carro cadastrado:", c)

        elif op == "2":
            nome = input("Nome: ")
            doc = input("Documento: ")
            cli = s.cadastrar_cliente(nome, doc)
            if cli: print("Cliente cadastrado:", cli)

        elif op == "3":
            disp = s.listar_carros_disponiveis()
            if not disp:
                print("Nenhum carro disponível.")
            else:
                for c in disp:
                    print("-", c)

        elif op == "4":
            placa = input("Placa: ")
            doc = input("Documento do cliente: ")
            dias = int(input("Dias: "))
            a = s.alugar(placa, doc, dias)
            if a:
                print("Aluguel aberto.")
                print("Carro:", a.carro)
                print("Cliente:", a.cliente)
                print("Dias:", a.dias_contratados, "| Km inicial:", int(a.km_inicial))

        elif op == "5":
            placa = input("Placa: ")
            kmf = float(input("Odômetro final: "))
            a = s.devolver(placa, kmf)
            if a:
                print("Devolução feita.")
                print("Carro:", a.carro.placa, a.carro.modelo)
                print("Cliente:", a.cliente.nome, a.cliente.documento)
                print("Dias:", a.dias_contratados)
                print("Km:", int(a.km_inicial), "->", int(a.km_final))
                print("Total: R$", f"{a.valor_total:.2f}")

        elif op == "6":
            todos = s.listar_alugueis(False)
            if not todos:
                print("Nenhum aluguel.")
            else:
                for a in todos:
                    print("-", a)

        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
