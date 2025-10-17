# %% 

import pandas as pd

# %%

df = pd.read_csv("homicidios_consolidado.csv", sep = ";")
df

# %%

# Transformando as colunas em linhas: colunas "métrica" e "valor"
df_stack = (df.set_index(["nome", "período"])
            .stack())
df_stack = df_stack.reset_index()
df_stack.columns = ["nome", "período", "métrica", "valor"]
df_stack

# %%

# Construir colunas a partir dos valores distintos de outra (ex.: métrica):
df_unstack = (df_stack.set_index(["nome", "período", "métrica"])
              .unstack()
              .reset_index())

# Para tratar multicolumns
nome_metricas_lista = df_unstack.columns.droplevel(0)[2:].tolist()
df_unstack.columns = ["nome", "período"] + nome_metricas_lista
df_unstack

# %%

