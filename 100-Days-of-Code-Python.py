# print("Welcome to the tip calculator!")
# total_amount = int(input("What was the total amount? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people =  int(input("How many poeple to split the bill?"))

# compute = round(((total_amount + total_amount * (tip/100))/people), 2)

# print(f"Each person should pay: ${compute}")

# Second problem 
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# # Pizza amount
# pizza_options = ['s','m', 'l']

# if size.lower() in pizza_options:
#     if size.lower() == pizza_options[0]:
#         pizza_amount = 15
#     elif size.lower() == pizza_options[1]:
#         pizza_amount = 20
#     elif size.lower() == pizza_options[2]:
#         pizza_amount = 25
# else:
#     pizza_amount = 0

# # Adding Pepperoni
# pepperoni_options = ['y', 'n']

# if pepperoni.lower() in pepperoni_options:
#     if pepperoni.lower() == pepperoni_options[0]:
#         pizza_amount += 2

# #adding extra cheese
# cheese_options = ['y', 'n']

# if extra_cheese.lower() in cheese_options:
#     if extra_cheese.lower() == cheese_options[0]:
#         pizza_amount += 1

# print(f"Total amount {pizza_amount}")


# print("Welcome to Treasure Island. Your mission is to find the treasure.")
# step_one = input("Do you want to go: left or right?")
# if step_one.lower() == 'right':
#     print('Game over')
# else:
#     step_two = input('Do you want to swim or wait?')
#     if step_two.lower() == 'swim':
#         print('Game over')
#     else:
#         step_three =  input('Which door would you like to use: red, yellow or blue?')
#         if step_three.lower() in ['red', 'blue']:
#             print('Game over')
#         elif step_three.lower() == 'yellow':
#             print('You Win')

#working with a random module

# import random

# random_integer = random.randint(0,1)
# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")


# friends = ["Alice", "Bob", "Charles", "David", "Emanuel"]

# random_number = random.randint(0, len(friends))

# print(friends[random_number])


# rand_list = [-4,90,200,1,-3,10,15,10000,2000,500]

# max_number = 0

# for item in rand_list:
#     if item > max_number:
#         max_number = item 

# print("James", max_number)

#Capiltal letter number [65,90], small letter [97,122] number[48,57] special character [33, 46]  use char = chr(ascii_value)

import random

print("Welcome to the password generator")
number_of_password = int(input("How many letters would you like in your password? "))
number_of_symbol =  int(input("How many Symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

if numbers + number_of_symbol <= number_of_password:
    #Random symbols
    list_of_symbols = []
    for index in range(0,number_of_symbol):
        rand_number = random.randint(33,46)
        char = chr(rand_number)
        list_of_symbols.append(char)

    #Random numbers
    list_of_numbers = []
    for index in range(0,numbers):
        rand_number = random.randint(48,57)
        char = chr(rand_number)
        list_of_numbers.append(char)

    number_of_letters = number_of_password - (numbers + number_of_symbol)
    letters = []

    for index in range(0, number_of_letters):
        random_cap_low =  random.randint(0, 1)

        if random_cap_low == 1:
            #Capitals [65,90]
            rand_number = random.randint(65, 90)
            char = chr(rand_number)
            letters.append(char)
        else:
            #lower case [97,122]
            rand_number = random.randint(97, 122)
            char = chr(rand_number)
            letters.append(char)

    total_list = list_of_symbols + list_of_numbers + letters

    random.shuffle(total_list)
    print(total_list)

