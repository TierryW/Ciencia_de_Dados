import pandas as pd
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes-v2-tratados.csv')

print(df.head())

df = df[['idade', 'salario']]

# Normalização - MinMaxScaler
scaler = MinMaxScaler()  # Transforma valores para o intervalo 0 a 1
df['idade_MinManScaler'] = scaler.fit_transform(df[['idade']])
df['salario_MinManScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1))  # Transforma valores para o intervalo -1 a 1
df['idade_MinManScaler_mm'] = min_max_scaler.fit_transform(df[['idade']])
df['salario_MinManScaler_mm'] = min_max_scaler.fit_transform(df[['salario']])

# Padronização - StandardScaler
scaler = StandardScaler()  # Usa média e desvio padrão - Média ~ 0 - Desvio padrão ~ 1
df['idade_StandardScaler'] = scaler.fit_transform(df[['idade']])
df['salario_StandardScaler'] = scaler.fit_transform(df[['salario']])

# Padronização - RobustScaler
scaler = RobustScaler()  # Usa mediana e IQR - Não é afetado por outliers
df['idade_RobustScaler'] = scaler.fit_transform(df[['idade']])
df['salario_RobustScaler'] = scaler.fit_transform(df[['salario']])

print(df.head(15))

print('MinMaxScaler (De 0 a 1):')
print('Idade - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['idade_MinManScaler'].min(), df['idade_MinManScaler'].max(), df['idade_MinManScaler'].mean(), df['idade_MinManScaler'].std()))
print('Salário - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['salario_MinManScaler'].min(), df['salario_MinManScaler'].max(), df['salario_MinManScaler'].mean(), df['salario_MinManScaler'].std()))

print('\nMinMaxScaler (De -1 a 1):')
print('Idade - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['idade_MinManScaler_mm'].min(), df['idade_MinManScaler_mm'].max(), df['idade_MinManScaler_mm'].mean(), df['idade_MinManScaler_mm'].std()))
print('Salário - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['salario_MinManScaler_mm'].min(), df['salario_MinManScaler_mm'].max(), df['salario_MinManScaler_mm'].mean(), df['salario_MinManScaler_mm'].std()))

print('\nStandardScaler (Ajusta a média a 0 e desvio padrão a 1):')
print('Idade - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['idade_StandardScaler'].min(), df['idade_StandardScaler'].max(), df['idade_StandardScaler'].mean(), df['idade_StandardScaler'].std()))
print('Salário - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['salario_StandardScaler'].min(), df['salario_StandardScaler'].max(), df['salario_StandardScaler'].mean(), df['salario_StandardScaler'].std()))

print('\nRobustScaler (Ajusta a mediana e IQR):')
print('Idade - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['idade_RobustScaler'].min(), df['idade_RobustScaler'].max(), df['idade_RobustScaler'].mean(), df['idade_RobustScaler'].std()))
print('Salário - Min: {:.4f} Max: {:.4} Mean: {:.4f} Std: {:.4f}'.format(df['salario_RobustScaler'].min(), df['salario_RobustScaler'].max(), df['salario_RobustScaler'].mean(), df['salario_RobustScaler'].std()))
