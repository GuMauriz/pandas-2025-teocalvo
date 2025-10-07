# %%

import pandas as pd

# %%

# Copiando dados da área de transferência (clipboard)
# Precisa copiar os dados antes de rodar essa célula

# ,idCliente,flEmail,flTwitch,flYouTube,flBlueSky,flInstagram,qtdePontos,DtCriacao,DtAtualizacao
# 0,000ff655-fa9f-4baa-a108-47f581ec52a1,0,0,0,0,0,25086,2024-02-01 00:00:00.000,2025-09-26 13:28:37.697
# 1,001749bd-37b5-4b1e-8111-f9fbba90f530,0,0,0,0,0,50,2024-02-01 00:00:00.000,2024-02-01 00:00:00.000
# 2,0019bb9e-26d4-4ebf-8727-fc911ea28a92,0,0,0,0,0,2,2024-02-01 00:00:00.000,2024-02-01 00:00:00.000

df = pd.read_clipboard(sep = ',')
df