# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 12:59:44 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/12 13:02:26 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = (19, 20, 25)


# print("The {} numbers are: ".format(len(kata)), end="")
# if (len(kata) == 1):
# 	print("{}".format(kata[len(kata) - 1]))
# else:
# 	for i in range(len(kata) - 1):
# 		print("{}".format(kata[i]), end=", ")
# 	print("{}".format(kata[len(kata) - 1]))

print("The {} numbers are: ".format(len(kata)), end="")
print(*kata, sep=', ')

# print(type(kata))

# print(f"The {len(kata)} numbers are: {kata[0]}, {kata[1]}, {kata[2]}")
# print("The {} numbers are: {}, {}, {}".format(kata[0], kata[1], kata[2]))
# print("The {length} numbers are: {num_1}, {num_2}, {num_3}".format(num_1 = kata[0], 
# 															num_2 = kata[1], 
# 															num_3 = kata[2]))
