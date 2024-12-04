# # # # # # # # # # # # # # #  Blackjack Project v1.0 # # # # # # # # # # # # # # # # # # # # #

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

import random

# Import ASCII art resources from blackjackart,py
from blackjackart import logo, ace

def main():
    print(logo)
    print(ace)

if __name__ == "__main__":
    main()

