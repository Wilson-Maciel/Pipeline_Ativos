# GetPrices_loop_db.py
# A cada 60s: junta Bitcoin + Commodities e insere no PostgreSQL.

import time
import pandas as pd
from sqlalchemy import create_engine
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

# Configuração do banco (substituir com seus dados reais)
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")
port = os.getenv("port")
dbname = os.getenv("dbname")
# Criar conexão SQLAlchemy
DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(DATABASE_URL)

SLEEP_SECONDS = 60

if __name__ == "__main__":
    while True:
        # Coleta
        df_btc = get_bitcoin_df()
        df_comm = get_commodities_df()

        # Junta tudo
        df = pd.concat([df_btc, df_comm], ignore_index=True)

        # Salva no banco (append)
        df.to_sql("bronze_cotacoes", engine, if_exists="append", index=False)

        print("✅ Cotações inseridas no banco com sucesso!")

        # Espera próximo ciclo
        time.sleep(SLEEP_SECONDS)
