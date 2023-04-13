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

import time

def draw_bar():
	start = 0
	end = 50
	step = 1
	i = 0

	for i in 
	print("\rETA: {eta:>3.2f}s [{prog_perc:>3}%][".format(eta=3.4, prog_perc=20.34), end="")
	# [{done:=<test1}{tbd:<test2}
	print("="*i + ">", end="")
	print(" "*(end - i), end="")
	print("] {current:5}/{end:5} | elapsed time {time:2.2f}s".format(current=1000, end=10000, time=1.33	))

	i = 20

	print("\rETA: {eta:>3.2f}s [{prog_perc:>3}%][".format(eta=3.4, prog_perc=20.34), end="")
	# [{done:=<test1}{tbd:<test2}
	print("="*i + ">", end="")
	print(" "*(end - i), end="")
	print("] {current:5}/{end:5} | elapsed time {time:2.2f}s".format(current=1000, end=10000, time=1.33	))


if __name__ == "__main__":
	draw_bar()