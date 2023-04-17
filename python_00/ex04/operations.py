# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 11:45:57 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/17 10:56:06 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# TODO: Format periodic tithe (adding ... at the end)

import sys

def sum(x, y):
	print(f"Sum:\t\t\t\t{x + y}")

def diff(x, y):
	print(f"Difference:\t\t\t{x - y}")

def mult(x, y):
	print(f"Product:\t\t\t{x * y}")

def quot(x, y):
	if (y == 0):
		print("Quotient:\t\t\tERROR (division by zero)")
	else:
		print(f"Quotient:\t\t\t{x / y:.5}")

def remain(x, y):
	if (y == 0):
		print("Remainder:\t\t\tERROR (modulo by zero)")
	else:
		print(f"Remainder:\t\t\t{x % y}")

def calculate(num_1:int, num_2:int):
	"""
Usage: python operations.py <number1> <number2>
Example:
	python operations.py 10 3
	"""

	sum(num_1, num_2)
	diff(num_1, num_2)
	mult(num_1, num_2)
	quot(num_1, num_2)
	remain(num_1, num_2)


if __name__ == "__main__":
		if (len(sys.argv) == 1):
			print(calculate.__doc__)
		elif (len(sys.argv) == 2):
			print("AssertionError: few arguments")
		elif (len(sys.argv) > 3):
			print("AssertionError: too many arguments")
		else:
			try:
				num_1 = int(''.join(sys.argv[1:2]))
				num_2 = int(''.join(sys.argv[2:3]))

				if (isinstance(num_1, int) and isinstance(num_2, int)):
					calculate(num_1,num_2)
			except ValueError as ve:
				print("AssertionError: only integers")




