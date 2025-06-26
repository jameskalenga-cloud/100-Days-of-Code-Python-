
import pandas as pd


# Read the CSV file (replace with your actual filename)
student_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

# Loop through each row
new_dict = { row.letter: row.code for index, row in student_data_frame.iterrows()}

try:
    name = input("Please enter your name: ")
    results = [new_dict[f"{letter.upper()}"] for letter in name]
except KeyError as message:
    print("please enter valid name")
    name = input("Please enter your name: ")
    results = [new_dict[f"{letter.upper()}"] for letter in name]


    

print(results)
