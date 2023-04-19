import os
import requests
from bs4 import BeautifulSoup


def download_images_from_url(url, output_dir):
    # Recupera o conteúdo da página
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todos os links na página
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):
            links.append(href)

    # Recupera todas as imagens nas páginas
    images = []
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src')
            if src and src.startswith('http'):
                images.append(src)

    # Cria o diretório de saída, se ainda não existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Baixa as imagens e salva no diretório de saída
    for i, image in enumerate(images):
        response = requests.get(image)
        filename = os.path.join(output_dir, f'image_{i}.jpg')
        with open(filename, 'wb') as f:
            f.write(response.content)


download_images_from_url('https://www.42madrid.com', 'images')