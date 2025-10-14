# %%
import pandas as pd
import requests

# %%

# 1. Define the URL and headers
url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

try:
    # 2. Use requests to get the HTML content with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    
    # 3. Pass the HTML content to pandas.read_html()
    dfs = pd.read_html(response.text)
    
    print("Successfully read HTML tables:")
    print(dfs[1].head()) # Print the head of the first DataFrame
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
except ValueError as e:
    print(f"Error parsing HTML: {e}")

# %%
df_uf_brasil = dfs[1].drop(columns=['Bandeira'])
df_uf_brasil.head()
# %%
# Verificando os tipos das colunas
df_uf_brasil.dtypes
# %%

# Separando as colunas para arrumar e o dicionário de substituição

columns_to_float = ["Área (km²)", "PIB per capita (R$) (2015)",
                    "Expectativa de vida (2016)"]
columns_to_integer = ["População (Censo 2022)", "PIB (2015)"]

dictionary_replace = {
    ' ': '',
    ',': '.',
    'anos': '',
    '%': '',
    '‰': '',
    '\xa0': ''
}

# %% 

# Construindo uma função para realizar a substituição
def replace_values(value, replace_dict):
    if isinstance(value, str):
        for old, new in replace_dict.items():
            value = value.replace(old, new)
    return value

# %%

# Aplicando a função para converter as colunas para float
for col in columns_to_float:
    df_uf_brasil[col] = df_uf_brasil[col].apply(
        lambda x : float(replace_values(x, dictionary_replace)))

# %%

# Aplicando a função para converter as colunas per cent e per mille para float

df_uf_brasil["Alfabetização (2016)"] = df_uf_brasil["Alfabetização (2016)"].apply(
    lambda x: float(replace_values(x, dictionary_replace))/100
)

df_uf_brasil["Mortalidade infantil (2016)"] = df_uf_brasil["Mortalidade infantil (2016)"].apply(
    lambda x: float(replace_values(x, dictionary_replace))/1000
)

# %%

# Aplicando a função para converter as colunas para integer
for col in columns_to_integer:
    df_uf_brasil[col] = df_uf_brasil[col].apply(
        lambda x: int(replace_values(x, dictionary_replace))
    )

# %%
df_uf_brasil.dtypes
# %%
df_uf_brasil.head()
# %%

# Construção de um CASE WHEN para criar uma nova coluna
def uf_to_region(uf):
    if uf in ["Goiás", "Mato Grosso", "Mato Grosso do Sul", "Distrito Federal"]:
        return 'Centro-Oeste'
    elif uf in ["Alagoas", "Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return 'Nordeste'
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
        return 'Norte'
    elif uf in ["Espírito Santo"," Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return 'Sudeste'
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return 'Sul'
# %%
df_uf_brasil['Região'] = df_uf_brasil['Unidade federativa'].apply(uf_to_region)
# %%
df_uf_brasil.head()
# %%

# Para aplicar nas linhas, usamos axis=1
def calculate_population_density(row):
    return row['População (Censo 2022)'] / row['Área (km²)']

df_uf_brasil['Densidade populacional (hab/km²)'] = df_uf_brasil.apply(calculate_population_density, axis=1)
df_uf_brasil.head()