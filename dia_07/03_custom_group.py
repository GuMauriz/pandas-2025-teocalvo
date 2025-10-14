# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()
# %%

# Estatística aleatória, a meu critério: sqrt((Amplitude - média) ** 2)

def custom_group(x: pd.Series) -> float:
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media) ** 2)

# %%

# Idade desde a primeira atividade do cliente (primeira transacao) em dias
def lifetime_days(x: pd.Series) -> int:
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

# %%

summary = df.groupby(by=["IdCliente"], as_index=False).agg({
    "IdTransacao": ["count"],
    "QtdePontos": ["sum", "mean", custom_group],
    "DtCriacao": [lifetime_days]
})

# %%
summary.columns = [
    "IdCliente",
    "TotalTransacoes",
    "TotalPontos",
    "MediaPontos",
    "CustomGroupPontos",
    "DiasDesdePrimeiraTransacao"
]

summary.head()