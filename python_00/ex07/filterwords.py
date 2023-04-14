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
	punctuation = "!#$%&'()\"*+,-./:;<=>?@[\\]^_`{|}~"
	return(''.join([' ' if char in punctuation else char for char in string])) # List comprehention
	# For each char in string test if char is in punctuation and if true change to <space> else keep char


def ft_filter(string, number):
	new_string = string.strip().split()
	new_list = []
	# new_list = [i if (len(i) > number) for i in new_string]

	for i in new_string:
		if (len(i) > number):
			new_list.append(i)

	print(new_list)

if __name__ == "__main__":
	string = sys.argv[1]
	number = None

	if not (isinstance(string, str)):
		print("ERROR")
	
	if (not (isinstance(int(sys.argv[2]), int))):
		print("ERROR")
	number = int(sys.argv[2])

	string = ft_remove_punctuation(string)
	ft_filter(string, number)
