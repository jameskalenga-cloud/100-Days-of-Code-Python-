# print("Welcome to the tip calculator!")
# total_amount = int(input("What was the total amount? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people =  int(input("How many poeple to split the bill?"))

# compute = round(((total_amount + total_amount * (tip/100))/people), 2)

# print(f"Each person should pay: ${compute}")

# Second problem 
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# Pizza amount
pizza_options = ['s','m', 'l']

if size.lower() in pizza_options:
    if size.lower() == pizza_options[0]:
        pizza_amount = 15
    elif size.lower() == pizza_options[1]:
        pizza_amount = 20
    elif size.lower() == pizza_options[2]:
        pizza_amount = 25
else:
    pizza_amount = 0

# Adding Pepperoni
pepperoni_options = ['y', 'n']

if pepperoni.lower() in pepperoni_options:
    if pepperoni.lower() == pepperoni_options[0]:
        pizza_amount += 2

#adding extra cheese
cheese_options = ['y', 'n']

if extra_cheese.lower() in cheese_options:
    if extra_cheese.lower() == cheese_options[0]:
        pizza_amount += 1

print(f"Total amount {pizza_amount}")