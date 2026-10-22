# <h1 align="center">Previsão de Compras Online com Regressão Logística e Random Forest</h1>

## 📚 Objetivo

Este projeto tem como objetivo analisar o comportamento dos clientes de uma campanha de marketing e desenvolver modelos de Machine Learning para prever a probabilidade de realização de compras online, utilizando a variável `WebPurchases` como alvo de classificação binária.

Foram utilizadas a **Regressão Logística** e o **Random Forest** para comparar o desempenho de diferentes algoritmos na identificação de clientes com maior probabilidade de realizar compras pela internet.

O projeto envolve análise exploratória, tratamento dos dados, análise de correlação, preparação das variáveis, treinamento dos modelos, otimização de hiperparâmetros e avaliação dos resultados. Também foi analisada a importância das variáveis no Random Forest, com o objetivo de identificar características relevantes para apoiar a segmentação de clientes e o planejamento de campanhas de marketing.

---

## 📊 Dados

O projeto utiliza o conjunto de dados `marketing_campaign.csv`.

A base contém informações relacionadas ao perfil dos clientes, histórico de compras, gastos por categoria de produtos e comportamento de navegação.

**Variáveis da base de dados:**

- `Year_Birth` — Ano de nascimento do cliente.
- `Education` — Nível de escolaridade do cliente.
- `Marital_Status` — Estado civil do cliente.
- `Income` — Renda do cliente.
- `Kidhome` — Número de crianças pequenas no domicílio.
- `Recency` — Número de dias desde a última compra.
- `MntWines` — Gastos com vinhos.
- `MntFruits` — Gastos com frutas.
- `MntMeatProducts` — Gastos com produtos de carne.
- `MntFishProducts` — Gastos com produtos de peixe.
- `MntSweetProducts` — Gastos com produtos doces.
- `MntGoldProds` — Gastos com produtos da categoria ouro.
- `NumStorePurchases` — Número de compras realizadas em lojas físicas.
- `NumWebVisitsMonth` — Número de visitas ao site no último mês.
- `Complain` — Indicador de reclamação registrada pelo cliente.
- `WebPurchases (Target)` — Variável-alvo binária utilizada para representar a ocorrência de compra online: (0) não realizou compra online e (1) realizou compra online, conforme a codificação utilizada no projeto.

---

## 🔎 Análise Exploratória

Foram realizadas as seguintes etapas:

- Visualização das primeiras linhas com `head()`.
- Verificação dos tipos de dados com `dtypes`.
- Análise estatística descritiva com `describe()`.
- Verificação de valores ausentes com `isnull().sum()`.
- Análise da distribuição da variável-alvo.
- Identificação de correlações entre as variáveis numéricas.
- Construção de uma matriz de correlação para investigar relações entre o comportamento dos clientes e as compras online.
- Análise das relações entre renda, gastos por categoria, compras em lojas físicas e visitas ao site.

A análise exploratória identificou associações relevantes entre algumas variáveis e o comportamento de compra online. Entre os destaques estão as correlações positivas de `MntWines` e `NumStorePurchases` com a variável-alvo, além da correlação negativa observada para `Kidhome`.

Também foram identificadas relações entre a renda e os gastos em determinadas categorias de produtos, contribuindo para compreender melhor os diferentes perfis de consumo.

Esses resultados serviram como base para a preparação dos dados e para a interpretação das variáveis mais relevantes durante a modelagem.

---

## ⚙️ Preparação dos Dados

Inicialmente, as variáveis foram separadas entre preditoras e variável-alvo.

```python
X = df.drop(columns=["WebPurchases"])
Y = df['WebPurchases']
```

A variável `WebPurchases` foi utilizada como alvo, enquanto as demais variáveis foram utilizadas para prever a classe correspondente.

As etapas de preparação incluíram:

- Tratamento das variáveis categóricas, como `Education` e `Marital_Status`.
- Codificação das variáveis categóricas para permitir sua utilização pelos modelos.
- Tratamento de valores ausentes quando necessário.
- Separação dos dados em conjuntos de treinamento e teste.
- Avaliação de estratégias para lidar com o desbalanceamento das classes.
- Padronização das variáveis nos fluxos de modelagem em que essa etapa foi utilizada.

