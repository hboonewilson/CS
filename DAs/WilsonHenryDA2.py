#Henry Wilson
#Discussion Assignment 1
#Section 0A04
# Aug/29/19

#getHawkID
def getHawkID():
    return ['hbwilson']


#write a function with 3 arguements, all of which are numbers.
#return the three arguments' average rounded to the nearest THENTH
def calculateAverage(n1, n2, n3):
    #find mean
    mean = (n1 + n2 + n3) / 3
    #return rounded mean
    return round(mean, 1)


#write a function with 3 arguements, all of which are numbers.
#return the three arguments' average rounded to the nearest THENTH in the form..
#of a string.
def getAverageString(n1, n2, n3):
    #find mean
    mean = (n1 + n2 + n3) / 3
    #round mean
    rounded = round(mean , 1)
    #integrate mean into string
    return f"The average value is {rounded}."


#write a function that takes 3 arguments, 2 values, and a string ("S"/"P")
#if 'S': return the sum
#if 'P': return the product
def doMath(n1, n2, operation):
    #find out which operation to do from operation arg.. then return the answer
    if operation.upper() == 'S':
        return n1 + n2
    elif operation.upper() == 'P':
        return n1 * n2