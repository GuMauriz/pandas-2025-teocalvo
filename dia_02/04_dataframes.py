# %%

import pandas as pd
import openpyxl

# %%

# Carregar o arquivo CSV com separador ponto e vírgula
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")

# Ver as cinco primeiras linhas por padrão
df_clientes.head()

# %%

# Ver as cinco últimas linhas por padrão
df_clientes.tail()

# %%

# Pegar uma amostra aleatória de 10 linhas
df_clientes.sample(10)

# %%

# Ver o número de linhas e colunas
print("Número de linhas no df: ", df_clientes.shape[0])
print("Número de colunas no df: ", df_clientes.shape[1])

# %%

# Ver os nomes das colunas
df_clientes.columns

# %%

# Verificar os índices
df_clientes.index

# %%

# Verificar o tipo de dados de cada coluna
df_clientes.dtypes

# %%

# Verificar o tipo de dados da última coluna
df_clientes.dtypes.iloc[-1]

# %%

# Verificar informações gerais do DataFrame
df_clientes.info(memory_usage="deep")