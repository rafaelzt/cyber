# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exec.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/11 14:17:15 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/11 17:11:30 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

invert_arguments = sys.argv[:0:-1]
for argument in invert_arguments:
    print(argument[::-1].swapcase(), end=" ")
print()
