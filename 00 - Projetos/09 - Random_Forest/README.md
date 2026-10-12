<h1 align="center">Classificação da Qualidade de Vinhos com Random Forest</h1>

## 📚 Objetivo

Este projeto tem como objetivo analisar as características físico-químicas de vinhos tintos e desenvolver modelos de Machine Learning para classificar sua qualidade, representada pela variável `quality`.

Foram realizadas análises exploratórias, investigação das correlações entre as variáveis, balanceamento das classes com SMOTE e treinamento de um modelo Random Forest. Em seguida, foi aplicada uma busca aleatória de hiperparâmetros com `RandomizedSearchCV` e investigada uma abordagem alternativa com `class_weight`, buscando melhorar o desempenho da classificação.

---

## 📊 Dados

O projeto utiliza o conjunto de dados `winequality-red.csv`, que contém características físico-químicas dos vinhos.

- `fixed acidity` — acidez fixa.
- `volatile acidity` — acidez volátil.
- `citric acid` — ácido cítrico.
- `residual sugar` — açúcar residual.
- `chlorides` — cloretos.
- `free sulfur dioxide` — dióxido de enxofre livre.
- `total sulfur dioxide` — dióxido de enxofre total.
- `density` — densidade.
- `pH` — medida de acidez.
- `sulphates` — sulfatos.
- `alcohol` — teor alcoólico.
- `quality` — nota de qualidade do vinho, utilizada como variável-alvo.

---

## 🔎 Análise Exploratória

Foram realizadas as seguintes etapas:

- Visualização das primeiras linhas com `head()`.
- Verificação dos tipos de dados com `dtypes`.
- Identificação de valores ausentes com `isnull().sum()`.
- Análise estatística descritiva com `describe()`.
- Contagem e análise percentual das classes da variável `quality`.
- Construção de uma matriz de correlação entre as variáveis numéricas.

### Distribuição da qualidade

A análise identificou um desbalanceamento entre as classes. A maior parte dos registros pertence às classes de qualidade 5 (aproximadamente 42,59%) e 6 (aproximadamente 39,9%). As classes 3, 4 e 8 possuem menos amostras, o que dificulta o aprendizado dos padrões dessas categorias.

### Matriz de correlação

Entre as correlações observadas entre as variáveis explicativas, destacaram-se:

- `fixed acidity` e `citric acid`: aproximadamente 0,67.
- `fixed acidity` e `density`: aproximadamente 0,67.
- `free sulfur dioxide` e `total sulfur dioxide`: aproximadamente 0,67.
- `volatile acidity` e `citric acid`: aproximadamente -0,55.
- `citric acid` e `pH`: aproximadamente -0,54.
- `density` e `alcohol`: aproximadamente -0,50.

As variáveis com maior correlação com a qualidade (`quality`) foram `alcohol` (0,48), `volatile acidity` (-0,39), `sulphates` (0,25) e `citric acid` (0,23). Apesar dessas relações, foram utilizadas todas as variáveis explicativas, pois os testes realizados com apenas as variáveis de maior correlação apresentaram desempenho inferior.

---

## ⚙️ Preparação dos Dados

A variável `quality` foi separada das demais colunas para ser utilizada como alvo da classificação. A base foi dividida em 80% para treinamento e 20% para teste, utilizando `random_state=42`.

```python
X = df.drop('quality', axis=1)
Y = df['quality']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
```

---

## ⚖️ Balanceamento das Classes com SMOTE

Para reduzir o desbalanceamento no conjunto de treinamento, foi utilizado o **SMOTE (Synthetic Minority Over-sampling Technique)**, que gera amostras sintéticas para as classes minoritárias.

```python
smote = SMOTE(random_state=42)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, Y_train)
```

Após o balanceamento, foi utilizado `StandardScaler` para padronizar as variáveis. O scaler foi ajustado com os dados de treinamento balanceados e aplicado ao conjunto de teste sem reajuste. A distribuição das classes após o SMOTE foi visualizada em um gráfico de barras.

---

## 🤖 Modelo 1: Random Forest

O primeiro modelo foi desenvolvido com `RandomForestClassifier`, utilizando `random_state=42`.

```python
random_forest = RandomForestClassifier(random_state=42)
random_forest.fit(X_train_scaled, y_train_balanced)
Y_pred = random_forest.predict(X_test_scaled)
```

O desempenho foi avaliado com acurácia, relatório de classificação e matriz de confusão.

### Resultados

O modelo apresentou acurácia de aproximadamente **62%** no conjunto de teste.

As classes 5 e 6 tiveram os melhores resultados, com F1-scores de aproximadamente 0.70 e 0.62, respectivamente. A classe 7 apresentou F1-score de aproximadamente 0.59.

As classes 3, 4 e 8 apresentaram dificuldades de classificação. A classe 3 não teve nenhuma amostra corretamente identificada no conjunto de teste. A matriz de confusão também evidenciou confusões entre as classes 5 e 6 e entre as classes 6 e 7.

---

## 🔧 Modelo 2: Otimização com RandomizedSearchCV

Na segunda abordagem, foi utilizada a busca aleatória de hiperparâmetros com `RandomizedSearchCV`, testando diferentes configurações do Random Forest.

Os parâmetros considerados foram:

- `n_estimators`: quantidade de árvores.
- `max_depth`: profundidade máxima das árvores.
- `min_samples_split`: número mínimo de amostras para dividir um nó.
- `min_samples_leaf`: número mínimo de amostras em uma folha.
- `max_features`: quantidade de variáveis consideradas em cada divisão.

