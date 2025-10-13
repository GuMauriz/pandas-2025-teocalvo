# %%

import pandas as pd

# %%

# Novo dataset
df_exemplo = pd.DataFrame({
    "Nome": ["Gus", "Tavo", "Júlia", "Lia", "Gus", "Tavo"],
    "Sobrenome": ["Silva", "Silva", "Ferreira", "Jú", "Ferreira", "Silva"]
})

df_exemplo

# %%

# Verificando duplicatas considerando todas as colunas
df_exemplo.duplicated()

# %%

# Removendo duplicatas considerando todas as colunas - mantém o primeiro
df_exemplo.drop_duplicates()

# %%

# Removendo duplicatas considerando todas as colunas - mantém o último
df_exemplo.drop_duplicates(keep="last")

# %%

# Inserindo mais uma coluna
df_exemplo["Idade"] = [20, 21, 19, 18, 19, 21]
df_exemplo

# %%

# Removendo duplicatas considerando apenas a coluna "Nome"
df_exemplo.drop_duplicates(subset=["Nome"])

# %%

# Removendo duplicatas considerando a coluna "Sobrenome" e "Idade"
df_exemplo.drop_duplicates(subset=["Sobrenome", "Idade"])

# %%
# 05.05 - Selecione a primeira transação diária de cada cliente.
transacoes_df = pd.read_csv("../data/transacoes.csv", sep = ";")
transacoes_df.head()
# %%
transacoes_df = transacoes_df.sort_values(by=["IdCliente", "DtCriacao"])
transacoes_df["DiaCriacao"] = pd.to_datetime(transacoes_df["DtCriacao"]).dt.date
transacoes_df.head()
# %%
transacoes_df = transacoes_df.drop_duplicates(subset=["IdCliente", "DiaCriacao"], keep="first")
transacoes_df.head(10)