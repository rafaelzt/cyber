#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:23:49 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/12 17:28:04 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def ft_remove_punctuation(string):
	punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
	return(''.join([' ' if char in punctuation else char for char in string])) # List comprehention
	# For each char in string test if char is in punctuation and if true change to <space> else keep char


def ft_filter(string, number):
	new_string = string.strip().split()
	new_list = []

	for i in new_string:
		if (len(i) > number):
			new_list.append(i)

	print(new_list)

if __name__ == "__main__":
	new_string = ft_remove_punctuation("Hel!lo, my friend")
	number = 2
	print(new_string)
	print(number)
	ft_filter(new_string, number)
