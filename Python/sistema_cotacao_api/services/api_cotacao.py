import requests

def pegar_cotacao(base, destino):
    """
    Busca a cotação (sem API key) usando open.er-api.com.
    Retorna taxa de câmbio (float) ou None se falhar.
    """
    # Faz a ligação para pegar as taxas da base para todas as moedas
    url = f"https://open.er-api.com/v6/latest/{base}"
    resposta = requests.get(url)
    
    try:
        dados = resposta.json()
    except ValueError:
        print("❌ Erro: resposta não é um JSON válido.")
        return None
    
    # Verifica se a resposta diz 'success'
    if dados.get("result") != "success":
        print("❌ Erro: API não conseguiu retornar as taxas.")
        print(dados)
        return None
    
    # Checa se a moeda destino está presente nas taxas
    taxas = dados.get("rates", {})
    if destino not in taxas:
        print(f"❌ Erro: cotação de '{destino}' não encontrada.")
        print(dados)
        return None
    
    return taxas[destino]
