
def is_leap(year):
    "Determines whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False."
    leap = False

    #In the Gregorian calendar, three conditions are used to identify leap years:
    #The year can be evenly divided by 4, is a leap year, unless:
    if year % 4 == 0:
        # The year can be evenly divided by 100, it is NOT a leap year, unless:
        if year % 100 == 0:
            # The year is also evenly divisible by 400. Then it is a leap year.
            if year % 400 == 0:
                leap = True

    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))