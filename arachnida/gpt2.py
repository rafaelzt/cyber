import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

def download_images(url):
    # Faz a solicitação HTTP para a URL fornecida
    response = requests.get(url)

    # Analisa o HTML da página usando a biblioteca beautifulsoup4
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todas as tags de imagem na página
    img_tags = soup.find_all('img')

    # Cria um diretório para salvar as imagens
    directory = os.path.join(os.getcwd(), 'images')
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Loop através de todas as tags de imagem e baixa cada imagem
    for img in img_tags:
        try:
            # Faz a solicitação HTTP para a URL da imagem
            img_url = img['src']
            if not img_url.startswith('http'):
                img_url = url + img_url
            img_response = requests.get(img_url)

            # Cria uma imagem a partir do conteúdo da resposta HTTP
            img_data = BytesIO(img_response.content)
            img_file = Image.open(img_data)

            # Salva a imagem em disco
            filename = os.path.join(directory, os.path.basename(img_url))
            img_file.save(filename)
            print(f"Imagem baixada: {filename}")

        except Exception as e:
            print(f"Erro ao baixar a imagem: {e}")


def collect_urls(url, urls=[]):
    # Faz a solicitação HTTP para a URL fornecida
    response = requests.get(url)

    # Analisa o HTML da página usando a biblioteca beautifulsoup4
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todas as tags de âncora na página
    a_tags = soup.find_all('a')

    # Loop através de todas as tags de âncora e coleta cada URL
    for a in a_tags:
        try:
            # Extrai a URL do atributo href da tag âncora
            href = a['href']

            # Se a URL não começar com 'http', adiciona a URL base à frente da URL
            if not href.startswith('http'):
                href = url + href

            # Adiciona a URL à lista de URLs
            if href not in urls:
                urls.append(href)
                print(f"URL coletada: {href}")

                # Visita a URL e coleta todas as URLs na página
                collect_urls(href, urls)

        except Exception as e:
            print(f"Erro ao coletar a URL: {e}")

    return urls

if __name__ == "__main__":
    download_images("https://42madrid.com")