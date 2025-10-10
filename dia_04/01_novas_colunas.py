# %%

import numpy as np
import pandas as pd

# %%

# Carregando o dataset
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes.head()

# %%

# Acrescentar 100 pontos para cada cliente
df_clientes["qtdePontosMaisCem"] = df_clientes["qtdePontos"] + 100
df_clientes.head()

# %%

# Coluna que informa se o cliente tem email ou twitch
df_clientes["emailTwitch"] = df_clientes["flEmail"] | df_clientes["flTwitch"]
df_clientes.head()

# %%

# Coluna que informa se o cliente tem email E twitch
df_clientes["emailETwitch"] = df_clientes["flEmail"] & df_clientes["flTwitch"]
df_clientes.head()

# %%

# Testando filtro na nova coluna
df_email_e_tw = df_clientes[df_clientes["emailETwitch"] == True]
df_email_e_tw

# %%

# Estatísticas descritivas da coluna qtdePontos
df_clientes["qtdePontos"].describe()

# %%

# Aplicando uma transformação logarítmica na coluna qtdePontos
df_clientes["logQtdePontos"] = np.log(df_clientes["qtdePontos"] + 1)
df_clientes.head()

# Adiciona-se 1 para evitar log(0)

# %%

# A transformação logarítmica é útil para reduzir o impacto de valores extremos
# e tornar a distribuição dos dados mais próxima de uma distribuição normal ou
# de um requisito/técnica que se usa.

import matplotlib.pyplot as plt

plt.hist(df_clientes["qtdePontos"])
plt.title("Distribuição original de qtdePontos")
plt.grid(True)
plt.show()

plt.hist(df_clientes["logQtdePontos"])
plt.title("Distribuição logarítmica de qtdePontos")
plt.grid(True)
plt.show()