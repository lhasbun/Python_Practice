#Password Generator Project
import random
import os
import re

def easy_password(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols):

    char_list = []

    for i in range(0, nr_letters):
        rand_letter = letters[random.randint(0, len(letters) - 1)]
        char_list.append(rand_letter)

    for i in range(0, nr_symbols):
        rand_symbol = symbols[random.randint(0, len(symbols) - 1)]
        char_list.append(rand_symbol)

    for i in range(0, nr_numbers):
        rand_number =  numbers[random.randint(0, len(numbers) - 1)]
        char_list.append(rand_number)

    password = ''.join(char_list)

    return password

def hard_password(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols):

    char_list = []

    for i in range(0, nr_letters):
        rand_letter = letters[random.randint(0, len(letters) - 1)]
        char_list.append(rand_letter)

    for i in range(0, nr_symbols):
        rand_symbol = symbols[random.randint(0, len(symbols) - 1)]
        char_list.append(rand_symbol)

    for i in range(0, nr_numbers):
        rand_number =  numbers[random.randint(0, len(numbers) - 1)]
        char_list.append(rand_number)

    random.shuffle(char_list)

    password = ''.join(char_list)

    return password

def main():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    active = True

    while active == True:

        print("\nWelcome to the PyPassword Generator!\n")
        print("Instructions: Enter the number of letters, symbols, and numbers you want your password to contain.\nMinimum Password Length: 4\nMaximum Password Length: 30\n")

        while True:
            
            while True:

                nr_letters = input("How many letters would you like in your password? 0-9\n")

                if not re.match(r"^[0-9]+$", nr_letters):
                    print("Please enter a value between 0-9")
                    continue

                else:
                    nr_letters = int(nr_letters)
                    break

            while True:

                nr_symbols = input(f"How many symbols would you like? 0-9\n")

                if not re.match(r"^[0-9]+$", nr_symbols):
                    print("Please enter a value between 0-9")
                    continue

                else:
                    nr_symbols = int(nr_symbols)
                    break

            while True:

                nr_numbers = input(f"How many numbers would you like? 0-9\n")

                if not re.match(r"^[0-9]+$", nr_numbers):
                    print("Please enter a value between 0-9")
                    continue

                else:
                    nr_numbers = int(nr_numbers)
                    break

            if((nr_letters + nr_symbols + nr_numbers) < 4):
                print(f'Not long enough, please enter at least 4 characters in any combination')
                continue

            if((nr_letters + nr_symbols + nr_numbers) > 30):
                print(f'Too long, please enter 30 or less characters in any combination')
                continue

            else:
                break

        while True:
            
            rand_sel = str(input(f"Would you like to randomize character order? Y/N\n"))

            #Eazy Level - Order not randomised:
            #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
          
            if(rand_sel.lower() == "n"):
                password = easy_password(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols)
                print(f'Here is your password: {password}\n')
                break

            #Hard Level - Order of characters randomised:
            #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P   

            elif(rand_sel.lower() == "y"):
                password = hard_password(nr_letters, nr_symbols, nr_numbers, letters, numbers, symbols)
                print(f'Here is your password: {password}\n')
                break

            else:
                print('Invalid Input\n')
                continue

        while True:

            reset = str(input(f'Generate a new password? Y/N\n'))

            if reset.lower() == 'y':
                break

            elif reset.lower() == 'n':                
                active = False
                break

            else:
                print(f'Ivalid Input\n')
                continue

    else:

        exit

if __name__=="__main__": 
    main()



