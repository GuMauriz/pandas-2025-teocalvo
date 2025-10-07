# %%

import pandas as pd
import openpyxl

# %%

# Carregar o arquivo CSV com separador ponto e vírgula
df_transacoes = pd.read_csv("../data/transacoes.csv", sep = ";")
df_transacoes.head()

# %%

df_transacoes.info(memory_usage = "deep")

# %%

df_transacoes.dtypes

# %%

# Renomear colunas
renamed_columns = {
    "DtCriacao": "DataCriacao",
    "DescSistemaOrigem": "SistemaOrig"}
# Inplace=True faz a alteração no próprio DataFrame
df_transacoes.rename(columns=renamed_columns, inplace=True)
df_transacoes.head()

# %%

# Selecionar colunas específicas
# É necessário passar uma lista de colunas
df_transacoes[['IdCliente', 'QtdePontos']]

# %%

# Ordernar as colunas por ordem alfabética
columns = df_transacoes.columns.tolist()
columns.sort()
df_transacoes[columns]