A divisão entre treinamento e teste foi realizada com `train_test_split`, utilizando 20% dos dados para teste e `random_state=42`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
```

O conjunto de teste foi reservado para avaliar a capacidade de generalização dos modelos em dados não utilizados durante o treinamento.

Para evitar vazamento de dados, as transformações e técnicas de balanceamento devem ser ajustadas somente com os dados de treinamento. O conjunto de teste deve permanecer separado e não deve receber `SMOTE`.

---

## 🤖 Modelo 1: Regressão Logística

Foi utilizado o algoritmo `LogisticRegression` como modelo inicial de classificação binária.

```python
modelo1 = LogisticRegression(random_state=42)
```

A Regressão Logística foi escolhida como referência por ser adequada a problemas de classificação binária e permitir estimar probabilidades associadas às classes.

Também foram investigados ajustes de hiperparâmetros utilizando `GridSearchCV` e validação cruzada estratificada.

### Resultados

A Regressão Logística apresentou aproximadamente **85% de acurácia nos dados de teste**. A otimização dos hiperparâmetros não produziu melhorias significativas em relação ao modelo original.

Apesar de apresentar resultados consistentes entre treinamento e teste, seu desempenho foi inferior ao obtido pelo Random Forest nas avaliações realizadas.

---

## 🌳 Modelo 2: Random Forest

O algoritmo `RandomForestClassifier` foi utilizado para identificar relações potencialmente não lineares entre as características dos clientes e a ocorrência de compras online.

O Random Forest combina diversas árvores de decisão para produzir uma previsão final, permitindo trabalhar com diferentes tipos de variáveis e analisar a importância relativa das características utilizadas pelo modelo.

Foram avaliadas versões do modelo sem ajuste e com otimização de hiperparâmetros.

### Resultados

O Random Forest sem ajuste apresentou aproximadamente **91% de acurácia nos dados de teste**, mas demonstrou indícios de sobreajuste, pois alcançou 100% de acurácia no treinamento.

Após a otimização, o Random Forest ajustado manteve aproximadamente **91% de acurácia no teste**, reduzindo a acurácia de treinamento para 96%.

O modelo ajustado também apresentou:

- `Recall` de 89% para a classe 0.
- `Recall` de 93% para a classe 1.
- `F1-score` de aproximadamente 0,91 para ambas as classes.
- `ROC-AUC` de aproximadamente 0,97.

Esses resultados indicam um equilíbrio entre desempenho preditivo e capacidade de generalização, embora ainda seja importante monitorar possíveis erros de classificação.

---

## 🔁 Validação Cruzada

Foi utilizada a validação cruzada para comparar o desempenho dos modelos em diferentes divisões dos dados de treinamento.

Essa técnica permite avaliar se os resultados permanecem consistentes em diferentes subconjuntos, reduzindo a dependência de uma única divisão dos dados.

Na comparação registrada no projeto, a Regressão Logística ajustada apresentou acurácia média de aproximadamente 85%, enquanto o Random Forest ajustado alcançou cerca de 90%.

A validação cruzada reforçou a escolha do Random Forest ajustado como o modelo mais equilibrado entre as abordagens comparadas.

---

## 📈 Importância das Variáveis

Após o treinamento do Random Forest, foi analisada a importância das variáveis para identificar quais características mais contribuíram para as previsões do modelo.

As variáveis de maior importância registradas foram:

| Variável | Importância |
|---|---:|
| `MntWines` | 0,255384 |
| `MntMeatProducts` | 0,175440 |
| `NumStorePurchases` | 0,118568 |
| `Income` | 0,086569 |
| `NumWebVisitsMonth` | 0,070988 |
| `MntGoldProds` | 0,058383 |
| `MntFruits` | 0,049882 |
| `MntSweetProducts` | 0,043784 |
| `MntFishProducts` | 0,042325 |

Os resultados indicam que os gastos com vinhos e carnes, assim como o histórico de compras em lojas físicas, tiveram maior importância relativa para as previsões do modelo.

A renda e a frequência de visitas ao site também apresentaram contribuição relevante.

**Importante:** a importância das variáveis representa sua contribuição preditiva no modelo, não uma relação de causa e efeito. Da mesma forma, a correlação observada na análise exploratória não comprova causalidade.

---

## 💡 Aplicações no Marketing

Os resultados da análise exploratória e do Random Forest podem apoiar a definição de estratégias de marketing mais direcionadas.

As principais possibilidades identificadas são:

- **Campanhas por categoria de produto:** testar ofertas de vinhos, carnes e outras categorias com clientes que demonstram afinidade com esses produtos.
- **Integração entre canais:** desenvolver ações que incentivem clientes habituados às lojas físicas a realizar compras online, como cupons digitais.
- **Segmentação por renda e consumo:** avaliar diferentes faixas de renda e padrões de gastos para personalizar ofertas.
- **Otimização da experiência digital:** investigar clientes que visitam o site e testar melhorias na navegação, recomendações de produtos e incentivos à conversão.
- **Reativação de clientes:** avaliar campanhas direcionadas a consumidores que estão há mais tempo sem comprar.

---

## 📚 O Que Aprendi

- Manipulação e exploração de dados com Pandas.
- Análise estatística descritiva.
- Tratamento de dados ausentes e preparação de variáveis.
- Codificação de variáveis categóricas.
- Análise de correlação e interpretação de relações entre variáveis.
- Separação dos dados em conjuntos de treinamento e teste.
- Aplicação da Regressão Logística para classificação binária.
- Utilização do Random Forest para classificação.
- Ajuste de hiperparâmetros com `GridSearchCV`.
- Utilização de técnicas de balanceamento, como `SMOTE`, no conjunto de treinamento.
- Avaliação de modelos com acurácia, precisão, `recall`, `F1-score` e `ROC-AUC`.
- Aplicação de validação cruzada para comparar modelos.
- Interpretação da importância das variáveis.
- Transformação de resultados dos modelos em hipóteses para estratégias de marketing.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook
- Git
- GitHub

### Bibliotecas utilizadas

```python
# Manipulação dos Dados
import pandas as pd
import numpy as np

