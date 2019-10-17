#Wilson Boone
#Discussion Assignment 7
#Section 0A04
# OCT/17/19

def getHawkID():
    return ['hbwilson']

def problem1(n):
    store = []
    for i in range(1, n + 1):
        x = i ** 2
        store.append(x)
    ans = 0
    for value in store:
        ans += value
    return ans

#Function that takes as arguments, slope, intercept, x coordinate of a point on the line and returns a y coordinate of the point on the line.

def problem2(slope, intercept, x):
    #create the quation y = mx + b
    y = (slope * x) + intercept
    return y

#Write a function that takes as a na rgument a list, and returns a LIST that duplicates the elements in the list, following the pattern show in the example below
def problem3(aList):
    #create return list (retlis)
    retlis = []
    #iterate aList for values
    for value in aList:
        #append each value 2 times
        retlis.append(value)
        retlis.append(value)
    #return retlis
    return retlis

#Write a function that takes two lists of distinct positive integers and returns the list whose product of elements is larger. You must iterate through the lists using either a for loop or while loop
def problem4(list1, list2):
    #create two variable that will count product (v1,v2)
    v1 = 1
    v2 = 1
    #iterate list1 for values
    for value in list1:
        v1 *= value
    for value in list2:
        v2 *= value
    if v1 > v2 :
        return list1
    elif v2 > v1:
        return list2
    else:
        return 'They are the same.'