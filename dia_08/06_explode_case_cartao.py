# %%

import pandas as pd

# %%

df = pd.read_csv("dados_cartao.csv", sep=";")
df

# %%

# Tratando colunas existentes e construindo "vlParcela"
df["dtTransacao"] = pd.to_datetime(df["dtTransacao"])
df["vlParcela"] = round(df["vlVenda"] / df["qtdParcelas"], 2)
df

# %%

# Determinar a ordem das parcelas, aumentando as linhas pelo explode
df["ordemParcela"] = df.apply(lambda row:
                              [i for i in range(row["qtdParcelas"])],axis=1)
df_explode = df.explode("ordemParcela")
df_explode

# %%

# Função para calcular o mês de parcela
def calc_data_parcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])

    if dt.month < 10:
        mes = "0" + str(dt.month)
    else:
        mes = str(dt.month)

    dt = f"{dt.year}-{mes}-01"
    return dt

# %%

# Acrescentando o valor de "ordemParcela" como mês na dtTransacao
df_explode["dtParcela"] = df_explode.apply(lambda row:
                                           calc_data_parcela(row), axis=1)

df_explode

# %%

# Agrupando por cliente e data da parcela para somar o valor de pgto
summary = (df_explode
           .groupby(by=["idCliente", "dtParcela"], as_index=False)
           .agg({"vlParcela": ["sum"]})
           )

summary.columns = ["idCliente", "dtParcela", "vlParcela"]

summary.sort_values(by=["idCliente", "dtParcela"], ascending=[True, True])