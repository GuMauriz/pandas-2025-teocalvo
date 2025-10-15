# %%

import pandas as pd
import os

# %%

# Função para ler o arquivo e construir um DF a partir dele
def read_file(file_name:str) -> pd.DataFrame:
    df = (pd.read_csv(f"../data/ipea/{file_name}.csv", sep = ";")
        # Renomeando com nome do arquivo
        .rename(columns={"valor": f"{file_name}"})
        # Como a concatenação ocorre pelo index (no eixo 1 - axis=1),
        # é necessário transformar as colunas em comum como
        # índice nos dataframes.
        .set_index(["nome", "período"])
        # Dropando coluna desnecessária
        .drop(["cod"], axis=1)
    )

    return df

# %%

# Lista dos arquivos .csv
arquivos = os.listdir("../data/ipea/")

# Lista de dataframes para concatenar
dfs = []
for i in arquivos:
    dfs.append(read_file(i.split(".")[0]))

# %%

df_final = (
    pd.concat(dfs, axis=1)
    .reset_index()
    .sort_values(by=["período", "nome"])
)

df_final.to_csv("homicidios_consolidado.csv", index=False, sep=";")