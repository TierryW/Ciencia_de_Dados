<h1 align="center">Segmentação de Clientes com K-Means</h1>

## 📚 Objetivo

Este projeto tem como objetivo aplicar conceitos de **modelagem e Machine Learning não supervisionado** para realizar uma segmentação de clientes utilizando o algoritmo de **clustering K-Means**.

A análise busca identificar grupos de clientes com características semelhantes a partir de variáveis relacionadas à **idade, renda anual e comportamento de consumo**.

Ao final, os clusters são avaliados por meio de métricas de qualidade e utilizados para identificar diferentes perfis de clientes que podem auxiliar na definição de estratégias de marketing.

---

## 📊 Dados

O projeto utiliza o dataset:

- `Mall_Customers.csv`

As principais variáveis utilizadas na análise são:

- `Age` — idade do cliente.
- `Annual Income (k$)` — renda anual do cliente.
- `Spending Score (1-100)` — pontuação de consumo do cliente.

As colunas `CustomerID` e `Gender` foram removidas antes da aplicação do algoritmo, pois não foram utilizadas na segmentação.

---

## 🔎 Análise Exploratória

Inicialmente, foram realizadas algumas etapas de exploração dos dados:

- Visualização das primeiras linhas com `head()`.
- Análise estatística com `describe()`.
- Verificação dos tipos de dados com `dtypes`.
- Verificação de valores ausentes com `isnull().sum()`.
- Análise de possíveis outliers utilizando BoxPlot.
- Análise das relações entre as variáveis utilizando `pairplot`.
- Visualização da relação entre renda anual e pontuação de consumo.

A análise mostrou que o conjunto de dados não possui valores nulos.

Também foi analisada a variável `Annual Income (k$)` por meio de um BoxPlot. Apesar da presença de valores extremos, eles não foram considerados outliers problemáticos e, por isso, não foi realizado nenhum tratamento nessa variável.

---

## 🧹 Pré-processamento

Após a análise exploratória, foram removidas as colunas:

```python
df = df.drop(columns=['CustomerID', 'Gender'])
```

As variáveis utilizadas no modelo foram:

```python
padronizar = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
```

Para colocar as variáveis na mesma escala, foi utilizado o `StandardScaler`:

```python
sc = StandardScaler()

df_padronizado[padronizar] = sc.fit_transform(df[padronizar])
```

A padronização foi realizada antes da aplicação do K-Means para evitar que variáveis com escalas diferentes tivessem influência desproporcional no processo de clusterização.

---

## 📐 Método do Cotovelo

Para determinar a quantidade adequada de clusters, foi utilizado o **Método do Cotovelo (Elbow Method)**.

Foram testados valores de `k` entre 1 e 10 e calculada a inércia de cada modelo.

```python
inercia = []

for k in range(1, 11):
    modelo = KMeans(n_clusters=k, random_state=42, n_init=10)

    modelo.fit(df_padronizado)
    inercia.append(modelo.inertia_)
```

A análise do gráfico mostrou uma redução significativa da inércia até **k = 5**. Após esse ponto, a redução tornou-se mais gradual.

Dessa forma, foram utilizados **5 clusters**, buscando equilibrar a qualidade da segmentação e a simplicidade do modelo.

---

## 🤖 Modelo K-Means

O modelo foi configurado utilizando:

```python
kmeans = KMeans(n_clusters=5, n_init=10, random_state=42)

kmeans.fit(df_padronizado)
```

Após o treinamento, foram obtidos os rótulos dos clusters e seus respectivos centroides:

```python
centroides = kmeans.cluster_centers_
labels = kmeans.labels_
```

Os centroides também foram convertidos novamente para a escala original para facilitar a interpretação dos perfis de clientes.

---

## 📊 Avaliação do Modelo

A qualidade da segmentação foi avaliada utilizando três métricas:

- Silhouette Score
- Calinski-Harabasz
- Davies-Bouldin

Resultados obtidos:

|      Métrica      |  Resultado |
| ----------------: | ---------: |
|  Silhouette Score |      0.417 |
| Calinski-Harabasz |     125.10 |
|   Davies-Bouldin  |      0.875 |

O **Silhouette Score de 0.417** indica uma separação satisfatória entre os grupos, embora exista alguma sobreposição entre os clusters.

