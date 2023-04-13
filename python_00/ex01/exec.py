#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python
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

new_list = []
arguments = (sys.argv[1:][::-1]) # reverse the list
for argument in arguments: # iterate over the list
    new_list.append(argument[::-1]) # reverse each word

print(' '.join(new_list)) # join the list with a space