<h1 align="center">Análise de Dados de Supermercado</h1>

## 📚 Objetivo

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (EDA)** a partir de uma base de dados de produtos de supermercado. 

A análise busca compreender o comportamento dos **preços e descontos dos produtos**, explorando diferenças entre categorias e marcas. Também foram utilizadas medidas estatísticas para identificar possíveis **valores discrepantes (outliers)** e compreender melhor a distribuição dos preços.

O projeto foi desenvolvido com foco na aplicação prática de conceitos de **Data Analysis**, desde a manipulação dos dados até a geração de visualizações e interpretação dos resultados.

---

## 🔎 Análise dos Dados

A análise foi realizada utilizando a base `BASE_SUPERMERCADO.csv`.

Inicialmente, os dados foram carregados utilizando **Pandas** e explorados para compreender sua estrutura e visualizar os primeiros registros.

Em seguida, foram realizadas análises agrupando os produtos por **categoria**, utilizando diferentes medidas estatísticas.

### 📌 Preço Médio

Foi calculado o preço médio dos produtos para cada categoria, permitindo comparar quais categorias apresentam os maiores e menores preços médios.

```python
df.groupby('Categoria')['Preco_Normal'].mean()
```

### 📌 Mediana dos Preços

Também foi calculada a mediana dos preços por categoria. A mediana foi utilizada como uma medida complementar à média para entender melhor a distribuição dos valores e reduzir a influência de valores extremos.

As categorias identificadas **acima da mediana** foram:

- belleza-y-cuidado-personal
- congelados
- frutas
- verduras
- lacteos
- instantaneos-y-sopas

A categoria identificada **abaixo da mediana** foi:

* comidas-preparadas

### 📌 Desvio Padrão

O desvio padrão foi utilizado para analisar a **variabilidade dos preços** dentro de cada categoria.

Essa análise permite identificar categorias nas quais os preços apresentam maior dispersão em relação à média.

### 📌 Média x Mediana

A comparação entre média e mediana também foi utilizada para observar possíveis comportamentos relacionados a valores extremos.

- Média > Mediana: pode indicar a presença de valores elevados que influenciam a média.
- Mediana > Média: pode indicar a presença de valores mais baixos influenciando a média.

Essa comparação foi utilizada como uma etapa inicial para investigar possíveis **outliers**.

---

## 📊 Identificação de Outliers

Para aprofundar a análise, foi utilizado um **Box Plot** para visualizar a distribuição dos preços da categoria `lacteos`.

O gráfico permite observar a concentração dos preços e identificar valores que se encontram fora do comportamento esperado da distribuição.

A análise indicou que a categoria **lacteos apresenta produtos com preços acima da média**, destacando-se pela presença de possíveis valores discrepantes superiores.

---

## 💰 Análise de Descontos

Também foi analisado o **desconto médio por categoria**.

Para isso, os dados foram agrupados pela coluna `Categoria` e foi calculada a média da coluna `Desconto`.

O resultado foi representado por meio de um **Gráfico de Barras**, facilitando a comparação entre as categorias.

```python
desconto_categoria = df.groupby('Categoria')['Desconto'].mean()
```

Essa visualização permite identificar quais categorias apresentam maiores níveis médios de desconto.

---

## 🏷️ Análise por Categoria e Marca

Além da análise por categoria, os descontos foram analisados considerando simultaneamente **categoria e marca**.

```python
categoria_marca_desconto = df.groupby(['Categoria', 'Marca'])['Desconto'].mean()
```

Para representar essa relação, foi utilizado um **Treemap**, permitindo visualizar de forma hierárquica:

**Categoria → Marca → Desconto Médio**

Essa visualização facilita a identificação das marcas e categorias que apresentam maior participação nos descontos analisados.

---

## 📈 Visualizações

Foram utilizadas diferentes visualizações para facilitar a interpretação dos dados:

### 📦 Box Plot

Utilizado para analisar a distribuição dos preços da categoria `lacteos` e investigar possíveis outliers.

### 📊 Gráfico de Barras

Utilizado para comparar o desconto médio entre as diferentes categorias.

### 🗺️ Treemap

Utilizado para explorar a relação entre **categorias, marcas e desconto médio**.

As visualizações foram desenvolvidas utilizando **Plotly Express**, permitindo gerar gráficos interativos.

---

## 💡 Principais Insights

A análise permitiu identificar alguns comportamentos relevantes na base de dados:

- As categorias apresentam diferenças significativas na distribuição dos preços.
- A comparação entre **média e mediana** auxilia na identificação de possíveis influências de valores extremos.
- A categoria `lacteos` apresentou destaque na análise de preços acima da média.
- O **desvio padrão** permite observar a variabilidade dos preços dentro de cada categoria.
- Existem diferenças nos níveis médios de desconto entre as categorias.
- A análise conjunta de **categoria e marca** permite uma visão mais detalhada do comportamento dos descontos.

---

## 🧠 O que Aprendi

Durante o desenvolvimento deste projeto, pratiquei conceitos importantes de **Análise de Dados**, incluindo:

- Importação e leitura de dados utilizando **Pandas**.
- Exploração inicial de datasets.
- Manipulação e filtragem de DataFrames.
- Agrupamento de dados utilizando `groupby()`.
- Cálculo de **média, mediana e desvio padrão**.
- Ordenação de resultados.
- Análise da distribuição dos dados.
- Identificação de possíveis **outliers**.
- Criação de visualizações para apoiar a análise.
- Interpretação de resultados estatísticos.
- Utilização de **Plotly Express** para visualizações interativas.
- Transformação de dados em informações que podem apoiar a tomada de decisão.

---

## 🛠️ Tecnologias e Ferramentas

- Python
- Pandas
- Plotly Express
- Jupyter Notebook
- CSV
- Git
- GitHub

### Blibliotecas Utilizadas:

```python
import pandas as pd
import plotly.express as px
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

4. Execute o Jupyter Notebook

```bash
jupyter notebook
```

**Abra o arquivo `Projeto.ipynb` e execute as células para reproduzir a análise e as visualizações.**

> **Observação:** o arquivo `BASE_SUPERMERCADO.csv` deve estar disponível no diretório utilizado pelo notebook.

---

## 📁 Estrutura do Projeto

```
📂 1 - Fundamentos_Descoberta_Dados
│
├── 📄 Projeto.ipynb
├── 📄 BASE_SUPERMERCADO.csv
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

Este projeto demonstra a aplicação prática de técnicas de **Análise Exploratória de Dados** para transformar uma base de produtos de supermercado em informações úteis sobre **preços, descontos, categorias e marcas**.

A utilização conjunta de **Pandas e Plotly** permitiu realizar o processo de tratamento, análise e visualização dos dados, desenvolvendo uma abordagem baseada em dados para identificar padrões e possíveis comportamentos relevantes.

O projeto faz parte da minha evolução na área de **Data Analysis**, com foco no desenvolvimento de habilidades em **Python, análise exploratória, visualização de dados e interpretação de informações**.

