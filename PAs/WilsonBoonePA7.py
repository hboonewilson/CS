#Boone Wilson
#PA7
#A04
#Nov 6

def getHawkID():
    return ['hbwilson']
def addDigits(n):
    retval = 0
    n = str(n)
    for num in n:
        retval += int(num)
    return retval
def intToList(n):
    retlis = []
    n = str(n)
    for num in n:
        retlis.append(int(num))
    return retlis
#take in a number, check that it's all digits and a length of 16...
#after this mult even indicies by 2 and add all indicies together...
#if sum of all indicies is module 10 (%10 == 0) return true else false
def checkCreditCard(n):
    #turn to string
    n = str(n)
    #check if n is all digits
    if not (n.isdigit()):
        #if not return 
        return "not digits"
    #check and make sure n is 16 ch long
    elif not (len(n) == 16):
        #if not return 
        return 'wrong length'
    #reconvert back to integer
    n = int(n)
    #call intoToList func to make list of n
    myList = intToList(n)
    #create final value (finval)
    finval = 0
    #iterate through myList for indicies
    for i in range(0, 16):
        #if i is even.. mult index by two
        if i % 2 == 0:
            product = myList[i] * 2
            #if product of the multiplication is two digits long use addDigits() 
            #set to add
            if len(str(product)) == 2:
                add = addDigits(product)
            #otherwise set add
            else:
                add = product
        
        #if i is odd .. set to add
        else:
            add = myList[i]
        #add add to finalval
        finval += add
    #if finalval %10 == 0 return True
    if finval % 10 == 0:
        return True
    #else return False
    else:
        return False