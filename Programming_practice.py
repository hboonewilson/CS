#whileloop function that iterates the number of times you tell it in the 
#argument (n) adding a specific number or character (ch) into myList
def whileList(n):
    #myList: record ch appendings
    myList = []
    #keep track of iteratinons
    counter = 0
    while len(myList) < n:
        #while the length of myList isn't equal to the argument n...
        ch = "yodel"
        counter += 1
        #append the ch variable and loop until while loop is broken by n == len(myList)
        myList.append(ch)
    print(f"{ch} has been appended {counter} times.")
    return myList