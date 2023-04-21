# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tests3.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/21 10:26:09 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/21 10:43:29 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [a.attrs.get('href') for a in soup.select('a[href]')]
    return urls


def download_image(url, folder='downloaded_images'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url, stream=True)
    file_name = os.path.join(folder, url.split('/')[-1])

    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded {url}")


def main(url, depth):
    if not is_valid_url(url):
        print("Invalid URL")
        return

    visited_urls = set()
    img_urls = set()
    urls_to_visit = [(url, 0)]

    while urls_to_visit:
        current_url, current_depth = urls_to_visit.pop()

        if current_url in visited_urls or current_depth > depth:
            continue

        visited_urls.add(current_url)

        try:
            response = requests.get(current_url)
        except requests.exceptions.RequestException:
            continue

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        for img in soup.find_all('img', src=True):
            img_url = img['src']
            img_url = urljoin(current_url, img_url)

            if img_url not in img_urls:
                download_image(img_url)
                img_urls.add(img_url)

        sub_links = get_all_links(current_url)
        for link in sub_links:
            link = urljoin(current_url, link)
            if is_valid_url(link) and link not in visited_urls:
                urls_to_visit.append((link, current_depth + 1))

    print(f"Downloaded {len(img_urls)} images.")


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <DEPTH>")
        sys.exit(1)

    url = sys.argv[1]
    depth = int(sys.argv[2])

    main(url, depth)