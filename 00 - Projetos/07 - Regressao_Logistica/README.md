<h1 align="center">Análise e Previsão de Doenças Cardiovasculares</h1>

## 📚 Objetivo

Este projeto tem como objetivo realizar uma análise exploratória de dados relacionados à saúde e desenvolver um modelo de Machine Learning para classificar a presença de doenças cardiovasculares.

O projeto envolve tratamento de dados, análise de possíveis outliers, visualização de variáveis, análise de correlação, padronização de atributos e balanceamento das classes com SMOTE. Ao final, o desempenho do modelo de Regressão Logística é avaliado com métricas de classificação e a curva ROC.

---

## 📊 Dados

O projeto utiliza o conjunto de dados `CARDIO_BASE.csv`.

As principais variáveis são:

- `age` — idade.
- `gender` — gênero, recodificado durante a preparação dos dados.
- `height` — altura.
- `weight` — peso.
- `cholesterol` — nível de colesterol.
- `gluc` — nível de glicose.
- `smoke` — indicador relacionado ao tabagismo.
- `alco` — indicador relacionado ao consumo de álcool.
- `active` — indicador de atividade física.
- `cardio_disease` — variável-alvo que indica a presença ou ausência de doença cardiovascular.

---

## 🔎 Análise Exploratória

Inicialmente, foram realizadas as seguintes etapas:

- Visualização das primeiras linhas com `head()`.
- Verificação dos tipos de dados e da estrutura com `info()`.
- Análise estatística descritiva com `describe()`.
- Verificação dos valores únicos das variáveis `cholesterol` e `gluc`.
- Análise da distribuição de `height` e `weight` por meio de boxplots.
- Investigação da relação entre idade, colesterol, glicose, peso e a variável-alvo.
- Construção de uma matriz de correlação entre as variáveis numéricas.

Essa etapa permitiu compreender melhor a estrutura do conjunto de dados e identificar relações que poderiam ser relevantes para a classificação.

---

## 🧹 Preparação e Tratamento dos Dados

### Conversão de variáveis

A coluna `weight` foi convertida para o tipo numérico após a remoção dos separadores presentes nos valores. A variável `gender` foi recodificada utilizando o mapeamento `{2: 0, 1: 1}`.

### Tratamento de outliers com IQR

O método IQR (Intervalo Interquartil) foi aplicado às variáveis `height` e `weight`. Os limites foram calculados a partir do primeiro quartil (Q1), do terceiro quartil (Q3) e do intervalo interquartil:

```python
Q1 = df['height'].quantile(0.25)
Q3 = df['height'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR
```

Os valores identificados fora dos limites foram substituídos pela mediana dos valores que estavam dentro do intervalo. O procedimento foi aplicado separadamente às variáveis `height` e `weight`. Após o tratamento, os boxplots foram gerados novamente para observar a distribuição dos dados.

---

## 📈 Análise das Variáveis

Foram criadas visualizações para investigar a relação entre as características dos indivíduos e a presença de doenças cardiovasculares.

### Idade × Doença Cardiovascular

A análise da mediana de idade por classe mostrou que o grupo com doença cardiovascular apresentava idade mediana de aproximadamente 56 anos, enquanto o grupo sem a doença apresentava mediana de aproximadamente 52 anos. Esse resultado sugere uma associação entre idade mais elevada e presença da doença no conjunto analisado, mas não demonstra, por si só, uma relação causal.

### Colesterol × Doença Cardiovascular

Foi criado um gráfico de barras empilhadas para observar a distribuição dos níveis de colesterol entre as classes. A análise indicou uma maior participação dos níveis 2 e 3 no grupo com doença cardiovascular.

### Glicose × Doença Cardiovascular

A distribuição dos níveis de glicose também foi analisada por meio de barras empilhadas. No conjunto analisado, os níveis 2 e 3 representaram uma parcela dos registros de pessoas com doença cardiovascular.

### Peso × Doença Cardiovascular

A mediana do peso foi comparada entre os grupos. Os valores observados foram de aproximadamente 74 para pessoas com doença cardiovascular e 70 para pessoas sem a doença.

### Matriz de Correlação

A matriz de correlação foi construída com Seaborn e Matplotlib. Entre as relações observadas, destacaram-se:

- `gender` e `height`: correlação de aproximadamente -0,52.
- `cholesterol` e `gluc`: correlação de aproximadamente 0,43.
- `smoke` e `alco`: correlação de aproximadamente 0,33.
- `height` e `weight`: correlação de aproximadamente 0,31.
- `age` e `cardio_disease`: correlação de aproximadamente 0,24.
- `cholesterol` e `cardio_disease`: correlação de aproximadamente 0,22.

As correlações com a variável-alvo foram relativamente baixas, sugerindo que a classificação envolve a combinação de diferentes atributos, em vez de depender de uma única variável.

---

## ⚙️ Pré-processamento

A variável-alvo foi separada das variáveis explicativas:

```python
X = df.drop('cardio_disease', axis=1)
Y = df['cardio_disease']
```

Os dados foram divididos em conjuntos de treinamento e teste, com 80% para treinamento e 20% para teste, utilizando `random_state=42`.

A padronização com `StandardScaler` foi aplicada às variáveis `age`, `height` e `weight`, que possuem escalas numéricas distintas. As variáveis binárias e as variáveis ordinais `cholesterol` e `gluc` foram mantidas em suas escalas originais para preservar a interpretação de seus valores.

---

