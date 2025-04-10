#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




def read_names():
    names_list = []
    with open('./Input/Names/invited_names.txt') as file:
        lines = file.readlines()
    
    for line in lines:
        names_list.append(line.replace("\n", ""))
    
    return names_list
        

def read_paragraph():
    paragraph = ""

    with open('./Input/Letters/starting_letter.txt') as file:
        paragraph = file.read()

    return paragraph


def mail_logic(name, letter):

    letter = letter.replace("[name]", name)
    with open(f'./Output/readyToSend/{name}.txt', mode='w') as file:
        file.write(letter)

names = read_names()

for name in names:
    paragraph = read_paragraph()
    mail_logic(name, paragraph)