#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 12:37:11 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/13 12:37:11 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

lst = range(100)

for value, idx in (enumerate(lst, 0)): 
	# enumarate (create a tuple with list elements and give an index starting from second argument : 1)
	print(f"{idx} -> {value}")