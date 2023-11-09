def switch(case, x, y, mylist):
    "Consider a list (list = []). You can perform the following commands:"
    if case == "insert":
        mylist.insert(int(x), int(y))
    elif case == "print":
        print(mylist)
    elif case == "remove":
        mylist.remove(int(x))
    elif case == "append":
        mylist.append(int(x))
    elif case == "sort":
        mylist.sort()
    elif case == "pop":
        mylist.pop()
    elif case == "reverse":
        mylist.reverse()


if __name__ == '__main__':
    N = int(input())
    
    mylist = []
    
    # Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. 
    # Iterate through each command in order and perform the corresponding operation on your list.
    for _ in range(N):
        inputline = input()
        x, y = 0, 0
        if len(inputline.split()) == 1:
            switch(inputline, x, y, mylist)
        elif len(inputline.split()) == 2:
            instruct, x = inputline.split()
            switch(instruct, x, y, mylist)
        else:
            instruct, x, y = inputline.split()
            switch(instruct, x, y, mylist)