## ⚖️ Balanceamento das Classes com SMOTE

Para lidar com o desequilíbrio entre as classes, foi utilizado o **SMOTE (Synthetic Minority Over-sampling Technique)** no conjunto de treinamento. Essa técnica gera amostras sintéticas da classe minoritária para equilibrar a distribuição das classes.

```python
smote = SMOTE(random_state=42)
X_train_balanced, Y_train_balanced = smote.fit_resample(X_train, Y_train)
```

O balanceamento foi aplicado somente aos dados de treinamento, mantendo o conjunto de teste separado para avaliar o modelo em observações não utilizadas nessa etapa.

---

## 🤖 Modelo de Machine Learning: Regressão Logística

Foi utilizado o algoritmo de Regressão Logística para classificar os registros em duas categorias: presença ou ausência de doença cardiovascular.

```python
logistic_cardio = LogisticRegression(random_state=0)

logistic_cardio.fit(X_train_balanced, Y_train_balanced)
```

A Regressão Logística estima a probabilidade de uma observação pertencer a determinada classe e utiliza um limite de decisão para realizar a classificação.

---

## 📊 Avaliação do Modelo

O modelo foi avaliado nos conjuntos de treinamento balanceado e teste por meio de `classification_report`, que apresenta:

- Acurácia: proporção total de classificações corretas.
- Precisão: proporção de previsões positivas que estavam corretas.
- Recall: proporção dos casos de uma classe que foram identificados corretamente.
- F1-score: média harmônica entre precisão e recall.

### Resultados no treinamento

No conjunto de treinamento balanceado, o modelo apresentou acurácia de aproximadamente 63%, com métricas de precisão, recall e F1-score próximas entre as duas classes. Esse resultado indica um desempenho moderado.

### Resultados no teste

No conjunto de teste, o modelo alcançou acurácia de aproximadamente **65%**. O recall da classe 0 foi de aproximadamente 0,69, enquanto o recall da classe 1 foi de aproximadamente 0,61. Isso indica que o modelo identificou melhor os registros da classe 0 do que os da classe 1.

Os resultados de treinamento e teste foram semelhantes, sem uma diferença expressiva de acurácia. Entretanto, o desempenho geral ainda apresenta limitações, pois cerca de 35% das classificações no teste foram incorretas.

---

## 📉 Curva ROC e AUC

A curva ROC foi utilizada para analisar a relação entre a taxa de verdadeiros positivos (True Positive Rate) e a taxa de falsos positivos (False Positive Rate). A área sob a curva (AUC) registrada foi de aproximadamente **0,65**, indicando capacidade moderada de distinguir as classes.

---

## 💡 Conclusão

O projeto demonstrou a aplicação de análise exploratória, tratamento de outliers, padronização, balanceamento de classes e classificação com Regressão Logística em dados relacionados a doenças cardiovasculares.

O modelo obteve aproximadamente 63% de acurácia no treinamento balanceado e 65% no teste, com AUC registrada de 0,65. Os resultados indicam capacidade moderada de classificação, mas ainda há espaço para melhorias, principalmente na identificação da classe 1.

Como próximos passos, podem ser explorados outros algoritmos de classificação, ajustes de hiperparâmetros, validação cruzada e avaliação de métricas adicionais. Este projeto tem finalidade educacional e analítica e não deve ser utilizado isoladamente para diagnóstico ou decisões clínicas.

---

## 📚 O Que Aprendi

- Manipulação e limpeza de dados com Pandas.
- Análise exploratória de dados.
- Estatística descritiva.
- Identificação e tratamento de outliers com IQR.
- Visualização de dados com Plotly, Seaborn e Matplotlib.
- Análise de correlação.
- Divisão de dados com `train_test_split`.
- Padronização com `StandardScaler`.
- Balanceamento de classes com SMOTE.
- Treinamento de modelos de classificação com Scikit-learn.
- Avaliação com acurácia, precisão, recall e F1-score.
- Análise de curva ROC e AUC.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Seaborn
- Matplotlib
- Plotly
- Imbalanced-learn
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

### Bibliotecas utilizadas

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, classification_report
```

---

## 🚀 Como Executar

1. Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/TierryW/Ciencia_de_Dados.git
```

2. Acesse a pasta do projeto:

```bash
cd Ciencia_de_Dados
```

3. Instale as bibliotecas utilizadas no projeto:

```bash
pip install -r requirements.txt
```

4. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise, o treinamento do modelo e as visualizações.**

> **Observação:** o arquivo `CARDIO_BASE.csv` deve estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 7 - Regressao_Logistica
│
├── CARDIO_BASE.csv
├── Projeto.ipynb
├── requirements.txt
└── README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Tratamento de Outliers → Pré-processamento → SMOTE → Regressão Logística → Avaliação → Curva ROC**

O projeto percorreu as principais etapas de um processo de análise de dados e Machine Learning, desde a exploração e preparação da base até o treinamento e a avaliação do modelo de Regressão Logística. O tratamento de outliers com IQR, a padronização das variáveis e o balanceamento das classes com SMOTE foram aplicados para preparar os dados para a classificação.
Por fim, o modelo foi avaliado por meio de métricas como acurácia, precisão, recall, F1-score e curva ROC, permitindo analisar seu desempenho na identificação de doenças cardiovasculares. Os resultados indicaram uma capacidade de classificação moderada, evidenciando oportunidades de melhoria por meio de outros algoritmos, ajustes de parâmetros e novas avaliações.

