# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    new_arachnida.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/18 15:06:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/18 17:53:25 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import argparse
import exifread
import sys
import os
import re
from requests.models import HTTPError
import urllib3

from bs4 import BeautifulSoup


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
    for link in (soup.findAll('a', attrs={'href': re.compile("^https://")})):
        links.append(link.get('href'))
    return (links)


def iterate_list(lst):
    # base case: if the list is empty, return
    if len(lst) == 0:
       return
    
    # recursive case: iterate into the first element of the list
    print(lst[-1])
    iterate_list(lst[:-1])

if __name__ == "__main__":
    #arguments = ft_parse_arguments(sys.argv)
    #print("Program: \t\t{} \t type: {}".format(sys.argv[0], type(sys.argv[0])))
    #print("URL: \t\t\t{} \t\t type: {}".format(arguments.url, type(arguments.url)))
    #print("Recursive Flag: \t{} \t\t\t type: {}".format(arguments.recursive, type(arguments.recursive)))
    #print("Depth: \t\t\t{} \t\t\t type: {}".format(arguments.depth, type(arguments.depth)))
    #print("Path: \t\t\t{} \t\t\t type: {}".format(arguments.path, type(arguments.path)))

    iterate_list(range(5))
    #my_list = [1,2,3,4,5]
    #print(my_list)
    #print(my_list[::-1])

    nivel_0 = (ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content("https://42madrid.com"))))
    print(nivel_0)
    nivel_0_1 = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(nivel_0[0])))
    print(nivel_0_1)
    nivel_0_2 = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(nivel_0[1])))
    print(nivel_0_2)
    nivel_0_3 = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(nivel_0[2])))
    print(nivel_0_3)
    nivel_0_4 = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(nivel_0[3])))
    print(nivel_0_4)
    nivel_0_5 = ft_extract_link_from_soup(ft_warmup_my_soup(ft_get_content(nivel_0[4])))
    print(nivel_0_5)
