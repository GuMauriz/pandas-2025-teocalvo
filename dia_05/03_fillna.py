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

# Preenchendo valores nulos das variáveis numéricas com a média
medias = df_exemplo[["Idade", "Salário"]].mean().astype(int)
df_exemplo.fillna(medias)

# %%

# Preenchendo valores nulos das variáveis numéricas com a mediana
medianas = df_exemplo[["Idade", "Salário"]].median().astype(int)
df_exemplo.fillna(medianas)