Projeto de Coleta de Cotações de Ativos
Este projeto faz parte da Jornada de Dados e tem como objetivo coletar, consolidar e salvar cotações em tempo real de Bitcoin e de commodities selecionadas, utilizando APIs públicas e a biblioteca yfinance.

📂 Estrutura do Projeto
GetBitcoin.py
Script responsável por coletar a cotação atual do Bitcoin em USD.

Fonte: API pública da Coinbase.

Retorna um DataFrame padronizado com as colunas:

ativo — símbolo do ativo (BTC-USD)
preco — preço atual
moeda — moeda de cotação (USD)
horario_coleta — horário local da coleta
Pode ser executado de forma independente (python GetBitcoin.py) para teste.

GetCommodities.py
Script responsável por coletar a última cotação de commodities em USD, no intervalo de 1 minuto.

Fonte: Yahoo Finance via biblioteca yfinance.

Lista de ativos incluídos por padrão:

GC=F — Ouro
CL=F — Petróleo WTI
SI=F — Prata
Retorna um DataFrame padronizado com as colunas:

ativo — símbolo do ativo
preco — preço atual
moeda — moeda de cotação (USD)
horario_coleta — horário local da coleta
Pode ser executado de forma independente (python GetCommodities.py) para teste.

GetPrices.py
Script orquestrador que combina os resultados de GetBitcoin e GetCommodities.

Três variações disponíveis:

Execução única — junta e imprime o DataFrame.
Loop infinito — coleta e imprime a cada 60 segundos.
Loop infinito com salvamento — coleta a cada 60 segundos e salva/append em um arquivo CSV consolidado (cotacoes.csv).
🚀 Como Executar
Instalar dependências:

pip install pandas yfinance requests
Rodar a coleta de Bitcoin:

python GetBitcoin.py
Rodar a coleta de Commodities:

python GetCommodities.py
Rodar a coleta consolidada (exemplo com salvamento a cada 60s):

python GetPrices_loop_save.py
📊 Objetivo Futuro
Os dados coletados serão utilizados para:

Calcular KPIs diários como lucro/prejuízo.
Avaliar variação de preços.
Criar dashboards de acompanhamento.
