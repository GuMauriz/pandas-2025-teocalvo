# %%

import pandas as pd
# %%

# Carregando o dataset
df = pd.read_csv("../data/transacao_produto.csv", sep = ";")
df.head()

# %%

# Filtrar onde o produto é 5 ou 11
filtro = df["IdProduto"].isin(["5", "11"])
df[filtro]

# %%

# Novo dataset
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes.head()

# %%

# Filtrando clientes cuja data de criação não exista
df_clientes[df_clientes["DtCriacao"].isna()]

# %%

# Filtrando clientes cuja data de criação exista
df_clientes[~df_clientes["DtCriacao"].isna()]
# É o mesmo que: df_clientes[df_clientes["DtCriacao"].notna()]