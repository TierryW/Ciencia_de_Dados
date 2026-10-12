<h1 align="center">Previsão de Valores de Aluguel</h1>

## 📚 Objetivo

Este projeto tem como objetivo realizar uma análise exploratória de dados imobiliários e aplicar modelos de **Regressão Linear Simples e Múltipla** para analisar e prever valores de aluguel.

O projeto envolve tratamento de dados, identificação de possíveis outliers, visualização de informações e análise de correlação, buscando compreender quais características dos imóveis estão relacionadas aos valores de aluguel.

Ao final, os modelos são avaliados por meio do coeficiente de determinação (R²), permitindo comparar a contribuição de diferentes variáveis para a previsão dos preços.

---

## 📊 Dados

O projeto utiliza o conjunto de dados `ALUGUEL.csv`.

As principais variáveis utilizadas são:

- `Valor_Aluguel` — valor do aluguel do imóvel.
- `Valor_Condominio` — valor do condomínio.
- `Metragem` — metragem do imóvel.
- `N_Quartos` — quantidade de quartos.
- `N_banheiros` — quantidade de banheiros.
- `N_Suites` — quantidade de suítes.
- `N_Vagas` — quantidade de vagas de estacionamento.

---

## 🔎 Análise Exploratória

Inicialmente, foram realizadas as seguintes etapas:

- Visualização das primeiras linhas com `head()`.
- Verificação dos tipos de dados com `dtypes`.
- Identificação de valores ausentes com `isnull().sum()`.
- Análise estatística com `describe()`.
- Verificação da quantidade de registros com valor de condomínio igual a zero.
- Análise de possíveis outliers utilizando boxplots.
- Investigação da relação entre as características dos imóveis e os valores de aluguel.
- Construção de uma matriz de correlação entre as variáveis numéricas.

Essa etapa permitiu compreender a estrutura dos dados e identificar aspectos que poderiam influenciar a análise e os modelos de regressão.

---

## 🧹 Tratamento de Outliers

Para analisar possíveis valores extremos na variável `Valor_Condominio`, foi utilizado o método **IQR (Intervalo Interquartil)**. Esse método utiliza o primeiro quartil (Q1) e o terceiro quartil (Q3) para calcular os limites inferior e superior.

```python
Q1 = df['Valor_Condominio'].quantile(0.25)
Q3 = df['Valor_Condominio'].quantile(0.75)

IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
```

Os valores identificados como possíveis outliers foram analisados por meio do boxplot. Os valores de condomínio iguais a zero foram mantidos, pois o limite inferior calculado pelo IQR foi negativo e, portanto, esses registros não ultrapassavam o limite inferior. A decisão de manter esses valores evita alterá-los sem confirmação de que sejam inválidos.

Após o tratamento, alguns pontos ainda foram indicados como possíveis outliers no boxplot. Eles foram mantidos por não apresentarem, na análise realizada, impacto considerado significativo para o objetivo do projeto.

---

## 📈 Análise das Variáveis

Foram desenvolvidas visualizações para investigar a relação entre as características dos imóveis e o valor do aluguel.

### Metragem × Valor do Aluguel

Foi calculada a média do valor do aluguel para cada metragem utilizando `groupby()`. A análise indicou uma tendência de aumento do aluguel conforme a metragem aumenta. Entretanto, essa relação não se aplica a todos os imóveis, pois outros fatores também influenciam o preço.

### Número de Suítes × Valor do Aluguel

Foi calculada a mediana do valor do aluguel para cada quantidade de suítes. O gráfico indicou uma tendência de aumento dos valores de aluguel em imóveis com maior número de suítes.

### Número de Vagas × Valor do Aluguel

A análise da relação entre o número de vagas e o valor do aluguel permitiu observar diferenças nos preços conforme a quantidade de vagas disponíveis. Em geral, imóveis com aluguéis mais elevados apresentaram maior disponibilidade de vagas.

### Matriz de Correlação

