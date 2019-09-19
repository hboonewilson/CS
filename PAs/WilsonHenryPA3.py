#Henry Wilson
#Project Assignment 
#Section 0A04
# Sep/18/19

#gethawkID
def getHawkID():
    return ["hbwilson"]


#write a function that takes, as an argument, a list identified by the
#variable aList. If the list only contains elements containing 
#digits(strings or integers) return string of concatenated list. 
#if not integers, return the string 'The length of the input is (len).'
def AmIDigits(aList):
    #set flag to true
    AmID = True
    #iterate through list, checking to see if the entire list is made up 
    #of digits
    for index in aList:
        if str(index).isdigit():
            continue 
        #if the list is not totally made up of digits change flag to false
        else:
            AmID = False
    #if flag is still true concatenate the integers together and return
    #them as one string        
    if AmID:
        concat = ''
        for index in aList:
            concat += str(index)
        return concat
    #if flag was turned false return a string describing its length
    elif not AmID:
        return f"The length of the input is {len(aList)}."

#Write a function that takes a list and a string, as arguments, and 
#returns a Boolean based on whether or not all o fthe letters in the string 
#appear somwhere in the list.
def findLetters(myList, myString):
    concat = ''
    #concat myList to make it easier to loop through to check it
    for index in myList: 
        concat += index
    #iterate through the two lists...(one item of myString to all indexes
    #in myList) 
    #false conditional statement was_it_th
    #loop through
#Write a function that takes, as an argument, a list, and an integer, n. 
#If the integer is negative, the function should return a list containing
#two lists, one being the original list, and the other being a list of 
#zeros to the absolute value of n. If n is zero, return the last element
#in the list. Otherwise return the sum of the list
def finalFunction(myList, n):
    #using if statements, check what n is (negative/zero/neither)
    if n < 0:
        zeros = []
        for z in range(0, abs(n)):
            zeros.append(0)
        return [myList, zeros]
    elif n == 0:
        return myList[-1]
    else:
        total = 0
        for num in myList:
            total += num
        return total 