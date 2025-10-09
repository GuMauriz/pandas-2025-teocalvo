# %%

import pandas as pd

# %%

# Filtrar uma lista em python
valores = [32, 57, 66, 10, 65, 89, 45, 78, 45, 32, 12, 11, 7]

# %%

# Através de um for
valores_filtrados = []
for i in valores:
    if i >= 50:
        valores_filtrados.append(i)
print(valores_filtrados)

# %%

# Através de list comprehension
valores_filtrados = [i for i in valores if i >= 50]
print(valores_filtrados)

# %%

# Mesmo array, agora marcando True ou False
filtro = []
for i in valores:
    filtro.append(i >= 50)

print(filtro)

# %%

# Com base no True e False, filtrar os valores
valores_filtrados = []
for i in range (len(valores)):
    if filtro[i]:
        valores_filtrados.append(valores[i])
print(valores_filtrados)

# %%

# Dataframe de exemplo
df_exemplo = pd.DataFrame({
    "Nome": ["Ana", "Bia", "Carlos", "Daniel", "Eduardo"],
    "Idade": [23, 45, 12, 36, 28]
})

# %%

# Construção do filtro
filtro_df = df_exemplo["Idade"] >= 30
print(filtro_df)

df_exemplo[filtro_df]

# %%

# Dataframe real - transações
df = pd.read_csv("../data/transacoes.csv", sep=";" )
df.head()

# %%

# Filtrando onde os pontos são maiores do que 50 e menores do que 100
df[(df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)]

# %%

# Filtrando onde os pontos ou são 1 ou são iguais a 100
df[(df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)]

# %%

# Filtrando onde o sistema origem é diferente de "twitch"
df[df["DescSistemaOrigem"] != "twitch"]