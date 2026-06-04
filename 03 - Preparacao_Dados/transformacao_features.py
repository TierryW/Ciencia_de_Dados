import pandas as pd
import numpy as np
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('clientes-v2-tratados.csv')
print(df.head())

# Transformação Logarítmica - Reduz a diferença entre valores muito grandes
df['salario_log'] = np.log1p(df['salario'])  # log1p é usado para evitar problemas com zero
print('\nDataFrame após transformação em logarítmica no salario:\n', df.head())

# Transformação Box-Cox - Reduz assimetria e aproxima dados de uma distribuição normal
df['salario_boxcox'], _= stats.boxcox(df['salario'] + 1)  # df['salario'] + 1 - Box-Cox não aceita valores zero ou negativos
print('\nDataFrame após transformação em Box-Cox no salario:\n', df.head())

# Codificação de Frequência para estado - Calcula a frequência de cada estado
estado_freq = df['estado'].value_counts() / len(df)  # Conta quantas vezes cada valor aparece e divide pelo total de registros
df['estado_freq'] = df['estado'].map(estado_freq)  # Substitui o estado pela frequência dele no dataset
print('\nDataframe após codificação de frequência para estado:\n', df.head())

# Interações
df['interacao_idade_filhos'] = df['idade'] * df['numero_filhos']  # Nova variável combinando duas outras
print('\nDataFrame após criação de interações entre idade e numero_filhos:\n', df.head())

# Técnica                        Objetivo
# Logarítmica                    Reduzir assimetria
# Box-Cox                        Aproximar distribuição normal
# Codificação de Frequência      Transformar categorias em números
# Interação de variáveis         Capturar relações entre variáveis