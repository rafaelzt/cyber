# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:17:15 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/11 14:34:20 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if __name__ == '__main__':
    arguments = sys.argv[1:]
    size = len(arguments)
    count = 0

    while (count < size):
        print(arguments[count])

