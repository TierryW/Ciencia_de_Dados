import pandas as pd

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tippo
lista_nomes = ['Ana', 'Marcos', 'Carlos']
print('Lista de nomes: \n', lista_nomes)
print('Primeiro Elemento da lista: \n', lista_nomes[0]) # Imprime o item no index 0


# Dicionário: Estrutura composta de pares chave-valor
dicionario_pessoa = {
    'nome': 'Ana',
    'idade': 20,
    'cidade': 'São Paulo'
}
print('Dicionário de uma pessoa: \n', dicionario_pessoa)
print('Atributo do dicionário: \n', dicionario_pessoa.get('cidade')) # Buscando o valor através da chave cadastrada


# Lista de dicionários: Estrutura de dados que combina listas e dicionários
dados =[
    {'nome': 'Ana', 'idade': 20, 'cidade': 'São Paulo'},
    {'nome': 'Marcos', 'idade': 25, 'cidade': 'São José dos Campos'},
    {'nome': 'Carlos', 'idade': 35, 'cidade': 'Rio de Janeiro'}
]

# DataFrame: Estrutura de dados bidimensional
df =pd.DataFrame(dados)
print('DataFrame \n', df)

# Selecionar coluna
print(df['nome'])

# Selecionar várias colunas
print(df[['nome', 'idade']])

# Selecionar linhas pelo índice
print('Primeira linha \n', df.iloc[0]) # df.iloc - Significa integer location (localização por índice numérico)

# Adicionar uma nova coluna
df['salario'] = [4100, 3600, 5200]

# Adicionar um novo registro     # df.loc[len(df)] - Crie uma nova linha no índice igual ao tamanho atual
df.loc[len(df)] = {              # É possível registrar apenas informando os valores:
                                # Ex: df.loc[len(df)] = ['João', 30, 'Tabaté', 4800]
    'nome': 'João',
    'idade': 30,
    'cidade': 'Taubaté',
    'salario': 4800
}
print('DataFrame Atual \n', df)

# Removendo uma coluna
df.drop('salario', axis=1, inplace=True)  # axis = 0 -- remove linha
                                                # axsi = 1 -- remove coluna
                                                # inplace = true -- Faz a alteração diretamente no DataFrame original
# Filtrando pessoas com mais de 29 anos
filtro_idade = df[df['idade'] >= 30]  # Cria um novo DataFrame apenas com as linhas onde a idade é maior ou igual a 30
print('Filtro \n', filtro_idade)

# Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
# noinspection PyArgumentList
df_ler = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', df_ler)
