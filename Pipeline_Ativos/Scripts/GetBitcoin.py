import requests
from datetime import datetime
import pandas as pd



def get_bitcoin_df() -> pd.DataFrame:
    # URL da API da Coinbase para o preço spot do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"

    #Requisição GET para API do BitCoin
    response = requests.get(url)
    #Guardar a resposta em uma variável
    data = response.json()

    #Extrair os dados relevantes
    preco = float(data['data']['amount'])
    ativo = data['data']['base']      # "BTC"
    moeda = data['data']['currency']  # "USD"
    horario_de_coleta = datetime.now()

    # Criar DataFrame no padrão em português
    df = pd.DataFrame([{
        'ativo': ativo,
        'preco': preco,
        'moeda': moeda,
        'horario_coleta': horario_de_coleta

    }])

    return df

if __name__ == "__main__":
    df = get_bitcoin_df()
    print(df)
    print("✅ Cotação do Bitcoin obtida com sucesso!")
