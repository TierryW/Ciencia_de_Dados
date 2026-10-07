<h1 align="center">Análise de Credit Score</h1>

## 📚 Objetivo

Este projeto tem como objetivo realizar uma **Análise Exploratória de Dados (EDA)** sobre uma base de clientes e seus respectivos **Credit Scores**, buscando identificar padrões e relações entre características como idade, renda, escolaridade, estado civil, gênero, quantidade de filhos e propriedade de imóvel.

Além da análise exploratória, o projeto também contempla uma etapa de **preparação dos dados para Machine Learning**, incluindo tratamento de valores ausentes, transformação de variáveis categóricas, análise de correlação, divisão dos dados, balanceamento das classes e padronização das variáveis.

O projeto foi desenvolvido com foco na aplicação prática de conceitos de **Data Analysis e preparação de dados para modelos preditivos**.

---

## 🔎 Análise dos Dados

A análise foi realizada utilizando a base `CREDIT_SCORE.csv`.

Inicialmente, os dados foram carregados utilizando **Pandas** e foi realizada uma análise inicial da estrutura do dataset, incluindo tipos de dados, valores ausentes e estatísticas descritivas.

### 🧹 Tratamento dos Dados

A coluna `Income` apresentava valores no formato de texto. Foi necessário remover os separadores e converter os valores para o formato numérico.

A coluna `Age` também foi convertida para o tipo inteiro.

Durante a análise de valores ausentes, foi identificado que a coluna `Age` possuía aproximadamente **20% de dados nulos**.

Como essa quantidade representa uma parcela significativa da base, os registros não foram removidos. Em vez disso, os valores ausentes foram preenchidos utilizando a **mediana da idade**.

A escolha da mediana foi feita após comparar os valores de média e mediana da variável `Age`, que apresentaram valores próximos.

---

## 📊 Análise Exploratória

Foram analisadas as principais variáveis da base por meio de estatísticas descritivas e visualizações.

### 👥 Gênero

A distribuição de gênero apresentou um certo equilíbrio, com uma pequena predominância do gênero **Female**.

### 🎓 Escolaridade

A categoria **Bachelor's Degree** apresentou a maior participação entre os níveis de escolaridade, representando aproximadamente **25% dos dados**.

Também foi analisada a relação entre escolaridade e renda, sendo observado que **Master's Degree** e **Doctorate** apresentam as maiores medianas salariais.

### 💍 Estado Civil

A categoria **Married** apresentou a maior participação na variável `Marital Status`.

Também foi analisada a relação entre estado civil e idade. A mediana da idade foi de aproximadamente:

- Married: 37 anos
- Single: 33 anos

Na base analisada, pessoas casadas apresentam uma mediana de idade superior à das pessoas solteiras.

### 🏠 Propriedade de Imóvel

A categoria **Owned** apresentou predominância na variável `Home Ownership`, representando aproximadamente **67% dos dados**.

Também foi analisada a relação entre propriedade de imóvel e Credit Score.

### 💳 Credit Score

A categoria **High** representa aproximadamente **68% da base**, enquanto a categoria **Low** representa aproximadamente **9%**.

Essa diferença entre as classes é importante para a etapa posterior de Machine Learning, pois representa um **desbalanceamento dos dados**.

---

## 📈 Análise de Outliers

Foram utilizados **Box Plots** para analisar as variáveis:

- `Age`
- `Income`
- `Number of Children`

A variável `Number of Children` apresentou valores que poderiam ser identificados visualmente como possíveis outliers.

Entretanto, esses valores não foram removidos, pois representam uma característica real da população analisada. Ter três filhos, por exemplo, pode ser menos frequente na base, mas não representa necessariamente um erro ou valor inválido.

Dessa forma, os valores foram **mantidos na análise**.

---

## 🔗 Relação entre as Variáveis

Foram realizadas análises relacionando diferentes características dos clientes com o Credit Score.

### 💳 Credit Score x Education

A análise mostrou uma diferença na distribuição dos níveis de escolaridade entre os grupos de Credit Score.

Na base analisada, níveis de escolaridade como **Doctorate, Master's Degree e Bachelor's Degree** apresentam maior presença entre clientes com **High Credit Score**, enquanto **High School Diploma** e **Associate's Degree** apresentam maior participação entre clientes com scores mais baixos.

### 💰 Credit Score x Income

Foi analisada a mediana da renda para cada grupo de Credit Score.

Os resultados observados foram aproximadamente:

- High: 9,5 milhões
- Low: 3,25 milhões

Na base analisada, clientes com maior renda apresentam maior mediana de Credit Score.

### 🏠 Credit Score x Home Ownership

Também foi analisada a relação entre `Home Ownership` e `Credit Score`.

A categoria **Owned** apresentou forte presença entre os clientes classificados com **High Credit Score**.

Esse comportamento indica que a propriedade de imóvel pode apresentar uma relação relevante com a classificação de crédito dentro da base analisada.

### 🎓 Education x Income

A análise da renda por escolaridade mostrou que **Master's Degree** e **Doctorate** apresentam as maiores medianas de renda.

### 👥 Gender x Income

A mediana da renda também foi analisada por gênero.

Os valores observados foram aproximadamente:

