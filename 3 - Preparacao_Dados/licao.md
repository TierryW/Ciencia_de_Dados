# Preparação de dados 1
Vamos continuar o nosso projeto, realizando agora a preparação dos dados. Seu código deve conter os passos a seguir:

- Verifique a quantidade de dados únicos para cada campo e armazene na variável `unicos`.
- Verifique as estatísticas dos campos numéricos e armazene na variável `estatisticas`.
- Crie o campo `Preco` com esse cálculo em relação aos campos: `Reais` + (`Centavos`/100). O novo campo deve ser criado no mesmo DataFrame `df`.
- Remova os seguintes campos: ['Reais', 'Centavos', 'Condicao', 'Condicao_Atual']. A remoção deve ser feita no mesmo DataFrame `df`.

# Preparação de dados 2
Continuando o exercício anterior, seu código deve conter as ações abaixo. Todos os campos devem ser criados no mesmo DataFrame `df`:

- Crie o campo `Nota_MinMax` com a transformação do campo `Nota` para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
- Crie o campo `N_Avaliações_MinMax` com a transformação do campo `N_Avaliações` para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
- Crie o campo `Desconto_MinMax` com a transformação do campo `Desconto` para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
- Crie o campo `Preco_MinMax` com a transformação do campo `Preco` para numérico em uma escala de 0 a 1, utilizando o MinMaxScaler.
- Crie o campo `Marca_Cod` utilizando o método LabelEncoder para transformar o campo `Marca` em numérico.
- Crie o campo `Material_Cod` utilizando o método LabelEncoder para transformar o campo `Material` em numérico.
- Crie o campo `Temporada_Cod` utilizando o método LabelEncoder para transformar o campo `Temporada` em numérico.

# Preparação de dados 3
Vamos finalizar o exercício com mais algumas preparações. Siga os passos a seguir. Todos campos devem ser criado no mesmo DataFrame `df`:

- Crie o campo `Qtd_Vendidos_Cod` com a transformação do campo `Qtd_Vendidos` para número de acordo com as suas grandezas ('Nenhum', '1', '2', '3', '4', '+5', '+25', '+50', '+100', '+1000', '+10mil' '+50mil'), exemplo +10mil = 10000.
- Crie o campo `Marca_Freq` com a transformação do campo `Marca` para número de acordo com a frequência do valor.
- Crie o campo `Material_Freq` com a transformação do campo `Material` para número de acordo com a frequência do valor.

