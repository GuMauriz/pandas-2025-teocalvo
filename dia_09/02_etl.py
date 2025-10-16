# %%

import pandas as pd
import sqlalchemy
from sklearn import cluster

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%

with open("etl.sql") as open_file:
    query = open_file.read()

print(query)

# %%

df = pd.read_sql_query(query, con=engine)
df

# %%

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[["valorVendas", "qtdVendas"]])

df["cluster"] = kmean.labels_
df

# %%

df.to_sql("sellers_clusters", con=engine, index=False, if_exists="replace")