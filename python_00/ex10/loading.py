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

from time import sleep


def draw_bar(current, end):
	return (f"{'='*current}{'>'}{' '*(end - current)}")

def ft_progress(end):
	for i in range(end):
		print("\rETA: {eta:>3.2f}s [{prog_perc:>3}%][{bar}] {current:5}/{end:5} | elapsed time {time:2.2f}s".format(
			eta=3.4, 
			prog_perc=20.34,
			bar = draw_bar(i, end),
			current=i + 1, 
			end=end, 
			time=1.33
			), end="")
		sleep(0.01)

if __name__ == "__main__":
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		sleep(0.01)
	print()
	print(ret)

