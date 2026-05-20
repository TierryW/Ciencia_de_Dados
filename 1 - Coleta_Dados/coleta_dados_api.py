import requests

from coleta_dados_web import requisicao, url


def enviar_arquivo():
    caminho = 'C:/Users/willi/Downloads/Arquivos/produtos_informatica.xlsx'

    # Enviar Arquivo
    requisicao = requests.post('https://upload.gofile.io/uploadFile', files={
        'file': open(caminho, 'rb')})  #Tipo do Arquivo, seu caminho e 'rb', significa read (leitura), e binário
    saida_requisicao = requisicao.json()

    print(saida_requisicao)  # Impressão dos atributos
    url = saida_requisicao['data']['downloadPage']  #Extração das informações através dos atributos que desejamos
    print("Arquivo enviado. Link para acesso:", url)


def receber_arquivo(file_url): # O parametro é o link para download do arquivo
    # Receber arquivo
    requisicoes = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
        print('Arquivo baixado com sucesso!')
    else:
        print("Erro ao baixar o arquivo!", requisicao.json())


if __name__ == '__main__':
    receber_arquivo('https://gofile.io/d/C40VhB')
