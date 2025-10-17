# %% 

import pandas as pd

# %%

df = pd.read_csv("homicidios_consolidado.csv", sep = ";")
df

# %%

# Empilhando os dados
df_stack = (df.set_index(["nome", "período"])
            .stack()
            .reset_index())
df_stack.columns = ["nome", "período", "métrica", "valor"]
df_stack

# %%

# Pivotando para desempilhar (como no unstack)
(df_stack.pivot_table(
    values="valor", # Valor nas novas colunas
    index=["nome", "período"], # Agrupando por essas colunas já existentes
    columns="métrica") # Qual coluna terá seus valores como colunas
    .reset_index()
)

# %%

# Removendo umas das colunas de agrupamento e "compensando" esse dado 
# a partir de uma outra métrica (no exemplo, média)
(df_stack.pivot_table(
    values="valor",
    index=["nome"], # Removendo período
    columns="métrica",
    aggfunc="mean") # Faz mostrar o valor médio de "coluna_xpto" por período
)