# Visualização dos Gráficos
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Tratamento dos Dados
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# Modelos
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Melhoria de Hiperparâmetros
from sklearn.model_selection import (
            train_test_split,
            cross_val_score, 
            GridSearchCV, 
            StratifiedKFold,
            RandomizedSearchCV
)
# Métricas de Avaliação
from sklearn.metrics import (
            classification_report, 
            confusion_matrix, roc_curve, 
            roc_auc_score
)
from scipy.stats import randint
```

---

## 🚀 Como Executar

1. Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/TierryW/Ciencia_de_Dados.git
```

2. Acesse o diretório do projeto:

```bash
cd Ciencia_de_Dados
```

3. Instale as bibliotecas utilizadas:

```bash
pip install -r requirements.txt
```

4. Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

**Abra o arquivo `Projet.ipynb` e execute as células para reproduzir a análise exploratória, a preparação dos dados, o treinamento dos modelos e a avaliação dos resultados.**

> **Observação:** o arquivo `marketing_campaign.csv` deve estar no diretório esperado pelo código. 

---

## 📁 Estrutura do Projeto

```
📂 11 - Duelo_Modelos
│
├── 📄 marketing_campaign.csv
├── 📄 Projeto.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Preparação dos Dados → Regressão Logística → Random Forest → Otimização de Hiperparâmetros → Validação Cruzada → Importância das Variáveis → Recomendações de Marketing**

O projeto demonstrou a aplicação de técnicas de análise exploratória e Machine Learning para prever a ocorrência de compras online a partir das características e do comportamento dos clientes.

A comparação dos modelos indicou que o `Random Forest` apresentou desempenho superior à `Regressão Logística`. Enquanto a `Regressão Logística ajustada` alcançou aproximadamente 85% de acurácia média na validação cruzada, o `Random Forest ajustado` obteve cerca de 90%. Nos dados de teste, o `Random Forest ajustado` manteve aproximadamente 91% de acurácia, com `F1-score` de 0,91 para ambas as classes e `ROC-AUC` de 0,97.

A análise de importância das variáveis destacou os gastos com vinhos e carnes, o número de compras em lojas físicas e a renda como características relevantes para as previsões. Esses resultados oferecem subsídios para desenvolver hipóteses de segmentação, personalização de ofertas e integração entre canais físicos e digitais.

Dessa forma, o **`Random Forest ajustado` foi selecionado como o modelo mais equilibrado entre os avaliados**, considerando o desempenho no teste e a redução dos indícios de sobreajuste.

