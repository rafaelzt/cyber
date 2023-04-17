# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    spider.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/17 12:45:24 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/17 17:34:02 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import argparse
import os
import sys

import requests
from bs4 import BeautifulSoup

# print("Status code: {}\n".format(r.status_code))
# print("Header: {}\n".format(r.headers))
# print("Encoding: {}\n".format(r.encoding))
# print("Text: {}\n".format(r.text))
# print("Json: {}\n".format(r.json))

def ft_get_all_links(url) -> list:
	domain = "https://" + url
	r = requests.get(domain)
	page_source = r.text
	soup = BeautifulSoup(page_source, 'html.parser')
	# print(soup.prettify())

	full_domain_lst = []

	# Search all <a> tags
	for link in soup.find_all('a'):
		links = link.get('href')
		if (url in links):
			full_domain_lst.append(links)
		else:
			continue

	full_domain_lst = list(dict.fromkeys(full_domain_lst)) # Remove duplicated URLs
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
				with open(path + filename, 'wb') as file:
						file.write(r.content)
				
    # with open(file_name, 'wb') as f:
    #     for chunk in get_response.iter_content(chunk_size=1024):
    #         if chunk: # filter out keep-alive new chunks
    #             f.write(chunk)

				
			except:
				continue

# Search all <img> tags
# for link in soup.find_all('img'):
#     print("Images: {images}".format(images = link.get('src')))

if __name__ == "__main__":
	try:
		path = ("./" + sys.argv[2] + "/")
		os.mkdir(path)
	except FileExistsError as fe:
		print("WARN:\n\tFolder already exist!\n\t{}".format(fe))
	ft_get_all_images(ft_get_all_links(sys.argv[1]), path)
	