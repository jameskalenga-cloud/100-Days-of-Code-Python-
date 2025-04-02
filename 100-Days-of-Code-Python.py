print("Welcome to the tip calculator!")
total_amount = int(input("What was the total amount? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people =  int(input("How many poeple to split the bill?"))

compute = round(((total_amount + total_amount * (tip/100))/people), 2)

print(f"Each person should pay: ${compute}")