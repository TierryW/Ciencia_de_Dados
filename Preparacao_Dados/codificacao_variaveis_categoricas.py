import pandas as pd
from sklearn.preprocessing import LabelEncoder

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

# Codificação one-hot para 'estado_civil' - Cada categoria vira uma nova coluna
df = pd.concat([df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)
print('\nDataFrame após codificação one-hot para estado_civil: \n', df.head())

# Codificação ordinal para 'nível-educacao'
educacao_ordem = {'Ensino Fundamental': 1, 'Ensino Médio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4}
df['nivel_educacao_ordinal'] = df['nivel_educacao'].map(educacao_ordem)  # .map() - substitui os valores usando o dicionário
print('\nDataFrame após codificação ordinal para nivel_educacao: \n', df.head())

# Transforma 'area_atuacao' em categorias codificadas usando o método .cat.codes
df['area_atuacao_cod'] = df['area_atuacao'].astype('category').cat.codes  #  Converte para categoria e em código numérico
print('\nDataframe após transformar area_atuacao em códigos numéricos: \n', df.head())

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_classe-1
label_encoder = LabelEncoder()
df['estado_cod'] = label_encoder.fit_transform(df['estado'])  # Identifica os valores únicos e os transforma em números
print('\nDataFrame após aplicar LabelEncoder em estado: \n', df.head())

# Técnica                Usada em             Como funciona
# One-hot Encoding       estado_civil         Cria uma coluna para cada categoria
# Ordinal Encoding       nivel_educacao       Usa ordem lógica
# Category Codes         area_atuacao         Converte categorias em números
# LabelEncoder           estado               Números para cada classe