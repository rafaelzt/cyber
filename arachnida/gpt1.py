# -*- coding: utf-8 -*-

import os
import requests
import unicodedata
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.request import urlretrieve


def download_images_from_url(url):
    # cria um diretório para armazenar as imagens
    base_dir = 'images'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # coleta todas as urls contidas na url pai e nos seus subniveis
    urls = set()
    visited_urls = set()
    urls.add(url)
    while urls:
        current_url = urls.pop()
        visited_urls.add(current_url)
        try:
            response = requests.get(current_url)
        except requests.exceptions.RequestException:
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                # converte a url relativa para a url absoluta
                href = urljoin(current_url, href)
                # adiciona a url à lista, se ela ainda não tiver sido visitada
                if href not in visited_urls:
                    urls.add(href)

        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                # converte a url relativa para a url absoluta
                src = urljoin(current_url, src)
                # baixa a imagem
                filename = os.path.join(base_dir, os.path.basename(urlparse(src).path))
                urlretrieve(src, filename)

if __name__ == "__main__":
	download_images_from_url('https://www.42madrid.com/')