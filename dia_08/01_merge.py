# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")
transacoes.head()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";").rename(
    columns={
        'idCliente': 'IdCliente',
        "qtdePontos": "QtdePontos"
})
clientes.head()

# %%

transacoes_clientes = transacoes.merge(
    right=clientes,
    how="left",
    on="IdCliente",
    suffixes=('_transacao', '_cliente')
)

transacoes_clientes.head()

# %%

# # # # # # # # # # # # # # # # # # # # #
# Quem teve mais transações de Streak? #
# # # # # # # # # # # # # # # # # # # # 

df_trans_produto = pd.read_csv("../data/transacao_produto.csv", sep = ";")
df_trans_produto.head()

# %%

df_trans_produto.groupby(by=["IdProduto"])["IdProduto"].count()

# %%

df_produto = pd.read_csv("../data/produtos.csv", sep = ";")
# Transformando o IdProduto em string para conseguir dar o join
df_produto["IdProduto"] = df_produto["IdProduto"].astype(str)
df_produto

# %%
df_produto_transacao = df_trans_produto.merge(
    right= df_produto,
    how="left",
    on=["IdProduto"],
    suffixes=("_transprod", "_prod")
)
df_produto_transacao

# %%

df_final = transacoes.merge(
    right=df_produto_transacao,
    how="left",
    on=["IdTransacao"],
    suffixes=("_transacoes", "_transprod")
)
df_final.head()

# %%
summary_df_final = (
    df_final[df_final["DescNomeProduto"].isin(["Presença Streak"])]
    .groupby(by=["IdCliente"], as_index=False).agg({
        "IdTransacao": ["count"]
    })
)

summary_df_final.columns = ["IdCliente", "QtdTransacoesStreak"]

# %%

# Os cinco maiores clientes com transacoes de Streak
summary_df_final.sort_values(by=["QtdTransacoesStreak"], ascending=[False]).head(5)