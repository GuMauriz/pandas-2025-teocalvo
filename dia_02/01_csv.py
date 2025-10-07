# %%
import pandas as pd
import openpyxl # para o excel
import pyarrow # para o parquet

# %%

# Como ler informações de um .csv
df = pd.read_csv("../data\clientes.csv", sep = ';')
df

# %%

# Como salvar um .csv
# Dessa forma salva no diretório em que o programa atual se encontra.
df.to_csv('clientes.csv')

# %% 

# Como salvar como .parquet - precisa do pyarrow
df.to_parquet('clientes.parquet', index = False)

# %%

# Como salvar como .xlsx - precisa do openpyxl
df.to_excel('clientes.xlsx', index = False)