# %%

import pandas as pd

# %%

# Novo dataset
df_exemplo = pd.DataFrame({
    "Nome": ["Gus", "Tavo", "Júlia", "Lia"],
    "Idade": [None, 15, 23, 12],
    "Salário": [1300, None, 5000, 7500],
    "None": [None, None, None, None]
})

df_exemplo

# %%

# Remover linhas com qualquer valor ausente
df_exemplo.dropna(how="any")

# %%

# Remover linhas com todos os valores ausentes
df_exemplo.dropna(how="all")

# %%

# Remover colunas com qualquer valor ausente
df_exemplo.dropna(how="any", axis=1)

# %%

# Remover colunas com todos os valores ausentes
df_exemplo.dropna(how="all", axis=1)

# %%

# Remover apenas linhas com valores ausentes na coluna "Idade"
df_exemplo.dropna(subset=["Idade"])

# %%

# Remover apenas linhas com valores ausentes na coluna "Salário"
df_exemplo.dropna(subset=["Salário"])

# %%

# Remover linhas com valores ausentes em ambas as colunas "Idade" e "None"
df_exemplo.dropna(how = "all", subset=["Idade", "None"])