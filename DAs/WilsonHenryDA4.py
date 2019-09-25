#Henry Wilson
#Discussion Assignment 4
#Section 0A04
# Sep/19/19

def getHawkID():
    return ['hbwilson']

def problem1(length, width):
    area = length * width
    return f"The area of the rectangle is {area} square inches."
#if aList is even, return of the sum of all elements in aList. If odd return a 
#list with the length of the list as each element and the lentgth being the same
#as the aList
def problem2(aList):
    if len(aList) % 2 == 0:
        value = 0
        for item in aList:
            value += item
        return value
    else:
        lis = []
        length = len(aList)
        for i in range(0, length):
            lis.append(length)
        return lis
#return a list of the numbers in aList squared            
def problem3(aList):
    squares = []
    length = len(aList)
    for i in range(0, length):
        squares.append(aList[i] ** 2)
    return squares

#concatenate string1 + string2 + string1
def problem4(myString1, myString2):
    concat = myString1
    concat += myString2
    concat += myString1
    return concat
