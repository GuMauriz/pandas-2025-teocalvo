# %% 
import pandas as pd
# %%
df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()
# %%
id_cliente_exemplo = "000ff655-fa9f-4baa-a108-47f581ec52a1"
# Desejo pegar a última parte do id_cliente
id_cliente_exemplo.split("-")[-1]
# %%
# Para fazer isso em dataframes
df["idCliente"].apply(lambda x: x.split("-")[-1])
# %%
