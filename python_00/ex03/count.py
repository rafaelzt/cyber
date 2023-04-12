# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 17:23:21 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/12 11:32:24 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

punctuation = [',', '.', ':', ';', '!', '?', '"'
                , "'", '-', '(', ')', '[', ']', '{', '}']

try:
    # print("Before function")
    # print(sys.argv)
    def text_analyzer(argument = sys.argv):
        '''
        This function counts the number of upper characters, lower characters,
        punctuation and spaces in a given text.
        '''
        punct = 0
        upper = 0
        lower = 0
        space = 0

        # print(argument)

        if (len(argument) > 2):
            print("You should enter only one argument.")
        elif len(argument) == 1:
            print("What is the text to analyse?")
            argument = input()
        else:
            argument = ''.join(argument[1:])

        if not(isinstance(argument, str)):
            print("The argument is not a string.")
            return

        for letter in argument:
            if letter.isupper():
                upper += 1
            elif letter.islower():
                lower += 1
            elif letter.isspace():
                space += 1
            elif letter in punctuation:
                punct += 1
            
        print("The text contains", len(argument), "character(s):")
        print("-", upper, "upper letter(s)")
        print("-", lower, "lower letter(s)")
        print("-", punct, "punctuation mark(s)")
        print("-", space, "space(s)")
        # print(sys.argv) No exist
        print(argument)
except TypeError as te:
    print("You should enter only one argument.")


        
    
if __name__ == "__main__":
    # print(len(sys.argv))
    text_analyzer(''.join(sys.argv[1:]))
