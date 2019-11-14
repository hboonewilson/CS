#Boone Wilson
#DA 9
#Section A04
#11/7

def getHawkID():
    return ['hbwilson']

#write function that takes as an argument either a 12-digit positive integer or 
#string consisting of 12 digits and calculates the 13th digit
def calculatgeCheckDigit(n):
    #create a list to hold all of the digits as strings
    myList = []
    #convert n to a string myString
    myString = str(n)
    #add each digit to the list of digits in the correct order... turn to integers! 
    for num in myString:
        myList.append(int(num))
    #create a variable to track sum
    add = 0
    #digits at even indexes are added to sum and odd are multiplied by three and 
    #added to the sum
    for i in range(0, 12):
        if i % 2 == 0:
            #set even indicies' value to prod
            prod = myList[i]
        #odd!
        else:
            #set odd indicies' (value * 3) to product
            prod = myList[i] * 3
        #add whatever prod is to add
        add += prod
    for i in range(0, 10):
        if (add + i) % 10 == 0:
            return i

def flipBits(myString):
    for let in myString:
        if let == '0' or let == '1':
            pass
        else:
            return 'not a binary string'
    if len(myString) == 8:
        pass
    else:
        return 'wrong length'
    #create return str
    retstr = ''
    for let in myString:
        if let == '0':
            retstr += '1'
        else:
            retstr += '0'
    return retstr

def xor(string1, string2):
    zero = '0'
    one = '1'
    for number in string1:
        if number == zero or number == one:
            pass
        else:
            return 'not binary strings'
    for number in string2:
        if number == zero or number == one:
            pass
        else:
            return 'not binary strings'    
    if len(string1) == 4 and len(string2) == 4:
        pass
    else:
        return 'wrong length'
    retstr = ''
    for i in range(0, 4):
        if string1[i] == string2[i]:
            retstr += '0'
        else:
            retstr += '1'
    return retstr        
            