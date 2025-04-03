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

# import random

# print("Welcome to the password generator")
# number_of_password = int(input("How many letters would you like in your password? "))
# number_of_symbol =  int(input("How many Symbols would you like? "))
# numbers = int(input("How many numbers would you like? "))

# if numbers + number_of_symbol <= number_of_password:
#     #Random symbols
#     list_of_symbols = []
#     for index in range(0,number_of_symbol):
#         rand_number = random.randint(33,46)
#         char = chr(rand_number)
#         list_of_symbols.append(char)

#     #Random numbers
#     list_of_numbers = []
#     for index in range(0,numbers):
#         rand_number = random.randint(48,57)
#         char = chr(rand_number)
#         list_of_numbers.append(char)

#     number_of_letters = number_of_password - (numbers + number_of_symbol)
#     letters = []

#     for index in range(0, number_of_letters):
#         random_cap_low =  random.randint(0, 1)

#         if random_cap_low == 1:
#             #Capitals [65,90]
#             rand_number = random.randint(65, 90)
#             char = chr(rand_number)
#             letters.append(char)
#         else:
#             #lower case [97,122]
#             rand_number = random.randint(97, 122)
#             char = chr(rand_number)
#             letters.append(char)

#     total_list = list_of_symbols + list_of_numbers + letters

#     random.shuffle(total_list)
#     print(total_list)


# def calculate_love_score(name1, name2):
#     love_score = [0, 'love']
#     true_score = [0, 'true']
    
#     for item in name1.lower():
#         if item in true_score[1]:
#             true_score[0] +=1

#     for item in name2.lower():
#         if item in true_score[1]:
#             true_score[0] +=1

#     for item in name1.lower():
#         if item in love_score[1]:
#             love_score[0] +=1

#     for item in name2.lower():
#         if item in love_score[1]:
#             love_score[0] +=1
  
#     results = str(true_score[0]) + str(love_score[0])
#     results = int(results)
#     print(results)


# calculate_love_score("Kanye West", "Kim Kardashian")


# def encode(word,shift, encode_decode):
    
#     result = ''

#     for item in word:

#         if encode_decode ==  'encode':
#             if item == " ":
#                 ascii = ord(item)
#             else:
#                 ascii = ord(item) + shift

#         elif encode_decode == 'decode':
#             if item == " ":
#                 ascii = ord(item)
#             else:
#                 ascii = ord(item) - shift
#         print(item)
#         result += chr(ascii)


#     return result
        

# game_control = True

# while game_control:
#     encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
#     message = input('Type your message: ')
#     shift = int(input('Type the shift number: '))

#     if encode_decode.lower() == 'encode':

#         print(encode(message.lower(), shift, encode_decode))
#     elif encode_decode.lower() == 'decode':

#         print(encode(message.lower(), shift, encode_decode ))




#     game_continue = input("Type 'yes' if you wanty to go again. Otherwise type 'no'.")
#     if game_continue.lower() == 'yes':
#         game_control = True
#     else:
#         game_control = False


student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for item in student_scores:
    print(item)
    
    if student_scores[item] >= 91 and student_scores[item] <=100:
        student_grades[item] = "Outstanding"
    elif student_scores[item] >=81 and student_scores[item] <=90:
        student_grades[item] = "Exceeds Expectations"
    elif student_scores[item] >=71 and student_scores[item] <=80:
        student_grades[item] = "Acceptable"
    elif student_scores[item] <= 70:
        student_grades[item] = "Fail"
        
print(student_grades)



travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany":["Stuttgart", "Berlin"]

}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])


travel_log = {
    "France":{
        "cities_visited": ["Paris", "Lille","Dijon"],
        "total_visits": 12
    },
    "Germany":{
        "cities_visited": ["Berlin", "Humburg","Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])