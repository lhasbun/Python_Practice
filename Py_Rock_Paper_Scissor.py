import random
import os
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

play = True

player_wins = 0

npc_wins = 0

while(play == True):

    player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))

    print(choices[player_choice] + '\n')

    print('Computer chose:\n')

    npc_choice = random.randint(0, 2)

    print(choices[npc_choice] + '\n')

    if(player_choice == npc_choice):
        print('You Draw')

    if(player_choice == 0):
        if(npc_choice == 1):
            print('You Lose')
            npc_wins += 1
        elif(npc_choice == 2):
            print('You Win')
            player_wins += 1
    elif(player_choice == 1):
        if(npc_choice == 0):
            print('You Win')
            player_wins += 1
        elif(npc_choice == 2):
            print('You Lose')
            npc_wins += 1
    else:
        if(npc_choice == 0):
            print('You Lose')
            npc_wins += 1
        elif(npc_choice == 1):
            print('You Win')
            player_wins += 1

    print(f'\nCurrent Record:\nPlayer:{player_wins}\nComputer:{npc_wins}\n')

    cont_loop = True
    
    while cont_loop == True:

        play_str = str(input('Play Again? Y/N\n'))

        match play_str.lower():
            case 'y':
                os.system('cls')
                cont_loop = False
            case 'n':
                play = False
                cont_loop = False
            case _:
                print('Invalid Input\n')
                continue

else:

    sys.exit()
