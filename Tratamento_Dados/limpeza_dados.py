import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None) # Define o máximo de caracteres por linha na saída do console
print(df.head())

# Remover dados
df.drop('pais', axis=1, inplace=True)  # inplace=True - faz a alteração direta no DataFrame
                                             # Remove a coluna pais
df.drop(2, axis=0, inplace=True) # Remove a linha no cadastro de index 2

# Normalizar campos de texto
df['nome'] = df['nome'].str.title()  # Primeira letra maiúscula
df['endereco'] = df['endereco'].str.lower()  # Todas as letras em minúsculo
df['estado'] = df['estado'].str.strip().str.upper() # Todas as letras em maiúsculo

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0)  # Substituir valores nulos por 0
df_dropna = df.dropna()  # Remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4)  # Manter registro com no mínimo 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remover registro com CPF nulo

print('Valores nulos:\n', df.isnull().sum())
print('Quantidade de registros nulos com fillna: ', df_fillna.isnull().sum().sum())  # .isnull() - Verifica as células e retorna true/ NaN ou false
print('Quantidade de registros nulos com dropna: ', df_dropna.isnull().sum().sum())  # .sum() - Soma os valores de True por coluna, e conta quantos nulos existem - True = 1 e False = 0
print('Quantidade de registros nulos com dropna4: ', df_dropna4.isnull().sum().sum())  # .sum().sum() - O segundo .sum(), soma o total de nulos de todas as colunas
print('Quantidade de registros nulos com CPF: ', df.isnull().sum().sum())

df.fillna({'estado': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('Endereço não informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())  # Faz a média das idades e aplica aos nulos

# Tratar formato de dados  # pd.to_datetime - Função do pandas que transforma valores em datas
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')  # errors='coerce' - Se os valores não forem corretos e válidos o pandas transforma em NaT

# Tratar dados duplicados
print('Quantidade de registro atual: ', df.shape[0])  # df.shape - retorna uma tupla com (linhas, colunas)
df.drop_duplicates()                                  # df.shape(0) - retorna a quantidade total de registros (linhas) do DataFrame
df.drop_duplicates(subset='cpf', inplace=True)
print ('Quantidade de registros removendo as duplicadas', len(df))  #len(df) - retorna a quantidade de linhas (registros) do DataFrame
                                                         # df.shape(0) == len(df)
print('Dados Limpos:\n', df)

# Salvar dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame:\n', pd.read_csv('clientes_limpeza.csv'))
