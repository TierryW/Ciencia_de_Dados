# Tratamento dos dados 1
Vamos continuar o nosso projeto, realizando o tratamento de dados. Para facilitar, algumas questões, especifiquei os nomes dos campos, pois iremos usar em outros exercícios. Passo a passo:

- Verifique a quantidade de linhas e colunas e armazene na variável `linhas_colunas`.

- Verifique os tipos de dados de todo o dataframe e armazene na variável `tipos`.

- Verifique a quantidade de valores nulos e armazene na variável `nulos`.

- Substitua, no mesmo dataframe, os valores nulos das colunas `Temporada` e `Marca` por `Não Definido`.

# Tratamento dos dados 2
Vamos continuar a partir dos dados gerados no exercício anterior.

- Trate os campos `Marca`; `Material` e `Temporada` para os valores serem em minúsculo

- Mantenha apenas os registros que tenham no mínimo 8 valores não nulos.

# Tratamento dos dados 3
Dando continuação ao exercício, vamos filtrar os produtos com maiores quantidades de comentários (N_Avaliações). Para isso, utilizaremos o método do Intervalo Interquartil (IQR).

Passos:

- Calcular o IQR: O IQR é a diferença entre o terceiro quartil (Q3) e o primeiro quartil (Q1): `iqr = q3 - q1`.
- Determinar o Limite Superior para Outliers: O limite superior é calculado como `limite_alto = q3 + 1.5 * iqr`.
- Filtrar Produtos Acima do Limite: Filtre os produtos que têm `N_Avaliações` maior que `limite_alto` e armazene o resultado na variável `df_avaliados`.


# Tratamento dos dados 4
Finalize o exercício seguindo os passos abaixo:

- Converta a coluna Desconto para o tipo string.
- Modifique a coluna Desconto para exibir apenas o valor numérico do desconto (por exemplo, "18% OFF" deve se tornar "18").
- Crie duas novas colunas baseadas na coluna `Condicao`:
  - `Condicao_Atual`: Extraia a primeira parte do campo `Condicao` (por exemplo, "Novo | +10mil vendidos" deve se tornar "Novo").
  - `Qtd_Vendidos`: Extraia a quantidade de itens vendidos do campo `Condicao` (por exemplo, "Novo | +10mil vendidos" deve se tornar "+10mil"). Se não houver quantidade especificada, escreva "Nenhum".