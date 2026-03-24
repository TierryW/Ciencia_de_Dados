import pandas as pd

df = pd.read_csv('clientes.csv')

# Verificar os primeiros registros
print(df.head().to_string())

# Verificar a quantidade de linhas e colunas
print('Quantidade: ', df.shape)

# Verificar os tipos de dados
print('Tipagem:\n', df.dtypes)

# Verificar tipos de dados e valores nulos
print('Tipos de dados e valores nulos:\n', df.info())

# Checar valores nulos
print('Valores nulos:\n', df.isnull().sum())
