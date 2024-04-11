# -*- coding: utf-8 -*-
"""desafio_python_apis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12zV0L8A40Of9O_zZX2wgok10_8MjroU6
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50"
response = requests.get(url)
data = response.json()
item_ids = [item["id"] for item in data["results"]]

item_details = []
for item_id in item_ids:
    item_url = f"https://api.mercadolibre.com/items/{item_id}"
    item_response = requests.get(item_url)
    item_data = item_response.json()
    item_details.append(item_data)

df = pd.DataFrame(item_details)

relevant_columns = ["title", "price", "category_id", "condition"]
df_relevant = df[relevant_columns]

sns.histplot(df_relevant["price"], bins=20, kde=True)
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.title("Distribuição de Preços")
plt.show()

"""# Documentação da Solução

## Passo 1: Obtenção dos IDs dos Itens
Fazemos uma solicitação HTTP GET para a API pública do Mercado Livre usando o URL fornecido.
Extraímos os IDs dos itens da resposta JSON.

## Passo 2: Obtenção dos Detalhes dos Itens
Para cada ID de item, fazemos outra solicitação HTTP GET para obter os detalhes completos do item.
Armazenamos esses detalhes em uma lista.

## Passo 3: Desnormalização dos Dados
Convertemos a lista de detalhes dos itens em um DataFrame do Pandas.
Selecionamos as colunas relevantes (por exemplo, título, preço, categoria, condição).

## Passo 4: Análise Exploratória
Realizamos uma análise exploratória dos dados.
Exemplo: fiz um plot de um histograma dos preços dos itens.
"""