A busca utilizou `n_iter=100`, validação cruzada com `cv=5`, `n_jobs=-1` e `random_state=42`, tendo a acurácia como critério de avaliação.

### Resultados

Após a otimização, a acurácia registrada foi de aproximadamente **63%**, uma melhoria modesta em relação ao primeiro modelo.

As classes 5, 6 e 7 continuaram apresentando os melhores resultados, enquanto as classes 3, 4 e 8 permaneceram difíceis de classificar. As maiores confusões continuaram ocorrendo entre as classes 5 e 6 e entre as classes 6 e 7.

---

## ⚖️ Modelo 3: Random Forest com class_weight

Como alternativa ao SMOTE, foi investigado o parâmetro `class_weight`, que atribui pesos diferentes às classes durante o treinamento, aumentando a importância dos erros cometidos em classes menos representadas.

Nessa etapa, a abordagem foi avaliada separadamente, sem combinar SMOTE e StandardScaler, para observar o efeito do ajuste de pesos. A busca de hiperparâmetros passou a considerar opções como `None`, `balanced` e `balanced_subsample`. A melhor configuração registrada utilizou `class_weight='balanced_subsample'`.

### Resultados

A acurácia registrada aumentou de aproximadamente 63% para **67%**. Os F1-scores das classes 5 e 6 chegaram a aproximadamente 0.74 e 0.67, respectivamente.

Entretanto, as classes 3, 4 e 8 continuaram apresentando desempenho muito baixo e não tiveram amostras corretamente classificadas nessa avaliação. Isso demonstra que a melhora na acurácia geral não significou uma melhoria uniforme para todas as classes.

**Observação técnica:** nesta terceira abordagem, o `RandomizedSearchCV` é ajustado com `X_train` e `Y_train`, e o melhor modelo realiza previsões com `X_test`. Como o Random Forest não exige padronização das variáveis, essa etapa utiliza os dados originais, sem SMOTE e sem `StandardScaler`. Assim, treinamento e teste seguem a mesma representação dos dados. O uso de `class_weight` é avaliado separadamente das abordagens anteriores para comparar seu efeito no desempenho do modelo.

---

## 📊 Avaliação dos Modelos

| Abordagem | Acurácia registrada |
|---|---:|
| Random Forest com SMOTE e StandardScaler | 62% |
| Random Forest com RandomizedSearchCV | 63% |
| Random Forest com `class_weight` | 67% |

Os resultados indicam aumento gradual da acurácia entre as abordagens avaliadas. No entanto, a matriz de confusão e as métricas por classe mostram que o modelo apresenta dificuldades importantes nas classes minoritárias. Por isso, a acurácia não deve ser analisada isoladamente: precisão, recall e F1-score por classe também são necessários para compreender a qualidade das previsões.

---

## 💡 Conclusão

O projeto demonstrou a aplicação de técnicas de análise exploratória e classificação supervisionada para prever a qualidade de vinhos tintos com base em suas características físico-químicas.

O Random Forest inicial obteve aproximadamente 62% de acurácia. A otimização com `RandomizedSearchCV` elevou o resultado para cerca de 63%, enquanto a abordagem com `class_weight` registrou 67%. Apesar da melhora na acurácia, as classes 3, 4 e 8 continuaram apresentando dificuldades de classificação, principalmente devido à quantidade reduzida de exemplos disponíveis.

A análise evidencia que o desbalanceamento dos dados é um dos principais desafios do projeto. Como próximos passos, podem ser testadas outras estratégias de balanceamento, métricas mais adequadas para classes desbalanceadas e validação consistente do pipeline de pré-processamento, além da comparação com outros algoritmos de classificação.

---

## 📚 O Que Aprendi

- Manipulação e exploração de dados com Pandas.
- Análise estatística descritiva.
- Análise da distribuição de classes.
- Visualização de dados com Plotly, Seaborn e Matplotlib.
- Construção e interpretação de matrizes de correlação.
- Separação de dados em treino e teste com `train_test_split`.
- Balanceamento de classes com SMOTE.
- Padronização de variáveis com `StandardScaler`.
- Treinamento de modelos de classificação com Random Forest.
- Otimização de hiperparâmetros com `RandomizedSearchCV`.
- Uso de `class_weight` em conjuntos de dados desbalanceados.
- Avaliação com acurácia, precisão, recall, F1-score e matriz de confusão.
- Análise das limitações de modelos em classes minoritárias.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Imbalanced-learn
- Scikit-learn
- Jupyter Notebook
- Git 
- GitHub

### Bibliotecas utilizadas

```python
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
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

> **Observação:** o arquivo `winequality-red.csv` deve estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 9 - Random_Forest
│
├── 📄 winequality-red.csv
├── 📄 Projeto.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Correlação → Divisão Treino/Teste → SMOTE e Padronização → Random Forest → Otimização de Hiperparâmetros → class_weight → Avaliação**

O projeto percorreu as principais etapas de um processo de classificação utilizando Machine Learning, desde a análise exploratória dos dados e identificação de correlações entre as variáveis até o treinamento e a avaliação dos modelos Random Forest. Foram testadas diferentes abordagens para lidar com o desbalanceamento das classes, incluindo SMOTE, padronização dos dados, otimização de hiperparâmetros e utilização do parâmetro `class_weight`.

