# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_arachnida.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 15:06:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/20 12:46:20 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse
import os
import re
import requests
import sys
import urllib3

from bs4 import BeautifulSoup
from urllib.parse import urlparse


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


def ft_get_content(url, method = 'GET'):
    http = urllib3.PoolManager()
    try:
        content = http.request(method, 
                                url, 
                                preload_content=False,
                                retries=3,
                                timeout=5.0,
        )
    except:
        print("Nothing to see here! URL not reachable!")
        exit(1)
    return(content.data)


def ft_warmup_my_soup(content):
    soup = BeautifulSoup(content, 'html.parser')
    return (soup)


def ft_extract_tags_from_soup(soup, dict_tags):
    links = []
    for link in (soup.findAll(dict_tags.keys())):
        for _, value in dict_tags.items():
            links.append(link.get((''.join(value))))
    return (links)


def ft_create_multi_level_lst(url, iteration = 0):
    pass

def ft_get_all_images(url_lst, path):
    for image in url_lst[0]:
        try:
            filename = image.rsplit('/', 1)[1]
            r = requests.get(image, stream=True)
            with open(path + '/' + filename, 'wb+') as file:
                    file.write(r.content)
        except:
            continue

if __name__ == "__main__":
    url = "https://42madrid.com"
    iteration = 0
    
    if iteration == 0:
        lst_items.append(ft_extract_tags_from_soup(ft_warmup_my_soup(ft_get_content(url)), dict_tag_images))
    else:
        print("Nothing!")
    ft_get_all_images(lst_items, "./data/")