A matriz de correlação foi construída utilizando as variáveis numéricas do conjunto de dados. Entre as relações observadas, destacaram-se:

- `N_Suites` e `N_banheiros`.
- `N_Vagas` e `Metragem`.
- `Metragem` e `Valor_Aluguel`.
- `N_Vagas` e `N_Suites`.
- `N_banheiros` e `N_Vagas`.

Essas relações ajudam a compreender como as características dos imóveis se relacionam entre si e com o valor do aluguel.

---

## 📉 Regressão Linear Simples

O primeiro modelo utilizou apenas a variável `Metragem` para prever o `Valor_Aluguel`. Os dados foram divididos em conjuntos de treinamento e teste, com 75% dos dados para treinamento e 25% para teste, utilizando `random_state=42`.

```python
X = df[['Metragem']]
y = df['Valor_Aluguel']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

regressao = LinearRegression()
regressao.fit(X_train, y_train)
```

### Visualização do modelo

O gráfico de dispersão compara a metragem dos imóveis com seus valores reais de aluguel, enquanto a linha vermelha representa a regressão ajustada. Observa-se uma tendência positiva: em geral, imóveis maiores apresentam aluguéis mais elevados. No entanto, muitos pontos estão distantes da linha, indicando que a metragem isoladamente não explica toda a variação dos preços.

```python
plt.figure(figsize=(8, 6))

plt.scatter(X['Metragem'], y, color='blue', alpha=0.6, label='Dados Originais')

X_ordenado = X.sort_values('Metragem')
plt.plot(X_ordenado['Metragem'], regressao.predict(X_ordenado), color='red', linewidth=2, label='Linha de Regressão')

plt.xlabel('Metragem')
plt.ylabel('Valor do Aluguel')
plt.title('Regressão Linear Simples')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Avaliação da regressão simples

O modelo apresentou um R² de aproximadamente **0,52 nos dados de treinamento**. Isso significa que cerca de 52% da variação dos valores de aluguel no conjunto de treinamento é explicada pela metragem.

Nos dados de teste, o R² foi de aproximadamente **0.56**. Esse resultado indica que, nessa divisão dos dados, o modelo explicou cerca de 56,5% da variação dos valores de aluguel no conjunto de teste. O resultado de teste foi superior ao de treinamento, mas essa diferença, por si só, não garante uma boa capacidade de generalização. A dispersão observada no gráfico também evidencia limitações na previsão com apenas uma variável.

---

## 🤖 Regressão Linear Múltipla

No segundo modelo, foram utilizadas seis variáveis explicativas para prever o valor do aluguel:

- `Valor_Condominio`
- `Metragem`
- `N_Quartos`
- `N_banheiros`
- `N_Suites`
- `N_Vagas`

A variável dependente permaneceu como `Valor_Aluguel`.

```python
X = df[['Valor_Condominio', 'Metragem', 'N_Quartos', 'N_banheiros', 'N_Suites', 'N_Vagas']]
y = df['Valor_Aluguel']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

regressao_multipla = LinearRegression()
regressao_multipla.fit(X_train, y_train)
```

### Visualização das previsões no treinamento

Como a regressão múltipla utiliza seis variáveis independentes, não é possível representar o modelo inteiro como uma única reta em um gráfico bidimensional. Por isso, foi utilizado um gráfico que compara os valores reais de aluguel com os valores previstos pelo modelo. A linha vermelha representa a previsão ideal, na qual o valor previsto é igual ao valor real.

```python
previsoes_treino = regressao_multipla.predict(X_train)

plt.figure(figsize=(8, 6))
plt.scatter(y_train, previsoes_treino, color='blue', alpha=0.6, label='Valores previstos')

minimo = min(y_train.min(), previsoes_treino.min())
maximo = max(y_train.max(), previsoes_treino.max())

plt.plot([minimo, maximo], [minimo, maximo], color='red', linewidth=2, label='Previsão ideal')

