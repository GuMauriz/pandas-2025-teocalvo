# %%

# Importando a biblioteca
import pandas as pd

# %%
idades = [18, 15, 26, 31, 48, 20, 41, 16, 17, 22, 9, 14, 33]
series_idades = pd.Series(idades)
series_idades = series_idades.sort_values()
series_idades

# %%

# Acessar o primeiro elemento da série
series_idades.iloc[0]

# O 'iloc' serve para capturar os elementos da series não pelo índice/chave

# %%

# Acessar o último elemento da série
series_idades.iloc[-1]

# %%

# Acessar os primeiros três elementos
series_idades.iloc[:3]

# %%

# Acessar os últimos três elementos
series_idades.iloc[-3:]

# %%

# Do último ao primeiro
series_idades.iloc[::-1]

# %%

# Manipulando os indexes da series
nomes = ['Gus', 'Tavo', 'Ju', 'Lia', 'Manuel', 'Miguela',
         'Jair', 'Iracemo', 'Jhonsons', 'Maria', 'Bia',
         'Jukes', 'Bob']

series_nome_idade = pd.Series(idades, index = nomes)
series_nome_idade

# %%

series_nome_idade['Gus']