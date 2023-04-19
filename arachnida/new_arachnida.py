# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_arachnida.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 15:06:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/19 13:30:18 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse
# import exifread
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


def ft_recursive_list(scrape_lst, original_url):
    global lst_items
    domain = urlparse(original_url).netloc
    if len(scrape_lst) == 0: 
        return

    if (domain in scrape_lst[0]):
        #print("Domain: {} \t->\t Scrape: {}".format(domain, scrape_lst[0]))
        lst_items.append(scrape_lst[0])
        lst_items = list(dict.fromkeys(lst_items))

    ft_recursive_list(scrape_lst[1:], original_url)


def ft_create_multi_level_lst(lst_items, iteration = 0):
    global num_calls

    if not(num_calls >= iteration):
        for item in lst_items:
            print(item, num_calls)
            ft_create_multi_level_lst(lst_items[])
        num_calls += 1
    else:
        return


if __name__ == "__main__":
    #arguments = ft_parse_arguments(sys.argv)
    #print("Program: \t\t{} \t type: {}".format(sys.argv[0], type(sys.argv[0])))
    #print("URL: \t\t\t{} \t\t type: {}".format(arguments.url, type(arguments.url)))
    #print("Recursive Flag: \t{} \t\t\t type: {}".format(arguments.recursive, type(arguments.recursive)))
    #print("Depth: \t\t\t{} \t\t\t type: {}".format(arguments.depth, type(arguments.depth)))
    #print("Path: \t\t\t{} \t\t\t type: {}".format(arguments.path, type(arguments.path)))

    #iterate_list(range(5))
    #my_list = [1,2,3,4,5]
    #print(my_list)
    #print(my_list[::-1])

    url = "https://42madrid.com"
    domain = urlparse(url).netloc
    #print(ft_get_content(url))
    #print(ft_warmup_my_soup(ft_get_content(url)))
    lst = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(url)))
    ft_recursive_list(lst, url)
    # ft_create_multi_level_lst(url)
    # print(lst_items)

    ft_create_multi_level_lst(lst, 1)
