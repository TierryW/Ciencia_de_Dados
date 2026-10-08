<h1 align="center">Modelo de Árvore de Decisão para Credit Score</h1>

## 📚 Objetivo

Este projeto teve como objetivo desenvolver um **modelo preditivo de análise de crédito** utilizando o algoritmo de **Árvore de Decisão**, aplicado aos dados de Credit Score.

O projeto faz parte da etapa de Machine Learning da análise de crédito, utilizando dados previamente tratados, divididos entre treinamento e teste e balanceados para melhorar o aprendizado do modelo.

Além do treinamento e avaliação do modelo, também foi analisada a **importância das variáveis**, buscando entender quais características possuem maior influência nas decisões da árvore.

---

## 🔎 Preparação dos Dados

Antes da aplicação do algoritmo, os dados passaram por etapas de preparação, incluindo:

- Coleta e análise dos dados.
- Verificação dos tipos das variáveis.
- Tratamento de dados nulos.
- Verificação das variáveis categóricas.
- Análise univariada.
- Análise bivariada.
- Análise de correlação.
- Tratamento das variáveis categóricas.
- Divisão dos dados em treinamento e teste.
- Balanceamento dos dados de treinamento.

Para o treinamento foram utilizados os arquivos:

- `X_train_balanced.csv`
- `y_train_balanced.csv`

Enquanto os dados de teste foram armazenados em:

- `X_test.csv`
- `y_test.csv`

---

## 🌳 Modelo de Árvore de Decisão

Foi utilizado o algoritmo `DecisionTreeClassifier` da biblioteca **Scikit-learn**, utilizando o critério **Gini**:

```python
arvore = DecisionTreeClassifier(criterion='gini',random_state=0)
```

Após o treinamento, o modelo foi utilizado para realizar previsões nos conjuntos de treinamento e teste.

---

## 📊 Avaliação do Modelo

O modelo foi avaliado utilizando:

- Acurácia
- Precisão
- Recall
- F1-score
- Matriz de Confusão

### 🧪 Treinamento

Durante o treinamento, a árvore conseguiu classificar corretamente **100% das previsões** nas categorias de Credit Score.

Esse resultado demonstra um desempenho muito alto sobre os dados utilizados para o aprendizado. Entretanto, uma acurácia de 100% no treinamento pode ser um **indicativo de que o modelo está se ajustando excessivamente aos dados utilizados no aprendizado.**

A pequena diferença entre os resultados de treinamento e teste indica que, apesar do desempenho perfeito no treinamento, o modelo conseguiu generalizar bem para os dados de teste, não havendo evidências fortes de overfitting neste experimento.

### 🧪 Teste

Ao aplicar o modelo aos dados de teste, foi observado apenas **um erro de classificação**.

Os principais resultados foram:

- Acurácia: 98%
- Recall: 100%
- Precisão da classe 0: 86%
- F1-score da classe 0: 92%
- F1-score da classe 1: 98%

Apesar do erro em uma classificação, o modelo apresentou um desempenho bastante satisfatório no conjunto de teste.

---

## 📌 Matriz de Confusão

A matriz de confusão foi utilizada para visualizar os acertos e erros do modelo em cada classe.

Foram geradas matrizes de confusão tanto para o conjunto de treinamento quanto para o conjunto de teste utilizando o **Plotly**.

Essa análise permitiu identificar que o modelo apresentou poucos erros de classificação, principalmente no conjunto de teste.

---

## 🔍 Importância das Features

Também foi analisada a importância das variáveis utilizadas pela Árvore de Decisão.

As duas principais features identificadas foram:

- `Home Ownership_encoded`
- `Income`

A variável **`Income`** foi responsável pela primeira divisão da árvore, indicando sua importância para as decisões realizadas pelo modelo.

Além dela, outras variáveis contribuíram para as decisões em níveis mais profundos, como:

- `Age`
- `Home Ownership_encoded`
- `Number of Children`

---

## 🌳 Visualização da Árvore

A árvore de decisão foi visualizada utilizando o `plot_tree()` do Scikit-learn.

A árvore original apresentou **4 níveis de profundidade**.

Também foi possível observar diversos nós com `gini = 0.0`, indicando que as amostras presentes nesses nós pertenciam à mesma classe.

