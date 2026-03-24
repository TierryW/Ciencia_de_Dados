import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Gráfico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter')  # ['scatter', 'hist', 'hex', 'kde', 'reg', 'resid']
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['salario'], fill=True, color='#863e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salario')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma
# https://seaborn.pydata.org/tutorial/color_palettes.html
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']])
plt.show()

# Gráfico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Salário por Idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Gráfico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade Clientes')
plt.legend(title='Nível Educação')
plt.show()
