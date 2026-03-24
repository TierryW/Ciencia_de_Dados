import pandas as pd
import random
from faker import Faker

faker = Faker('pt-BR')

dados_pessoas = []

for i in range(10):
    nome = faker.name()
    cpf = faker.cpf()
    idade = random.randint(18, 60)
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime('%d/%m/%Y')
    endereco = faker.address()
    estado = faker.state()
    pais = 'Brasil'

    pessoa = {
        'nome': nome,
        'cpf': cpf,
        'idade': idade,
        'data': data,
        'endereco': endereco,
        'estado': estado,
        'pais': pais
    }

    dados_pessoas.append(pessoa)

df_pessoas = pd.DataFrame(dados_pessoas)
print(df_pessoas)

pd.set_option('display.max_columns', None)  # Define o número máximo de colunas que o Pandas vai mostrar
pd.set_option('display.max_rows', None)  # Define o número máximo de linhas exibidas
pd.set_option('display.max_colwidth', None)  # Define o tamanho máximo do conteúdo dentro de cada coluna
pd.set_option('display.width', None)  # Define a largura máxima da exibição no terminal
print(df_pessoas)

# print(df_pessoas.to_string())

df_pessoas.to_csv('clientes.csv')
