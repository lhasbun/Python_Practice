import random
import re
import sys
import os

def choose_word(word_list):

    seed = random.randint(0, 4000)

    chosen_word = word_list[seed]

    return chosen_word

def txt_to_lst(file_path):

    try:
        stopword=open(file_path,"r")
        lines = stopword.read().split('\n')
        return lines

    except Exception as e:
        print(e)

def main():

    # word_list = ["aardvark", "baboon", "camel"]

    #with open("C:\Users\lehas\Downloads\4000-most-common-english-words-csv.csv", 'r') as fd:
      #  reader = csv.reader(fd)
        #for row in reader:
           # lines = text_file.read().split(',')

    stages = ['''
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =========''', '''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========
            ''', '''
            +---+
            |   |
            O   |
                |
                |
                |
            =========
            ''', '''
            +---+
            |   |
                |
                |
                |
                |
            =========
            ''']       

    file_path = r"C:\Users\lehas\Downloads\4000-most-common-english-words-csv.csv"

    word_list = txt_to_lst(file_path)

    # Randomly choose a word from the word_list and assign it to a variable called chosen_word.

    active = True

    while active == True:

        print(" _")                                             
        print("| |")                                            
        print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
        print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
        print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
        print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
        print("                    __/ |")                      
        print("                   |___/ ")
        chosen_word = choose_word(word_list)
        chosen_array = list(chosen_word)
        blank_array = []
        for i in range(len(chosen_array)):
            blank_array.append('_')

        lives = 0

        # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
        while '_' in blank_array and lives < 6: 

            stage = stages[lives]

            print(stage)
            
            print(blank_array)

            while True:

                guess = str(input("\nGuess a letter:\n")).lower()

                if not re.match(r"^[a-zA-Z]+$", guess):
                    print("\nInvalid Input: Please enter a letter.\n")
                    continue

                if guess in blank_array:
                    print("Letter already guessed correctly, please pick a new letter.\n")
                    continue

                else:
                    break

            # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

            correct = guess in chosen_word

            indices = []

            if correct == True:

                for i in range(len(chosen_array)):
                    if(chosen_array[i] == guess):
                        indices.append(i)
                
                for i in range(len(indices)):
                    blank_array[indices[i]] = guess

                #print(blank_array)

            else:
                lives += 1
                print("Wrong guess, try again!")

        else:
            
            while True:

                if lives == 6:
                    print(stages[6])
                    reset = str(input('You Lose!\nPlay Again (Y/N)?\n'))
                else:
                    reset = str(input('You Win!\nPlay Again (Y/N)?\n'))

                if reset.lower() == 'y':
                    os.system('cls')
                    break

                elif reset.lower() == 'n':                
                    active = False
                    break

                else:
                    print(f'Ivalid Input\n')
                    continue

    else:
        
        sys.exit()
        

if __name__=="__main__": 
    main()