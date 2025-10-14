# %%
import pandas as pd
# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%
# Agrupando por clientes e contando todas as linhas
df.groupby(by=["IdCliente"]).count()
# %%
# Agrupando por clientes e contando todas as transacoes
df.groupby(by=["IdCliente"])["IdTransacao"].count()
# %%
# O exemplo acima retorna uma Series, para retornar um DataFrame
df.groupby(by=["IdCliente"])[["IdTransacao"]].count()
# %%
# O exemplo acima faz com que o índice seja o IdCliente
# Para resetar o índice
df.groupby(by=["IdCliente"])[["IdTransacao"]].count().reset_index()
# %%
# Ou
df.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%
# Agrupando por clientes e mostrando:
# - Quantidade de transações
# - Soma dos pontos
# - Média dos pontos

summary = df.groupby(by=["IdCliente"], as_index=False).agg(
    {"IdTransacao": ["count"],
    "QtdePontos": ["sum", "mean"]}
)
# %%
# Ajustando os nomes das colunas para evitar MultiIndex
summary.columns = ["IdCliente", "QtdeTransacoes", "TotalPontos", "MediaPontos"]
summary.head()