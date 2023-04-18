# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 17:23:49 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/18 10:53:20 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def ft_remove_punct(word):
    punctuation = "!#$%&'()\"*+,-./:;<=>?@[\\]^_`{|}~"
    word = (''.join(['' if letter in punctuation else letter for letter in word]))
    return(word)

def ft_check_size(phrase, length):
    # print("phrase = {} | size = {}".format(phrase, length))
    lst = []
    for word in phrase.strip().split(" "):
        if len(word) > length:
            # print("Appended: {}".format(word))
            lst.append(word)
        else:
            # print("Not appended: {}".format(word))
            continue
    return (lst)

def ft_filterwords(*arguments):
    lst = arguments[0]
    # print("from ft_fiterwords: {}".format(lst))
    if (len(lst) == 3):
        _, word, length = lst
        try:
            length = int(length)
            #print(type(length))
        except:
            print("Error: Second parameter must be a integer")
            return
        if not(isinstance(word, str)):
            print("Error: First parameter must be a string!")
        #print(type(word))
        word = ft_remove_punct(word)
        word = "".join(word)
        print(ft_check_size(word, length))
        
    else:
        print("Error: Unexpected number of arguments received!")

if __name__ == "__main__":
    # print("from main: {}".format(sys.argv))
    ft_filterwords(sys.argv)
