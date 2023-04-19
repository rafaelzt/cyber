# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 12:45:24 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/19 22:10:29 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import os

import requests
from bs4 import BeautifulSoup


# print("Status code: {}\n".format(r.status_code))
# print("Header: {}\n".format(r.headers))
# print("Encoding: {}\n".format(r.encoding))
# print("Text: {}\n".format(r.text))
# print("Json: {}\n".format(r.json))

def ft_get_all_links(domain) -> list:
    r = requests.get(domain)
    page_source = r.text
    soup = BeautifulSoup(page_source, 'html.parser')
    # print(soup.prettify())

    full_domain_lst = []

    # Search all <a> tags
    for link in soup.find_all('a'):
        links = link.get('href')
        if (domain in links) and not(domain in full_domain_lst):
            full_domain_lst.append(links)
        else:
            continue

    full_domain_lst = list(dict.fromkeys(full_domain_lst)) # Remove duplicated URLs
#    for link in full_domain_lst:
#        ft_get_all_links(link)
    return(full_domain_lst)

def ft_get_all_images(url_lst, path):
    i = 0
    for url in url_lst:
        r = requests.get(url)
        page_source = r.text
        soup = BeautifulSoup(page_source, 'html.parser')
        for image in soup.find_all('img'):
            try:
                img_url = image.get('src')
                filename = img_url.rsplit('/', 1)[1]
                # print("URL: {} -> {}".format(img_url, filename))
                r = requests.get(img_url, stream=True)
                # with open(path + filename, 'wb') as file:
                # 	for chunk in r.iter_content(chunk_size=1024):
                # 		file.write(chunk)
                with open(path + '/' + filename, 'wb+') as file:
                        file.write(r.content)
                
    # with open(file_name, 'wb') as f:
    #     for chunk in r.iter_content(chunk_size=1024):
    #         if chunk: # filter out keep-alive new chunks
    #             f.write(chunk)

                
            except:
                continue

# Search all <img> tags
# for link in soup.find_all('img'):
#     print("Images: {images}".format(images = link.get('src')))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Webscrap an URL and download images')
    # Positional arguments
    parser.add_argument("url", 
                        help='Specify URL to scrap')
    # Optional arguments
    parser.add_argument("-r", "--recursive", dest='r',
                        help='Recursivly download images', action='store_true')
    parser.add_argument("-l", "--length", metavar='[N]', dest='l',
                        help='Depth you want to scrap', default=5)
    parser.add_argument("-p", "--path", metavar='[PATH]', dest="p", 
                        help='Specify were downloaded images should be saved', default='./data/')

    args = parser.parse_args()
    print(args.r)
    print(args.l)
    try:
        os.mkdir(args.p)
    except FileExistsError as fe:
        print("WARN:\n\tFolder already exist!\n\t{}".format(fe))
    links = ft_get_all_links(args.url)
    for item in links:
        print(item)
    # ft_get_all_images(links, args.p)
    
