import math
import os
import random
import re
import sys

if __name__ == '__main__':
    # input(): allows user input
    # strip(): removes leading and trailing characters
    n = int(input().strip())
    
    # If n is odd, print Weird
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0:
        # If n is even and in the inclusive range of 2 to 5, print Not Weird
        if n >= 2 and n <= 5:
            print('Not Weird')
        # If n is even and in the inclusive range of 6 to 20, print Weird
        elif n >= 6 and n <= 20:
            print('Weird')
        # If n is even and greater than 20, print Not Weird
        else:
            print('Not Weird')