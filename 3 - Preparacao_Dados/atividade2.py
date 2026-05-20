import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('/data/ecommerce_tratados_ex2.csv')

# Escreva seu código abaixo

scaler = MinMaxScaler()
df['Nota_MinMax'] = scaler.fit_transform(df[['Nota']])

df['N_Avaliacoes_MinMax'] = scaler.fit_transform(df[['N_Avaliacoes']])

df['Desconto_MinMax'] = scaler.fit_transform(df[['Desconto']])

df['Preco_MinMax'] = scaler.fit_transform(df[['Preco']])

label = LabelEncoder()
df['Marca_Cod'] = label.fit_transform(df['Marca'])

df['Material_Cod'] = label.fit_transform(df['Material'])

df['Temporada_Cod'] = label.fit_transform(df['Temporada'])
