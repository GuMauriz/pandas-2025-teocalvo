# %%

import pandas as pd
import lxml

# %%

url = 'https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil'
# Pegando dados de uma tabela HTML
dfs = pd.read_html(url)
dfs

# Não deu certo porque o website não permitiu o acesso.