# %%

import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

# %%

df = pd.read_sql_table(table_name="tb_customers", con=engine)
df.head()

# %%

query = "SELECT * FROM tb_customers LIMIT 100"

df_100 = pd.read_sql_query(query, con=engine)
df_100