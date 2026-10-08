<h1 align="center">Análise de Dados E-commerce</h1>

## 📚 Objetivo

Este projeto tem como objetivo realizar uma **análise de dados de transações de clientes de uma loja virtual**, utilizando Python, Pandas e SQLite para organização, tratamento e consulta dos dados.

Ao final, os dados tratados são utilizados na construção de um **dashboard interativo no Power BI**, permitindo visualizar e analisar os principais indicadores de desempenho do e-commerce.

---

## 📊 Dados

O projeto utiliza duas tabelas principais:

- `TB_TRANSACOES.csv` — dados relacionados às transações realizadas.
- `TB_CLIENTES.csv` — informações dos clientes.

As tabelas são carregadas utilizando **Pandas** e posteriormente armazenadas em um banco de dados **SQLite**.

---

## 🐍 Tratamento dos Dados

Os arquivos CSV são carregados com Pandas:

```python
df_transacoes = pd.read_csv("TB_TRANSACOES.csv", delimiter=';')
df_clientes = pd.read_csv("TB_CLIENTES.csv", delimiter=';')
```

Em seguida, os DataFrames são armazenados em um banco SQLite:

```python
conn = sqlite3.connect('projeto.db')

df_transacoes.to_sql('tb_transacoes', conn, index=False, if_exists='replace')

df_clientes.to_sql('tb_clientes', conn, index=False, if_exists='replace')
```

---

## 🗄️ Consultas SQL

Foi criada uma função para executar consultas SQL e retornar os resultados como DataFrame:

```python
def run_query(query):
    return pd.read_sql_query(query, conn)
```

Para relacionar os clientes às suas respectivas transações, foi utilizado um **INNER JOIN** através da coluna `id_client`.

```sql
SELECT 
    A.*, 
    COUNT(B.id_client) AS Total_Purchases, 
    SUM(B.Price) AS Total_Spent 
FROM tb_clientes AS A
INNER JOIN tb_transacoes AS B
    ON A.Id_client = B.id_client
GROUP BY A.Id_client
ORDER BY Total_Purchases DESC
```

O `INNER JOIN` foi escolhido porque a análise tem como foco os **clientes que realizaram compras**.

Dessa forma, registros de transações sem cliente associado e clientes sem compras registradas não fazem parte do resultado final da análise.

---

## 📈 Métricas Criadas

Foram criadas duas novas métricas para consolidar as informações de cada cliente:

- Total_Purchases → quantidade de compras realizadas pelo cliente.
- Total_Spent → valor total gasto pelo cliente.

Essa abordagem permite que cada cliente seja representado em uma única linha, evitando a repetição de registros causada por múltiplas transações.

Após a consulta, os dados consolidados são exportados para:

```python
result_df.to_csv('dados_ecommerce_final.csv', index=False)
```

---

## 📊 Dashboard

Os dados tratados foram utilizados para desenvolver um **dashboard interativo no Power BI**, permitindo analisar o desempenho das vendas por diferentes dimensões.

### Principais indicadores

| Indicador                | Resultado   |
|------------------------- |-----------: |
| Preço médio dos produtos |      $75,78 |
| Total de vendas          |         170 |
| Ticket médio             |   $1,29 mil |
| Faturamento total        | $218,78 mil |

### Análises realizadas

O dashboard apresenta análises de:

- 📍 Desempenho por estado
- 👥 Desempenho por gênero
- 💼 Desempenho por profissão
- 🛍️ Desempenho por categoria de produto

Entre os estados analisados, **CA, TX e DC** apresentaram os melhores desempenhos.

Em relação ao gênero, **Female (47,02%)** e **Male (41,69%)** concentraram a maior parte das vendas.

Entre as profissões com maior volume de compras destacaram-se **Teacher**, **Senior Cost Accountant** e **Project Manager**. Nas categorias de produtos, destacaram-se **Beauty**, **Baby** e **Electronics**.

---

## 🎯 Resultado 

Os resultados demonstram o desempenho das vendas do e-commerce e permitem identificar os estados, gêneros, profissões e categorias de produtos com maior participação nas vendas.

O projeto demonstra como a integração entre **Python, Pandas, SQL, SQLite e Power BI** pode ser utilizada para transformar dados brutos de um e-commerce em informações organizadas e indicadores para análise de desempenho.

---

## 📚 O Que Aprendi

Durante o desenvolvimento deste projeto, foram trabalhados conceitos de:

- Manipulação de dados com **Pandas**
- Leitura e exportação de arquivos **CSV**
- Criação e utilização de banco de dados **SQLite**
- Consultas utilizando **SQL**
- `INNER JOIN`
- `GROUP BY`
- `COUNT()` e `SUM()`
- Agregação de dados
- Criação de métricas para análise
- Preparação de dados para **Business Intelligence**
- Construção de dashboards no **Power BI**
- Análise de indicadores de vendas

---

## 🛠️ Tecnologias Utilizadas

- Python
- Pandas
- SQLite
- SQL
- Power BI
- Jupyter Notebook
- CSV
- Git
- GitHub

### Blibliotecas Utilizadas:

```python
import sqlite3
import pandas as pd
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
5. Visualize o Dashboard no Power BI

Após executar a análise, abra o arquivo `Sales.pbix` no Power BI Desktop para visualizar o dashboard interativo e explorar os principais indicadores e análises do projeto.

> **Observação:** os arquivos `TB_CLIENTES.csv` e `TB_TRANSACOES.csv` devem estar no diretório esperado pelo código.

---

## 📁 Estrutura do Projeto

```
📂 5 - SQL
│
├── 📄 TB_TRANSACOES.csv
├── 📄 TB_CLIENTES.csv
├── 📄 Projeto.ipynb
├── 📄 projeto.db
├── 📄 dados_ecommerce_final.csv
├── 📄 Sales.pbix
├── 📄 Sales.pdf
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Resultado Final

**Python → SQLite → SQL → Dados Consolidados → Power BI → Dashboard**

O projeto demonstra um fluxo completo de **tratamento, consulta, consolidação e visualização de dados**, desde os arquivos CSV até a apresentação dos principais indicadores do e-commerce.

