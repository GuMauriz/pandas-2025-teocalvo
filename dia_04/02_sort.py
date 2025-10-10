# %%

import pandas as pd

# %%

# Carregando o dataset
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes.head()

# %%

# Ordenando os clientes pela quantidade de pontos (desc) numa series
df_clientes["qtdePontos"].sort_values(ascending = False).head()

# %%

# Ordenando os clientes pela quantidade de pontos (desc) num dataframe
df_clientes.sort_values(by = "qtdePontos", ascending = False).head()

# %%

# Novo dataframe
df_exemplo = pd.DataFrame({
    "nome": ["Gus", "Tavo", "Jú", "Áquila", "Lia"],
    "idade": [21, 12, 19, 41, 35],
    "salario": [5000, 1250, 10000, 1250, 6900]
})

df_exemplo

# %%

# Ordenando por maior salário e, em caso de empate, por menor idade
df_exemplo.sort_values(by = ["salario", "idade"], ascending = [False, True])