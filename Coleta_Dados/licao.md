# Coleta Dados 1
Vamos iniciar o nosso projeto de extração e manipulação de dados, utilizando inicialmente os dados do e-commerce books.toscrape.com. Este é um site para fins educativos para realizar web scraping de uma página fictícia de livraria. Vamos utilizar este site pois, se utilizássemos sites de e-commerce, poderíamos ser vistos como robôs que querem tentar invadir ou derrubar o site, afinal, muitos alunos acessariam o mesmo site e realizariam consultas.

Para este primeiro exercício faça o seguinte:

- Mostre os primeiros 2000 caracteres do site https://books.toscrape.com/
- Armazene a requisição na variável `requisicao`.
- Use o `print` com a `requisição` para chegar no resultado. Utilize também a função `prettify()`.

# Coleta Dados 2
Agora mostre o título e o preço dos livros da primeira página do site https://books.toscrape.com/, para fazer isso é necessário seguir os passos abaixo:

Parte 1
- Crie um `for` para encontrar a tag `<h3>` dentro da tag `<article>`.
- Extraia os textos da tag `<h3>` e armazene na variável `titulo`. Essa variável depois deve ser utilizada para atualizar o valor de `livro['Título']`.
- Crie outro `for` para encontrar a tag `<p class=’’price_color’>` com o `findall('p', class='price_color')`, dentro da tag `<h3>`.
- Extraia os textos da tag `<p>` e armazene na variável `preco`. Essa variável depois deve ser utilizada para atualizar o valor de `livro['Preço']`.
- Atente para a nomenclatura correta das variáveis e das chaves do dicionário. Os livros devem ser adicionados na lista `catalogo`, conforme o código padrão.

Parte 2

Calcule a quantidade de livros da primeira página do site https://books.toscrape.com/:

- Você pode utilizar a mesma estrutura de `for` loop feita na parte 1.
- Armazene a quantidade de livros na variável `contar_livros`.
- Imprima a variável `contar_livros`.
