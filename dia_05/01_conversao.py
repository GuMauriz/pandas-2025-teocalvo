# %%

import pandas as pd

# %%

# Dataset
df_clientes = pd.read_csv('../data/clientes.csv', sep = ";")
df_clientes.head()

# %%

# Convertendo a coluna qtdePontos (int) para o tipo float
df_clientes["qtdePontos"].astype(float)

# %%

# Convertendo a coluna DtCriacao (string/object) para o tipo datetime
df_clientes["DtCriacao"].astype("datetime64[ns]")

# %%

# Em casos de problemas, com datas inválidas,
# podemos usar o parâmetro errors = 'coerce'
df_clientes["DtCriacao"].astype("datetime64[ns]", errors = 'coerce')

# %%

# Ou então, usar o pd.to_datetime()
pd.to_datetime(df_clientes["DtCriacao"], errors = 'coerce')

# %%

# Caso eu deseje substituir alguns valores de uma coluna
# antes de fazer a conversão, posso usar o método .replace()
df_clientes["DtCriacao"].replace({
    "0000-00-00 00:00:00.000": "2024-02-01 00:00:00.000"
    }).astype("datetime64[ns]")

# O replace recebe um dicionário onde a chave é o valor
# que desejo substituir e o valor é o novo valor.

# %%

# Ao converter uma coluna para datetime, posso extrair
# informações como o ano, mês, dia, etc.

df_clientes["DtCriacao"] = pd.to_datetime(df_clientes["DtCriacao"], errors = 'coerce')
df_clientes["AnoCriacao"] = df_clientes["DtCriacao"].dt.year
df_clientes["MesCriacao"] = df_clientes["DtCriacao"].dt.month
df_clientes["DiaCriacao"] = df_clientes["DtCriacao"].dt.day
df_clientes["DiaSemanaCriacao"] = df_clientes["DtCriacao"].dt.day_name()
df_clientes.head()