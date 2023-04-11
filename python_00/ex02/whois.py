# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:12:29 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/11 17:20:07 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

argument = sys.argv[1:]

if len(argument) != 1:
	print("AssertionError: more than one argument are provided")
	exit()
	
try:
	value = int(''.join(argument))
	if value == 0:
		print("I'm Zero.")
	elif value % 2 == 0:
		print("I'm Even.")
	elif value % 2 != 0:
		print("I'm Odd.")
except ValueError:
	print("AssertionError: argument is not a integer")

