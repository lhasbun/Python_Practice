import random
import os
import re

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):

    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift 
    # amount and print the encrypted text.  
    #e.g. plain_text = "hello", shift = 5, cipher_text = "mjqqt", print output: "The encoded text is mjqqt"

    # Split input text into array of characters
    letters = split(text)

    index = 0

    for letter in letters:

        abcNum = alphabet.index(letter) # Alphabetical ordinal position of letter

        outOfIndex = bool((abcNum + shift) > 25) # Check if index in alphabet plus shift would be out of range

        if outOfIndex:

            newIndex = -1 + ((abcNum + shift) - 25)
            newChar = alphabet[newIndex]

        else:

            newChar = alphabet[abcNum + shift]

        letters[index] = newChar

        index += 1

    encripted = ''.join(letters)

    return encripted


# Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):


  #Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift 
  # amount and print the decrypted text.  
  #e.g. cipher_text = "mjqqt", shift = 5, plain_text = "hello", print output: "The decoded text is hello"

    letters = split(text)

    index = 0

    for letter in letters:

        abcNum = alphabet.index(letter) # Alphabetical ordinal position of letter

        outOfIndex = bool((abcNum - shift) < 0) # Check if index in alphabet minus shift would be out of range

        if outOfIndex:

            newIndex = 26 + (abcNum - shift)
            newChar = alphabet[newIndex]

        else:

            newChar = alphabet[abcNum - shift]

        letters[index] = newChar

        index += 1

    decrypted = ''.join(letters)

    return decrypted

def caesar(text, shift, direction):

    if direction == "encode":

        encrypted = encrypt(text, shift)

        return encrypted

    else:

        decrypted = decrypt(text, shift)

        return decrypted


def split(word):

    return list(word)

def main():

    inSession = True

    while inSession:

        logo = """           
            ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
           a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
           8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
           "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
            `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
                                      88                                 
                       88             88                                 
                                      88                                 
            ,adPPYba,  88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
            a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
            8b         88 88       d8 88       88 8PP""""""" 88          
            "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
            `"Ybbd8"'  88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
                          88                                             
                          88           
            """

        print(logo)

        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

        if direction.lower() == 'encode' or direction.lower() == 'decode':

            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            encoded = caesar(text, shift, direction)

            print(f'The {direction.lower()}d text is: {encoded}')

            restart = input("Would you like to go again? Y/N\n")

            if restart.lower() == 'y':
                os.system('cls')
                continue
            elif restart.lower() == 'n':
                inSession = False
            else:
                print('INVALID INPUT: Please type in ''Y'' or ''N''')

        else:

            print('INVALID INPUT: Please type in ''encode'' or ''decode''')    
  
if __name__=="__main__": 
    main()