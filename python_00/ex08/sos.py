#  **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 11:01:17 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/13 11:01:18 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
			'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
			'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
			'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--','X':'-..-',
			'Y':'-.--', 'Z':'--..', ' ' : '/', '1':'.----', '2':'..---', 
			'3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', 
			'8':'---..', '9':'----.', '0':'-----'}

arguments = [letter.upper() for letter in sys.argv[1:]]

try:
    for word in arguments:
        for letter in word:
            print(morse_dict[letter], end=" ")
        if not (word == arguments[len(arguments) - 1]):
            print("/", end=" ")
except:
    print("Some of the letters you enter can't be converted!")
print("")
