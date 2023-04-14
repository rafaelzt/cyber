#!/goinfre/rzamolo-/miniconda3/envs/42AI-rzamolo-/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rzamolo- <rzamolo-@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/12 14:07:03 by rzamolo-          #+#    #+#              #
#    Updated: 2023/04/12 15:19:38 by rzamolo-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# TODO: Protect functions if received null // check meal time to be a integer (non-negative)

cookbook = {
	"sandwich":{
		"ingredients":["ham", "bread", "cheese", "tomatoes"],
		"meal":"lunch",
		"prep_time":10
	},
	"cake":{
		"ingredients":["flour", "sugar", "eggs"],
		"meal":"dessert",
		"prep_time": 60
	},
	"salad":{
		"ingredients":["avocado", "arugula", "tomatoes", "spinach"],
		"meal":"lunch",
		"prep_time": 15
	}
}

def print_cookbook():
	print("."*80)
	print("{:^80}".format("Recipes"))
	print("."*80)
	for recipe in (cookbook.keys()):
		print("{}".format(recipe))
	# print(*cookbook, sep="\n")

def print_details(rcp):
	print("\nRecipe for {}:".format(rcp))
	print("  Ingredients list:{}".format(str(cookbook[rcp]["ingredients"])))
	print("  To be eaten for {}.".format(str(cookbook[rcp]["meal"])))
	print("  Takes {} minutes of cooking.".format(str(cookbook[rcp]["prep_time"])))

def del_recipe(rcp):
	cookbook.pop(rcp)

def new_recipe():
	rcp_name = input("Enter a name:\n")

	rcp_ing_list = []
	rcp_ing = "ingredients"
	
	print("{}".format("Enter ingredients:"))
	while (rcp_ing != ''):
		rcp_ing = ""
		rcp_ing = input()
		rcp_ing_list.append(rcp_ing)

	rcp_meal = input("Enter a meal type:\n")
	try:
		rcp_prep_time = int(input("Enter a preparation time:\n"))
	except:
		print("ValueError: Not a integer")
		return

	cookbook[rcp_name] = {
		"ingredients": rcp_ing_list,
		"meal": rcp_meal,
		"prep_time": rcp_prep_time

	}

def menu():
	print("List of available option:")
	print("1: Add a recipe")
	print("2: Delete a recipe")
	print("3: Print a recipe")
	print("4: Print the cookbook")
	print("5: Quit")

	option = input("\nPlease select an option:\n>> ")

	if (option == "1"):
		msg = ""
		print("{}".format(msg))
		new_recipe()
	elif (option == "2"):
		msg = "Please enter a recipe name to delete it:"
		print("{}".format(msg))
		del_recipe(input(">> "))
	elif (option == "3"):
		msg = "Please enter a recipe name to get its details:"
		print("{}".format(msg))
		print_details(input(">> "))
	elif (option == "4"):
		msg = "This are the recipes in the cookbook."
		print("{}".format(msg))
		print_cookbook()
	elif (option == "5"):
		msg = "Cookbook closed. Goodbye !"
		print("{}".format(msg))
		return
	else:
		print("{}".format("Sorry, this option does not exist."))

	menu()


if __name__ == "__main__":
	print("Welcome to the Python Cookbook !")
	menu()