import pandas as pd

df = pd.read_csv('/data/ecommerce_tratados_ex3.csv')

# Escreva seu código abaixo
dicionario = {'Nenhum': 0, '1': 1, '2': 2, '3': 3, '4': 4, '+5': 5, '+25': 25, '+50': 50, '+100': 100, '+1000': 1000, '+10mil': 10000, '+50mil': 50000}

df['Qtd_Vendidos_Cod'] = df['Qtd_Vendidos'].map(dicionario)

marca_freq = df['Marca'].value_counts() / len(df)
df['Marca_Freq'] = df['Marca'].map(marca_freq)

material_freq = df['Material'].value_counts() / len(df)
df['Material_Freq'] = df['Material'].map(material_freq)
