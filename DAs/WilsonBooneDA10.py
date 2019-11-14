#Boone Wilson
#Discussion Assignment 10
#Section A04
#Nov 14

def getHawkID():
    return ['hbwilson']



#Write function that takes as an argument a list of pos inegers and a target 
#value,and returns the number of times that the target value appears in the list 
#call this funtion problem 1
def problem1(myList, target):
    #create a target counter named counttarg
    counttarg = 0
    #iterate list
    for num in myList:
        #if number is equal to target add 1 counttarg
        if num == target:
            counttarg += 1
        #else, pass
        else:
            pass
    #after iteration, return counttarg
    return counttarg



#Write a function that takes, as argument, a positive integer and returns the sum
#of its digits. Call this function problem2(value)
def problem2(value):
    #turn value into string so we can iterate
    value = str(value)
    #create a sum counter called retsum
    retsum = 0
    #iterate
    for num in value:
        #turn num back to int and add to retsum
        retsum += int(num)
    #after iteration op, return retsum
    return retsum

#Write a function that takes as aruments, to strings: myString and charString, and
#is called problem3 (myString, charString). For each letter in charString, count
#the number of times that it appears in myString (and is case sensitive) and 
#returns the reuslt in the form of a list indicating the individual count values
#as shown in the example
def problem3(myString, charString):
    #create list to return (retlis)
    retlis = []
    #iterate through charString
    for char in charString:
        #create counter for char (countchar)
        countchar = 0
        #iterate through myString
        for let in myString:
            #if let is same as char
            if let == char:
                #add 1 to count char
                countchar += 1
            #otherwise pass
            else:
                pass
        #after iteration of myString format index for retlis
        retlis.append(f"{char}={countchar}")
    #after iteration through charString return retlis
    return retlis
    
#Write a function that takes as an argument two lists of equal length containing 
#positive integers and returns the list formed by weaving the two lists together
#starting with the first element in the first list tame your function 
#problem4(list1,list2)
def problem4(list1, list2):
    #create list to return (weavelis)
    weavelis = []
    #because both are equal length.. start by deciding length to iterate 
    #(len(either list)
    iterlen = len(list1)
    #iterate for indicies 
    for i in range(0, iterlen):
        #for indicy i, start with appending from list one to weavelis
        weavelis.append(list1[i])
        #follow with list two to keep order
        weavelis.append(list2[i])
    #after iteration op... return weavelis
    return weavelis
    