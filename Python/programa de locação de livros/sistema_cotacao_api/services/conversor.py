# Aqui vamos colocar funções para trabalhar com os valores lidos do TXT
def converter_valores(valores, taxa):
    """
    valores: lista de números (valores na moeda de origem)
    taxa: taxa de conversão (cotação da moeda)
    """
    # Multiplicamos cada valor pela taxa para converter
    # Exemplo real: cada preço em dólar vira preço em reais
    return [v * taxa for v in valores]


def ler_valores_txt(caminho):
    """
    Lê um arquivo .txt com valores (um por linha) e retorna uma lista de floats
    """
    with open(caminho, "r") as arquivo:
        # Lemos cada linha, tiramos espaços e transformamos em float
        return [float(linha.strip()) for linha in arquivo if linha.strip()]
