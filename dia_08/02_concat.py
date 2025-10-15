# %%

import pandas as pd

# %%
 
df_exemplo_1 = pd.DataFrame({
    "cliente": [1, 2, 3, 4, 5,],
    "nome": ["Gus", "Tavo", "Ju", "Lia", "Maria",],
})

df_exemplo_1
# %%

df_exemplo_2 = pd.DataFrame({
    "cliente": [6, 7, 8,],
    "nome": ["Manuel", "Miguela", "Iracemo",],
    "idade": [16, 27, 38,],
})

df_exemplo_2
# %%

# Concat é diferente do union. Concat une os dataframes mesmo que
# alguma coluna não exista em comum entre eles. Pra desconsiderar
# o index inicial dos dfs concatenados e começar um novo, ignore_index=True.
pd.concat([df_exemplo_1, df_exemplo_2], ignore_index=True)

# %%

df_exemplo_3 = pd.DataFrame({
    "idade": [21, 17, 19, 26, 15]
})

df_exemplo_3
# %%

# Concatenando o primeiro dataframe com o terceiro para capturar as idades
pd.concat([df_exemplo_1, df_exemplo_3])

# %%

# Do jeito acima dá problema por conta da inexistência de pelo menos
# uma coluna em comum. O parâmetro empilhou um em cima do outro.
# Para concatenar da esquerda/direita, neste caso:
pd.concat([df_exemplo_1, df_exemplo_3], axis=1)