plt.xlabel('Valor real do aluguel')
plt.ylabel('Valor previsto pelo modelo')
plt.title('Regressão Linear Múltipla - Dados de Treinamento')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Pontos próximos à linha vermelha indicam previsões próximas dos valores reais, enquanto pontos distantes representam erros maiores. O gráfico mostra que há dispersão entre os valores reais e previstos, principalmente nos aluguéis mais elevados, indicando que o modelo ainda apresenta limitações.

### Avaliação da regressão múltipla

Nos dados de teste, o modelo obteve um R² de aproximadamente **0.61**. Isso indica que cerca de 61,4% da variação dos valores de aluguel no conjunto de teste é explicada conjuntamente pelas seis variáveis independentes. Os 38,6% restantes não são explicados pelo modelo, o que sugere que outros fatores também influenciam os preços.

---

## ⚖️ Comparação entre os Modelos

| Modelo | Variáveis explicativas | R² nos dados de teste |
|:--|:--|--:|
| Regressão Linear Simples | Metragem | 0.56 |
| Regressão Linear Múltipla | Condomínio, metragem, quartos, banheiros, suítes e vagas | 0.61 |

A regressão múltipla apresentou o melhor resultado nos dados de teste. Seu R² foi de aproximadamente 0.61, comparado a 0.56 da regressão simples. Isso representa uma melhora de cerca de 4,9 pontos percentuais na proporção da variação explicada pelo modelo.

O resultado sugere que incluir outras características dos imóveis contribuiu para melhorar a capacidade explicativa das previsões. Entretanto, ambos os modelos apresentam limitações, e a inclusão de outras variáveis relevantes e a análise dos erros podem ajudar a aprimorar os resultados.

---

## 💡 Conclusão

O projeto demonstrou a aplicação de técnicas de análise exploratória, tratamento de possíveis outliers, visualização de dados e Machine Learning para investigar os fatores relacionados aos valores de aluguel.

A regressão linear simples, baseada apenas na metragem, obteve R² de aproximadamente 0.56 nos dados de teste. Já a regressão linear múltipla, que considera seis características dos imóveis, alcançou R² de aproximadamente 0.61 no mesmo tipo de avaliação. Portanto, o modelo múltiplo apresentou melhor desempenho nessa divisão dos dados.

Apesar da melhora, os gráficos mostram diferenças entre os valores reais e previstos, especialmente em imóveis com aluguéis mais elevados. Os modelos podem ser aprimorados com a análise dos resíduos, a avaliação de outras métricas e a inclusão de novas variáveis relevantes.

---

## 📚 O Que Aprendi

- Manipulação de dados com Pandas.
- Análise exploratória de dados.
- Estatística descritiva.
- Identificação de possíveis outliers com IQR.
- Visualização de dados com Matplotlib, Seaborn e Plotly.
- Agrupamento de dados com `groupby()`.
- Análise de correlação.
- Divisão de dados com `train_test_split`.
- Regressão Linear Simples.
- Regressão Linear Múltipla.
- Treinamento de modelos com Scikit-learn.
- Avaliação de modelos utilizando R².
- Comparação entre modelos preditivos.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Seaborn
- Matplotlib
- Plotly
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

### Bibliotecas Utilizadas

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```

---

## 🚀 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/TierryW/Ciencia_de_Dados.git
```

2. Acesse a pasta do projeto:

```bash
cd Ciencia_de_Dados
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise e as visualizações.**

**Observação:** o arquivo `ALUGUEL.csv` deve estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 3 - Regresssao_Linear
│
├── 📄 ALUGUEL.csv
├── 📄 Projeto.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Tratamento de Outliers → Visualização → Regressão Simples → Regressão Múltipla → Avaliação**

O projeto demonstra como a regressão linear pode ser aplicada à análise de dados imobiliários para investigar a relação entre as características dos imóveis e seus valores de aluguel, transformando dados brutos em informações úteis para análise e previsão.

