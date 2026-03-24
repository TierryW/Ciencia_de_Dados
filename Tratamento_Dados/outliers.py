import pandas as pd
from scipy import stats

pd.set_option('display.width', None)
df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]
print ('filtro básico:\n', df_filtro_basico[['nome', 'idade']])

# Identificar outliers com Z-score /// O Z-score mede quantos desvios padrão um valor está distante da média.
z_score = stats.zscore(df['idade'].dropna()) # Seleciona a coluna idade, remove os valores nulos e calcula o Z-score de cada idade.
outliers_z = df[z_score >= 3]  # Regra comum para outliers: Z >= 3, é um possível outliers
print ('Outliers pelo  Z-score:\n', outliers_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)  # Q1 - 25% dos dados
Q3 = df['idade'].quantile(0.75)  # Q3 - 75% dos dados
                                # IQR - Intervalo interquartil (parte central dos dados)
IQR = Q3 - Q1  # IQR mede os 50% do meio, ignorando extremos
                                # 1,5 é empírico
limite_baixo = Q1 - 1.5 * IQR  # Abaixo de limite_baixo é outlier
limite_alto = Q3 + 1.5 * IQR   # Acima de limite_alto é outlier

print('Limite IQR: ', limite_baixo, limite_alto)

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print ('Outliers pelo  IQR:\n', outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]  # Filtra idades muito altas e baixas

limite_baixo = 0
limite_alto = 100

# Filtrar endereços inválidos
df['endereco'] = df['endereco'].apply(lambda x: 'Endereço inválido' if len(x.split('\n')) < 3 else x)

# Tratar campos de texto
df['nome'] = df['nome'].apply(lambda x: 'nome inválido' if isinstance(x, str) and len(x) > 50 else x)
print('Quantidade de registros com nomes grandes: ', (df['nome'] == 'nome inválido').sum())

print('Dados com Outliers tratados: \n', df)

# Salvar no DataFrame
df.to_csv('clientes_remove_outliers.csv', index=False)