- Male: 10,5 milhões
- Female: 7 milhões

Na base analisada, homens apresentaram uma mediana salarial superior à das mulheres.

---

## 🔥 Matriz de Correlação

Foi criada uma matriz de correlação para analisar a relação entre as variáveis numéricas.

Entre as relações observadas estão:

- `Marital Status` × `Number of Children`
- `Home Ownership` × `Income`
- `Marital Status` × `Home Ownership`
- `Age` × `Credit Score`
- `Home Ownership` × `Age`

Também foi observada uma relação forte entre **idade e renda** na base analisada.

A matriz de correlação foi utilizada como uma ferramenta exploratória para compreender quais variáveis apresentam maior associação entre si.

---

## 🤖 Preparação para Machine Learning

Após a análise exploratória, os dados foram preparados para utilização em um modelo de Machine Learning.

### 🔤 Codificação das Variáveis

As variáveis categóricas foram transformadas em valores numéricos.

Foi utilizado **Label Encoding** para:

- `Gender`
- `Marital Status`
- `Home Ownership`
- `Credit Score`

Para a variável `Education`, foi utilizado **One-Hot Encoding**, criando variáveis binárias para representar as diferentes categorias de escolaridade.

---

## ⚖️ Balanceamento dos Dados

A distribuição da variável `Credit Score` apresentou um desbalanceamento significativo:

- High: aproximadamente 68%
- Low: aproximadamente 9%

Esse desbalanceamento pode prejudicar o treinamento de um modelo, fazendo com que ele tenha maior facilidade para classificar a classe majoritária.

Para lidar com esse problema, foi utilizado o **SMOTE (Synthetic Minority Over-sampling Technique)**.

O SMOTE foi aplicado **somente nos dados de treinamento**, aumentando a representação das classes minoritárias sem alterar os dados de teste.

---

## 📏 Padronização dos Dados

Após o balanceamento, foi utilizado o **StandardScaler** para padronizar as variáveis numéricas.

A padronização foi aplicada da seguinte forma:

- `X_train`: utilizado para ajustar o scaler.
- `X_test`: transformado utilizando o scaler ajustado no treinamento.

Essa abordagem evita que informações do conjunto de teste sejam utilizadas durante o processo de treinamento.

---

## 📂 Separação dos Dados

A variável `Credit Score` foi definida como variável alvo (`y`), enquanto as demais variáveis foram utilizadas como características (`X`).

Os dados foram divididos em:

- 75% para treinamento
- 25% para teste

Foi utilizado `random_state=42` para garantir a reprodutibilidade da divisão.

---

## 💾 Dados Processados

Após o processo de preparação, foram exportados os conjuntos utilizados no desenvolvimento do modelo:

```
y_train_balanced.csv
X_train_balanced.csv
y_test.csv
X_test.csv
```

Esses arquivos podem ser utilizados posteriormente na etapa de treinamento e avaliação dos modelos de Machine Learning.

---

## 🧠 O que Aprendi

Durante o desenvolvimento deste projeto, pratiquei conceitos importantes de **Data Analysis e preparação de dados para Machine Learning**, incluindo:

- Leitura e manipulação de arquivos CSV com **Pandas**.
- Identificação e tratamento de valores ausentes.
- Conversão e limpeza de dados numéricos.
- Análise estatística utilizando `describe()`.
- Cálculo de média e mediana.
- Análise de distribuição e possíveis outliers.
- Criação de gráficos utilizando **Plotly** e **Matplotlib**.
- Análise de variáveis categóricas.
- Análise de correlação entre variáveis.
- Label Encoding.
- One-Hot Encoding.
- Separação entre variáveis preditoras e variável alvo.
- Divisão entre dados de treinamento e teste.
- Balanceamento de classes utilizando **SMOTE**.
- Padronização utilizando **StandardScaler**.
- Exportação dos dados preparados para Machine Learning.

---

## 🛠️ Tecnologias e Ferramentas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Scikit-learn
- Imbalanced-learn
- Jupyter Notebook
- CSV
- Git
- GitHub

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

> **Observação:** mantenha o arquivo `CREDIT_SCORE.csv` no diretório utilizado pelo notebook.

---

## 📁 Estrutura do Projeto

```
📂 2 - Pre_Modelagem
│
├── 📄 Projeto.ipynb
├── 📄 CREDIT_SCORE.csv
├── 📄 X_train_balanced.csv
├── 📄 y_train_balanced.csv
├── 📄 X_test.csv
├── 📄 y_test.csv
├── 📄 requirements.txt
└── 📄 README.md
```

---

## 🎯 Conclusão

Este projeto apresenta uma análise completa de uma base de **Credit Score**, passando pelas principais etapas de um fluxo de análise de dados: **limpeza, tratamento, exploração, visualização, análise de relações entre variáveis e preparação para Machine Learning**.

A utilização de **Pandas, Plotly, Seaborn, Scikit-learn e SMOTE** permitiu transformar os dados brutos em uma base estruturada e preparada para uma etapa posterior de modelagem preditiva.

O projeto contribuiu para o desenvolvimento de habilidades em **Data Analysis, tratamento de dados, visualização, estatística e preparação de datasets para Machine Learning**.