O índice **Calinski-Harabasz de 125.10** reforça a existência de uma estrutura consistente nos grupos encontrados.

Já o índice **Davies-Bouldin de 0.875** indica uma segmentação adequada, considerando que valores menores representam melhor separação e compactação dos clusters.

Em conjunto, os resultados indicam que a escolha de **5 clusters** foi adequada para o conjunto de dados analisado.

---

## 👥 Segmentação dos Clientes

A análise do gráfico `Spending Score (1-100)` × `Annual Income (k$)` permitiu identificar **cinco** perfis principais:

### Cluster 0 — Baixa renda e baixo consumo

Clientes com menor renda anual e baixo `Spending Score`, representando consumidores com menor poder aquisitivo e menor nível de consumo.

### Cluster 1 — Baixa renda e alto consumo

Clientes com renda anual mais baixa, mas que apresentam elevado `Spending Score`, indicando um comportamento de consumo elevado mesmo com menor renda.

### Cluster 2 — Alta renda e alto consumo

Clientes com alta renda anual e elevado `Spending Score`.

Esse grupo representa os clientes mais valiosos para o shopping, pois combina alto poder aquisitivo com alto nível de consumo.

### Cluster 3 — Alta renda e baixo consumo

Clientes com alta renda anual, mas baixo `Spending Score`.

Esse grupo apresenta potencial para estratégias de fidelização e campanhas direcionadas para estimular o consumo.

### Cluster 4 — Renda e consumo intermediários

Clientes com renda e `Spending Score` intermediários, apresentando um comportamento de consumo mais equilibrado.

---

## 📈 Visualização dos Clusters

Foram utilizados gráficos de dispersão para visualizar a distribuição dos grupos.

### Age × Annual Income

A relação entre idade e renda mostra que a idade, isoladamente, não é suficiente para separar claramente os clientes.

Entretanto, quando analisada em conjunto com a renda e o comportamento de consumo, a idade contribui para identificar diferenças entre os grupos.

### Spending Score × Annual Income

A relação entre `Spending Score (1-100)` e `Annual Income (k$)` apresenta uma separação mais evidente entre os grupos.

Essas duas variáveis são as principais responsáveis pela formação dos cinco segmentos identificados.

---

## 🎯 Estratégias de Marketing

A segmentação pode ser utilizada para apoiar decisões estratégicas:

- **Alta renda + alto consumo:** benefícios exclusivos e programas de fidelização.
- **Alta renda + baixo consumo:** campanhas promocionais personalizadas para estimular compras.
- **Baixa renda + alto consumo:** promoções e programas de descontos.
- **Baixa renda + baixo consumo:** estratégias focadas em produtos de menor valor.
- **Perfil intermediário:** campanhas equilibradas para aumentar gradualmente o nível de consumo.

Essa abordagem permite direcionar estratégias de marketing de acordo com as características de cada grupo de clientes.

---

## 📚 O Que Aprendi

- Análise exploratória de dados.
- Estatística descritiva.
- Identificação de valores ausentes.
- Análise de possíveis outliers.
- Visualização de dados.
- Pré-processamento de dados.
- Padronização com `StandardScaler`.
- Machine Learning não supervisionado.
- Algoritmo K-Means.
- Método do Cotovelo.
- Análise de centroides.
- Avaliação de clusters.
- Silhouette Score.
- Calinski-Harabasz.
- Davies-Bouldin.
- Segmentação de clientes.
- Interpretação de clusters.
- Aplicação de Machine Learning em estratégias de negócio.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Jupyter Notebook
- Git
- GitHub

### Bibliotecas Utilizadas

```python
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
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

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise, o treinamento do modelo e as visualizações dos clusters.**

> **Observação:** o arquivo `Mall_Customers.csv` deve estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 6 - K-Means
│
├── 📄 Mall_Customers.csv
├── 📄 Projeto.ipynb
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

**Dados → Análise Exploratória → Pré-processamento → StandardScaler → Método do Cotovelo → K-Means → Avaliação → Segmentação de Clientes**

O projeto demonstra como o **K-Means** pode ser utilizado para identificar diferentes perfis de clientes a partir de características de idade, renda e comportamento de consumo.

A segmentação obtida pode auxiliar empresas na criação de **estratégias de marketing mais direcionadas**, permitindo adaptar campanhas e ações comerciais de acordo com o perfil de cada grupo.

