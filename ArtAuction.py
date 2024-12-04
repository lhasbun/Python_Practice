import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
    '''

def find_highest_bid(bid_dict):

    highest_bid = 0

    bidder = ""

    for bidder in bid_dict:

        bid_amt = bid_dict[bidder]

        if bid_amt > highest_bid:

            highest_bid = bid_amt
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}")


def main():

    print(logo)
    print("\nWelcome to the secret auction program.\n")

    bid_dict = {}

    bidEnd = False

    while bidEnd == False:

        name = input("What is your name?:")
        bid = input("What's your bid?: $")

        bid_dict[name] = bid
        
        otherBid = input("Are there any other bidders? Type 'yes' or 'no'.\n")

        valid = False

        while not valid:        

            if otherBid.lower() == 'yes':
                os.system('cls')
                break
            elif otherBid.lower() == 'no':
                bidEnd = True
            else:
                print("Not a valid response, please type 'yes' or 'no'\n")

    find_highest_bid(bid_dict)
    
if __name__=="__main__": 
    main()
