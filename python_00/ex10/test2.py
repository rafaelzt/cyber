#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python

from time import sleep


def ft_progress(lst):
	for elem in lst:
		print("\rETA: {eta:>3.2f}s [{prog_perc:>3.0f}%][{bar}] {current:5}/{end:5} | elapsed time {time:2.2f}s".format(
			eta=3.4, 
			prog_perc= ((elem / len(lst)) * 100) + 1,
			bar = "="*42,
			current= elem + 1, 
			end=len(lst), 
			time=1.33
			), end="")
		yield elem


if __name__ == "__main__":
	listy = range(100)
	ret = 0
	for el in ft_progress(listy):
		# print(el)
		ret += (el + 3) % 5
		sleep(0.01)
	print("\n...")
	print(ret)

