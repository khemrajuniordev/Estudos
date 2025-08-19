import os
from services.api_cotacao import pegar_cotacao
from services.conversor import ler_valores_txt, converter_valores

if __name__ == "__main__":
    moeda_origem = "USD"
    moeda_destino = "BRL"

    cotacao = pegar_cotacao(moeda_origem, moeda_destino)
    if cotacao is None:
        print("❌ Não foi possível obter a cotação. Tente novamente mais tarde.")
    else:
        print(f"Cotação atual: 1 {moeda_origem} = {cotacao:.2f} {moeda_destino}")

        # Caminho absoluto relativo ao script
        caminho_arquivo = os.path.join(os.path.dirname(__file__), "data", "valores.txt")
        valores_usd = ler_valores_txt(caminho_arquivo)

        print("Valores lidos do arquivo:", valores_usd)

        valores_convertidos = converter_valores(valores_usd, cotacao)

        print(f"\nValores convertidos para {moeda_destino}:")
        for original, convertido in zip(valores_usd, valores_convertidos):
            print(f"{original:.2f} {moeda_origem} = {convertido:.2f} {moeda_destino}")
