#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/13 12:37:19 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/13 12:37:20 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def header():
	print("This is an interactive guessing game!")
	print("You have to enter a number between 1 and 99 to find out the secret number.")
	print("Type 'exit' to end the game")
	print("Good luck!")

if __name__ == "__main__":
	header()
	secret = random.randint(0,99)
	secret = 42
	count = 1

	while (True):
		user_input = input("What's your guess between 1 and 99?\n>> ")
		if (user_input == "exit"):
			break
		try:
			user_input = int(user_input)
			if (user_input > secret):
				print("Too high!")
			elif (user_input < secret):
				print("Too low!")
			elif (user_input == secret) and (count == 1):
				if (secret == 42):
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				print("Congratulations! You got it on your first try!")
				break
			else:
				if (secret == 42):
					print("The answer to the ultimate question of life, the universe and everything is 42.")
				print("Congratulation, you've got it!")
				print("You won in {} attempts!".format(count))
				break
		except:
			print("That's not a number.")
		count += 1