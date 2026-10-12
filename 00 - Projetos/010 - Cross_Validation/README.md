# <h1 align="center">Detecção de Incêndio com Regressão Logística e Cross Validation</h1>

## 📚 Objetivo

Este projeto tem como objetivo analisar os dados de um sistema de detecção de incêndios e desenvolver um modelo de Machine Learning para realizar uma classificação binária, utilizando a variável `Fire_Alarm` como alvo.

Foi escolhida a **Regressão Logística**, por ser adequada para problemas de classificação binária e permitir estimar a probabilidade de uma observação pertencer a uma das classes. Para avaliar o desempenho do modelo, foi utilizada a técnica de validação cruzada com 5 folds, permitindo comparar os resultados obtidos em diferentes subconjuntos dos dados.

---

## 📊 Dados

O projeto utiliza o conjunto de dados `SMOKE_DETECTION.csv`, que contém informações ambientais e concentrações de gases e partículas, utilizadas para identificar condições associadas à ocorrência de incêndios.

### Variáveis da base de dados

- `Unnamed: 0` — índice dos registros, não utilizado como variável preditora no modelo.
- `UTC` — tempo em segundos UTC.
- `Temperature[C]` — temperatura do ar em graus Celsius.
- `Humidity[%]` — umidade do ar em porcentagem.
- `TVOC[ppb]` — concentração total de compostos orgânicos voláteis, medida em partes por bilhão.
- `eCO2[ppm]` — concentração equivalente de CO₂, medida em partes por milhão.
- `Raw H2` — hidrogênio molecular bruto, não compensado.
- `Raw Ethanol` — etanol gasoso bruto.
- `Pressure[hPA]` — pressão do ar em hectopascais.
- `PM1.0` — concentração de material particulado com tamanho inferior a 1,0 µm.
- `PM2.5` — concentração de material particulado com tamanho superior a 1,0 µm e inferior a 2,5 µm.
- `NC0.5` — concentração numérica de partículas com tamanho inferior a 0,5 µm.
- `NC1.0` — concentração numérica de partículas na faixa de 0,5 µm a 1,0 µm.
- `NC2.5` — concentração numérica de partículas na faixa de 1,0 µm a 2,5 µm.
- `CNT` — contador de amostras.
- `Fire_Alarm` — variável-alvo utilizada para a classificação binária.

### 🎯 Rótulos da variável-alvo

A variável `Fire_Alarm` representa a ocorrência ou não de um incêndio:

- `0` — Não há ocorrência de incêndio.
- `1` — Há ocorrência de incêndio.

O objetivo do modelo é utilizar as variáveis preditoras da base para identificar padrões associados à ocorrência de incêndios e classificar os registros de acordo com a variável-alvo.

---

## 🔎 Análise Exploratória

Foram realizadas as seguintes etapas:

- Visualização das primeiras linhas com `head()`.
- Análise estatística descritiva com `describe()`.
- Verificação de valores ausentes com `isnull().sum()`.
- Identificação dos tipos de dados com `dtypes`.
- Remoção da coluna `Unnamed: 0`, que não foi utilizada na modelagem.
- Renomeação da coluna `Fire Alarm` para `Fire_Alarm`.

Essas etapas permitiram verificar a estrutura da base e preparar os dados para a construção do modelo de classificação.

---

## ⚙️ Preparação dos Dados

A variável `Fire_Alarm` foi separada das demais colunas para ser utilizada como variável-alvo. As outras variáveis foram mantidas como preditoras.

```python
X = df.drop('Fire_Alarm', axis=1)
y = df['Fire_Alarm']
```

A separação permite que o modelo utilize as características disponíveis na base para prever a classe correspondente ao alarme de incêndio.

---

## 🤖 Modelo: Regressão Logística

Foi utilizado o algoritmo `LogisticRegression`.

```python
modelo = LogisticRegression(max_iter=1000)
```

A Regressão Logística foi escolhida por sua simplicidade, facilidade de interpretação e adequação a problemas de classificação binária.

O parâmetro `max_iter=1000` aumenta o número máximo de iterações disponíveis durante o treinamento, ajudando o algoritmo a convergir para uma solução adequada quando o limite padrão é insuficiente.

---

## 🔁 Validação Cruzada com KFold

Para avaliar o desempenho do modelo, foi utilizada a técnica de **Cross-Validation com 5 folds**, por meio de `KFold` e `cross_val_score`.

```python
folds = 5

crossvalidation = KFold(n_splits=folds, shuffle=True, random_state=42)

pontuacoes = cross_val_score(modelo, X, y, cv=crossvalidation)
```

A validação cruzada divide os dados em cinco partes. Em cada rodada, uma parte é utilizada para validação e as demais para treinamento. Esse processo se repete até que todas as partes tenham sido utilizadas para validação.

Essa abordagem permite avaliar o desempenho do modelo em diferentes divisões da base, reduzindo a dependência de uma única divisão entre treinamento e teste.

### Resultados

As pontuações informadas para cada fold foram:

| Fold | Pontuação |
|---|---:|
| 1 | 0.9766 |
| 2 | 0.9862 |
| 3 | 0.9784 |
| 4 | 0.9770 |
| 5 | 0.9776 |

A média dessas cinco pontuações é de aproximadamente **97,93%**.

No código original, também foi calculada a média de uma chamada separada de `cross_val_score`, utilizando `cv=folds` diretamente, cujo resultado informado foi `0.9619` (96,19%). Essa chamada utiliza a configuração padrão de validação cruzada, enquanto as pontuações listadas acima correspondem ao objeto `KFold` configurado com `shuffle=True` e `random_state=42`.

---

## 📊 Avaliação do Modelo

A avaliação foi realizada utilizando as pontuações obtidas na validação cruzada.

A média aproximada de 97,93% indica que o modelo apresentou uma taxa elevada de acertos nas divisões avaliadas. A proximidade entre as pontuações dos folds também sugere consistência nos resultados obtidos.

---

## 📚 O Que Aprendi

- Manipulação e exploração de dados com Pandas.
- Análise estatística descritiva.
- Verificação de valores ausentes e tipos de dados.
- Preparação de variáveis preditoras e variável-alvo.
- Aplicação da Regressão Logística para classificação binária.
- Utilização do parâmetro `max_iter` para auxiliar a convergência do modelo.
- Aplicação de validação cruzada com `KFold`.
- Avaliação de modelos com `cross_val_score`.
- Interpretação de pontuações por fold e cálculo da média.
- Importância de avaliar falsos negativos em problemas de detecção de incêndios.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

### Bibliotecas utilizadas

```python
import pandas as pd
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
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

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise e o treinamento do modelo.**

> **Observação:** o arquivo `SMOKE_DETECTION.csv` deve estar no diretório esperado pelo código.
---

## 📁 Estrutura do Projeto

```
📂 10 - Cross_Validation
│
├── 📄 SMOKE_DETECTION.csv
├── 📄 Projeto.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Preparação dos Dados → Regressão Logística → Validação Cruzada (5 folds) → Avaliação dos Resultados**

O projeto demonstrou a aplicação de técnicas de análise exploratória e Machine Learning para realizar uma classificação binária utilizando a Regressão Logística. Após a inspeção e preparação dos dados, o modelo foi avaliado por meio de validação cruzada com cinco folds.

Apesar dos resultados positivos, a acurácia, isoladamente, não garante que o modelo seja adequado para uma aplicação real. Como se trata de um problema relacionado à detecção de incêndios, é necessário investigar outras métricas, principalmente o recall da classe positiva e a ocorrência de falsos negativos.

