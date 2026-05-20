import requests
from bs4 import BeautifulSoup

url = 'https://python.org.br/web/'
requisicao = requests.get(url)


def extrair():
    extracao = BeautifulSoup(requisicao.content, 'html.parser')
    #print(extracao.text.strip()) # .text.strip() - Pega somente o texto dentro da tag e remove os espaços em branco
    return extracao


# Filtrar a exibição pela tag
def filtro():
    extracao = extrair()  #Atribuindo a funcao anterior a uma nova variável
    for linha_texto in extracao.find_all('h2'): #find.all - Procura as tags que vocë especificar
        titulo = linha_texto.text.strip()
        print('Título: ', titulo)


# Contar Títulos e Parágrafos
def filtro2():
    extracao = extrair()  #Atribuindo a funcao anterior a uma nova variável
    contador1 = 0
    contador2 = 0

    for linha_texto in extracao.find_all(['h2', 'p']):
        if linha_texto.name == 'h2':
            contador1 += 1
        elif linha_texto.name == 'p':
            contador2 += 1
    print('Total de Títulos: ', contador1, '///', 'Total de Parágrafos: ', contador2)


# Mostrar Títulos e Parágrafos
def texto():
    extracao = extrair()
    for linha_texto in extracao.find_all(['h2', 'p']):
        if linha_texto.name == 'h2':
            titulo = linha_texto.text.strip()
            print('Título: ', titulo)
        elif linha_texto.name == 'p':
            paragrafo = linha_texto.text.strip()
            print('Paragrafo: ', paragrafo)


# Extraindo Links da Web
def links():
    extracao = extrair()
    for titulo in extracao.find_all('h2'):
        print('\n Título: ', titulo.text.strip())
        for link in titulo.find_next_siblings('p'): #titulo.find_next_siblings - É usado para identificar links
            for a in link.find_all('a', href=True):
                print('Texto Link: ', a.text.strip(), ' | URL: ', a['href'])


if __name__ == '__main__':
    links()
