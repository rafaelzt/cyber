# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_arachnida.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 15:06:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/21 10:42:00 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse
import os
import requests
import sys

from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


lst_items = []
lst_image_types = ["jpeg", "jpg", "gif", "bmp", "png"]
dict_tag_images = {
                "img": ["src"],
                "images": ["src"]
                }
dict_tag_links = {"a": ["href"]}


def ft_parse_arguments(*arg):
    parser = argparse.ArgumentParser(
            prog=sys.argv[0],
            description="Webscrape an URL and download specific file type",
            epilog="And magic is done!",
            )

    # Positional Arguments
    parser.add_argument("url",
                        help="Specify URL to scrape",
            )

    # Optional Arguments
    parser.add_argument("-r", "--recursive",
                        dest="recursive",
                        action="store_true",
                        help="If present, recursively download files",
            )
    parser.add_argument("-l", "--length",
                        dest="depth",
                        metavar="[N]",
                        default=5,
                        type=int,
                        help="URL max depth to search for files",
            )
    parser.add_argument("-p", "--path",
                        dest="path",
                        metavar="[PATH]",
                        default="./data",
                        type=str,
                        help="Specify path where files will be downloaded",
                        )

    args = parser.parse_args()
    return (args)


def ft_check_url(url):
    parser = urlparse(url)
    return bool(parser.netloc) and bool(parser.scheme)


def ft_get_all_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    urls = [a.attrs.get('href') for a in soup.select('a[href]')]
    return urls


def ft_warmup_my_soup(content):
    soup = BeautifulSoup(content, 'html.parser')
    return (soup)


def download_image(url, folder='data'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    response = requests.get(url, stream=True)
    file_name = os.path.join(folder, url.split('/')[-1])

    with open(file_name, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"Downloaded {url}")

def ft_download_content(url, depth=0):
    if not ft_check_url(url):
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

        sub_links = ft_get_all_links(current_url)
        for link in sub_links:
            link = urljoin(current_url, link)
            if ft_check_url(link) and link not in visited_urls:
                urls_to_visit.append((link, current_depth + 1))

    print(f"Downloaded {len(img_urls)} images.")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python new_arachnida.py <URL> <DEPTH>")
        sys.exit(1)

    url = sys.argv[1]
    depth = int(sys.argv[2])

    ft_download_content(url, depth)
