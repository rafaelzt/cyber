#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:59:35 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/12 12:59:51 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

print("module_{module:02}, ex_{ex:02} : {num1:.2f} {sci1:.2e} {sci2:.2e}".format(module=kata[0],
				ex=kata[1],
				num1=kata[2],
				sci1=kata[3],
				sci2=kata[4]
))