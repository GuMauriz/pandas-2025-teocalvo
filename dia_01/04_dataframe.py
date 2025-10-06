# %%

# Importando a biblioteca
import pandas as pd

# %%

# Construindo series
idades = [18, 15, 26, 31, 48, 20, 41, 16, 17, 22, 9, 14, 33]

nomes = ['Gus', 'Tavo', 'Ju', 'Lia', 'Manuel', 'Miguela',
         'Jaira', 'Iracemo', 'Jhonsons', 'Maria', 'Bia',
         'Jukes', 'Bob']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

# DataFrame é um 'varal' que se pendura diversas series
df = pd.DataFrame()
df['idades'] = series_idades
df['nomes'] = series_nomes
df

# %%

# Selecionar todas as informações associadas a uma posição do df
df.iloc[1]

# Selecionar apenas uma informação específica associada a posição 'x' no df
df.iloc[1]['nomes']