# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:59:46 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/17 10:55:53 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata02.py file
kata = (2019, 9, 25, 3, 30)

print("{month:02}/{day:02}/{year:04} {hour:02}:{min:02}".format(
															year=kata[0],
															month=kata[1],
															day=kata[2],
															hour=kata[3],
															min=kata[4],
															))
