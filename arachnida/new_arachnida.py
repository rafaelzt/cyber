# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_arachnida.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 15:06:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/19 21:50:48 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse
import os
import re
import sys
import urllib3


from bs4 import BeautifulSoup
from urllib.parse import urlparse


lst_items = []
num_calls = 0

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


def ft_extract_link_from_soup(soup):
    links = []
    for link in (soup.findAll('a', attrs={'href': re.compile("^https?://")})):
        links.append(link.get('href'))
    return (links)


def ft_create_url_lst(scrape_lst, original_url):
	pass


def ft_create_multi_level_lst(url, iteration = 0):
    
    if (num_calls == iteration):
        return (lst_items)
    
	lst_items.append(ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(url))))
    
    return (lst_items)


if __name__ == "__main__":
    ft_create_multi_level_lst("https://42madrid.com", 2)
    print(lst_items)