# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:23:49 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/16 22:19:39 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_filterwords(*arguments):
	lst = arguments
	try:
		_, word, length = lst[0]
		try:
			length = int(length)
			print(length)
		except:
			print("Error: Second parameter must be a integer")
		if not(isinstance(word, str)):
			print("Error: First parameter must be a string!")



	except:
		print("Error: Unexpected number of arguments received!")

if __name__ == "__main__":
	ft_filterwords(sys.argv)