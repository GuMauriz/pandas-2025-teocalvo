# %%

import pandas as pd
# %%

# Carregando o dataset
df_clientes = pd.read_csv("../data/clientes.csv", sep = ";")
df_clientes.head()
# %%

filtro = df_clientes["qtdePontos"] == 0
df_clientes_0 = df_clientes[filtro]

df_clientes_0["flag_exemplo"] = 1

# O DataFrame original não é alterado, a menos que façamos uma atribuição
# df_clientes = df_clientes[filtro]. A variável df_clientes_0 é um novo
# DataFrame, que consiste num ponteiro para o DataFrame original onde
# o filtro é True.

# %%

A = [1, 2]
B = A
print("A: ", A)
print("B: ", B)

B.append(3)
print("A: ", A)
print("B: ", B)

# O dado A se altere porque B é um ponteiro para A.

# %%

# Para evitar isso, podemos criar uma cópia do dado original.

A = [1, 2]
B = A.copy()
print("A: ", A)
print("B: ", B)

B.append(3)
print("A: ", A)
print("B: ", B)

# O dado A não se altera porque B é uma cópia de A.
# Acontece o mesmo para DataFrames do Pandas.

# %%

filtro = df_clientes["qtdePontos"] == 0
df_clientes_0 = df_clientes[filtro].copy()

df_clientes_0["flag_exemplo"] = 1

df_clientes_0