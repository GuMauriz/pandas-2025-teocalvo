# %%

# Calcular média e variância de lista de idades
idades = [18, 15, 26, 31, 48, 20, 41, 16, 17, 22, 9, 14, 33]
media = sum(idades)/len(idades)
print('Média de idades: ', media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades) - 1)
print('Variância: ', variancia)

# %%

# Importando a biblioteca
import pandas as pd

# %%

# Transformando a lista em uma série de inteiros
series_idades = pd.Series(idades)
series_idades

# %%

# Estudando os métodos da series
print('Média idades: ', series_idades.mean())
print('Variâncias idades: ', series_idades.var())
print('DP idades: ', series_idades.std())

summary_idades = series_idades.describe()
summary_idades