Isso demonstra que o modelo conseguiu separar determinados grupos de dados de forma eficiente.

---

## 🔬 Redução das Features

Após analisar a importância das variáveis, foi criado um segundo modelo utilizando somente as duas principais features:

```python
X_train_reduzido = X_train[['Home Ownership_encoded', 'Income']]

X_test_reduzido = X_test[['Home Ownership_encoded', 'Income']]
```

O objetivo foi verificar se a redução da quantidade de variáveis poderia gerar um modelo mais simples sem comprometer significativamente seu desempenho.

### Resultado

A árvore reduzida apresentou:

- Acurácia: 95%
- Profundidade: 6 níveis

Apesar da redução da quantidade de variáveis, a árvore ficou **mais profunda visualmente**, passando de 4 para 6 níveis.

Com menos atributos disponíveis, o algoritmo precisou utilizar mais divisões para realizar suas classificações.

Além disso, houve uma redução no desempenho, passando de **98% para 95% de acurácia**.

Portanto, neste caso, a redução das features não tornou o modelo mais simples nem melhorou seu desempenho.

---

## ⚖️ Comparação com Naive Bayes

O projeto também permitiu comparar a Árvore de Decisão com o modelo Naive Bayes, desenvolvido anteriormente para o mesmo problema.

| Modelo            | Acurácia | Recall |
| ----------------- | -------: | -----: |
| Naive Bayes       |      92% |    96% |
| Árvore de Decisão |      98% |   100% |

A **Árvore de Decisão apresentou melhor desempenho** nos dados analisados.

Enquanto o Naive Bayes obteve aproximadamente 92% de acurácia e 96% de recall, a Árvore de Decisão alcançou 98% de acurácia e 100% de recall.

Uma possível explicação está na forma como os algoritmos trabalham com as características dos dados. O Naive Bayes considera uma independência entre os atributos, enquanto a Árvore de Decisão consegue utilizar diferentes combinações de variáveis para realizar suas divisões e classificações.

---

## 💡 Conclusão

A Árvore de Decisão apresentou um desempenho superior ao Naive Bayes neste conjunto de dados, alcançando **98% de acurácia e 100% de recall** no conjunto de teste.

A análise das features também permitiu identificar `Home Ownership_encoded` e `Income` como as principais variáveis utilizadas pelo modelo.

Embora a redução das variáveis tenha diminuído a quantidade de atributos utilizados, o modelo reduzido apresentou uma profundidade maior e uma acurácia inferior, indicando que, para este conjunto de dados, manter mais informações permitiu que a árvore realizasse suas decisões de forma mais eficiente.

De forma geral, o projeto demonstrou a aplicação prática de **Machine Learning para classificação de Credit Score**, desde a preparação dos dados até o treinamento, avaliação, interpretação e comparação de modelos.

---

## 📚 O Que Aprendi

- Aplicação de **Árvore de Decisão** para classificação.
- Utilização do `DecisionTreeClassifier`.
- Avaliação de modelos com acurácia, precisão, recall e F1-score.
- Interpretação de matriz de confusão.
- Visualização de árvores de decisão.
- Análise de importância das features.
- Redução de variáveis para comparação de modelos.
- Análise de profundidade da árvore.
- Comparação entre diferentes algoritmos de Machine Learning.
- Utilização de dados balanceados para treinamento.

---

## 🛠️ Tecnologias e Ferramentas

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Plotly
- Jupyter Notebook
- CSV
- Git
- GitHub

### Blibliotecas Utilizadas:

```python
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
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

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise e as visualizações.**

> **Observação:** os arquivos `X_train_balanced.csv`, `y_train_balanced.csv`, `X_test.csv` e `y_test.csv` devem estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 4 - Arvore_Decisao
├── 📄 Projeto.ipynb
├── 📄 X_train_balanced.csv
├── 📄 y_train_balanced.csv
├── 📄 X_test.csv
├── 📄 y_test.csv
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Resultado Final

A **Árvore de Decisão** apresentou o melhor desempenho entre os modelos testados para este conjunto de dados, alcançando **98% de acurácia e 100% de recall**.

A análise também mostrou que `Home Ownership_encoded` e `Income` foram as features mais importantes para as decisões do modelo, contribuindo para a interpretação dos padrões utilizados na classificação do Credit Score.

