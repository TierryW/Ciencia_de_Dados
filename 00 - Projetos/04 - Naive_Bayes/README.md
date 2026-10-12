<h1 align="center">Modelo Preditivo de Credit Score</h1>

## 📚 Objetivo

Este projeto teve como objetivo desenvolver um **modelo preditivo de análise de crédito** utilizando o algoritmo **Naive Bayes**, aplicado a um conjunto de dados financeiros.

A proposta foi treinar um modelo capaz de classificar novos clientes de acordo com sua **pontuação de crédito**, utilizando dados previamente preparados e balanceados.

Além do treinamento do modelo, foram utilizadas métricas como **acurácia**, **recall** e **matriz de confusão** para avaliar seu desempenho.

---

## 🧠 Modelo Utilizado

Para a classificação foi utilizado o algoritmo Gaussian Naive Bayes (`GaussianNB`), disponível na biblioteca `scikit-learn`.

O modelo foi treinado utilizando os dados balanceados obtidos na etapa anterior do projeto:

- `X_train_balanced.csv`
- `y_train_balanced.csv`

Após o treinamento, o modelo foi avaliado tanto nos dados utilizados durante o aprendizado quanto em dados de teste que não foram utilizados no treinamento.

---

## 🔎 Avaliação do Modelo

### 📊 Dados de Treinamento

Nos dados utilizados para o treinamento, o modelo apresentou:

- Acurácia: 94,44%
- Recall: 94,44%

A matriz de confusão mostrou que a **classe 2** foi reconhecida com alto desempenho, enquanto a **classe 1** também apresentou poucos erros.

A **classe 0** foi a que apresentou maior confusão, principalmente com a classe 1, indicando que essas duas classes possuem características semelhantes dentro dos dados analisados.

---

### 📈 Dados de Teste

Nos dados que não foram utilizados durante o treinamento, os resultados foram:

- Acurácia: 92,68%
- Recall: 96,55%

Mesmo com uma pequena redução na acurácia em relação ao treinamento, o modelo manteve um bom desempenho no conjunto de teste.

A diferença entre os resultados de treinamento e teste foi relativamente pequena, indicando que o modelo conseguiu **generalizar bem para dados não utilizados durante o aprendizado**.

Assim como no treinamento, a maior dificuldade permaneceu na diferenciação entre as **classes 0 e 1**.

---

## 📌 Matriz de Confusão

A matriz de confusão foi utilizada para visualizar os acertos e erros do modelo em cada classe.

Ela permite identificar quais classes são reconhecidas corretamente e quais apresentam maior confusão durante as previsões.

Foram geradas matrizes de confusão tanto para os dados de treinamento quanto para os dados de teste utilizando o **Plotly**.

---

## 📊 Resultados

| Conjunto    | Acurácia | Recall |
| ----------- | -------: | -----: |
| Treinamento |   94.44% | 94.44% |
| Teste       |   92.68% | 96.55% |

Os resultados mostram que o modelo apresentou um desempenho consistente entre treinamento e teste.

A pequena diferença na acurácia sugere que o modelo não apresentou uma perda significativa de desempenho ao receber dados que não foram utilizados no treinamento.

---

## 💡 Conclusão

O projeto demonstrou a aplicação do **Naive Bayes** na classificação de clientes de acordo com sua pontuação de crédito.

O modelo apresentou bons resultados tanto nos dados de treinamento quanto nos dados de teste, alcançando **92,68% de acurácia e 96,55% de recall no conjunto de teste**.

A matriz de confusão mostrou que a principal dificuldade do modelo está na diferenciação entre as classes **0 e 1**.

De forma geral, os resultados indicam que o modelo conseguiu identificar os padrões presentes nos dados e apresentar um bom desempenho na classificação de novos registros.

A aplicação desse tipo de modelo pode auxiliar análises de crédito, fornecendo informações baseadas em dados para apoiar processos de avaliação de clientes e tomada de decisão.

---

## 📚 O Que Aprendi

- Aplicação do algoritmo **Naive Bayes** para classificação.
- Utilização do `GaussianNB` com `scikit-learn`.
- Treinamento de modelos utilizando dados balanceados.
- Avaliação de modelos utilizando **acurácia** e **recall**.
- Interpretação de **matrizes de confusão**.
- Comparação entre resultados de treinamento e teste.
- Análise de possíveis diferenças de desempenho entre os conjuntos.
- Utilização do **Plotly** para visualização dos resultados.

---

## 🛠️ Tecnologias e Ferramentas

- Python
- Pandas
- Scikit-learn
- Plotly
- Jupyter Notebook
- CSV
- Git
- GitHub

### Blibliotecas Utilizadas:

```python
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, recall_score
import plotly.figure_factory as ff 
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
📂 4 - Naive_Bayes
│
├── 📄 Projeto.ipynb
├── 📄 X_train_balanced.csv
├── 📄 y_train_balanced.csv
├── 📄 X_test.csv
├── 📄 y_test.csv
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

O modelo **Gaussian Naive Bayes** apresentou um bom desempenho na classificação do Credit Score, alcançando **92,68% de acurácia e 96,55% de recall nos dados de teste**.

O projeto representa uma etapa de aplicação prática de **Machine Learning em análise de crédito**, utilizando preparação de dados, treinamento, avaliação e interpretação dos resultados.

