import requests
from bs4 import BeautifulSoup
import pandas

response = requests.get('https://www.precisaofinanceira.com.br/tabelas/selic')
#print(response.text[:600])
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:600])

print('Pandas:')
url_dados = pandas.read_html('https://www.precisaofinanceira.com.br/tabelas/selic')
print(url_dados[0].head(12))
