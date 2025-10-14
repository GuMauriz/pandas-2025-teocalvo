# %%
import pandas as pd
# %%
idades = [15, 22, 35, 45, 52, 60, 75, 80, 34,
          27, 13, 18, 23, 37, 48, 55, 63, 70]

idades = pd.Series(idades)
idades
# %%
# Soma das idades
idades.sum()
# %%
# Média das idades
idades.mean()
# %%
# Mediana das idades
idades.median()
# %%
# Desvio padrão das idades
idades.std()
# %%
# Descrição estatística das idades
idades.describe()

# %%
# Novo dataset
df = pd.read_csv("../data/clientes.csv", sep = ";")
df.head()
# %%
# Quantidade de pessoas que tem twitch
df["flTwitch"].sum()
# %%
# Média dos clientes que possuem cada rede social
redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]
df[redes_sociais].mean()
# %%
# Para pegar apenas uma estatística específica, como a média
num_columns = df.dtypes[df.dtypes != "object"].index
df[num_columns].mean()