def getHawkID():
    return ["hbwilson"]

#ONLY USE COURSE CONCEPTS DON'T USE BUILT IN HELP





#create a function that takes, as an argument, 2 strings and 
#dtermines if they are anagrams
def anagrams(string1, string2):
    #check to make sure they have the same amount of letters
    long_1 = len(string1)
    long_2 = len(string2)
    #if same length:
    if long_1 == long_2:
        #iterate through string 1
        #create boolean that will be returned (retbol)
        retbol = True
        for ch in string1:
            #boolean to switch to True if letter is contained in list
            contained = False
            #check to see if ch is in string2 through iterating through list and setting boolean equal to true
            for let in string2:
                #if letter you're checking in string 2 is equal to letter in string 1, break out
                if ch == let:
                    contained = True
                    break
                elif ch != let:
                    pass
            #if contained was not switched to true return false
            if not contained:
                return False
            #if contained was switched to true continue iterating
            else:
                pass
        return retbol
    #if strings aren't the same length
    return False
                
                
                
    
    
    
    
#should return a list where odd indexes return the letter that
#was there
#and even indexs how many times the odd index is a row
def runLengthEncoding(myList):
    #create a list that holds streak letters (letstr)
    letstr = []
    #create another list for returning (retlis)
    retlis = []
    #iterate
    for index in myList:
        if len(letstr) != 0:
            #check to see if index 0 of letstr is eual to value
            if letstr[0] == index:
                #add value to letstr
                letstr.append(index)
                
            else:
                #if index is not the same as index 0 of letstr add old value
                #to retlist and length of the streak, then reset letstr
                retlis.append(letstr[0])
                retlis.append(len(letstr))
                letstr = [index]
        else:
            letstr = [index]
    #after reaching the end of the list, add the final stats for the last letter
    #into retlist
    retlis.append(letstr[0])
    retlis.append(len(letstr))    
    return retlis






# Write a function that takes, as an argument, a string (which may contain spaces), and returns the Boolean True if it is a palindrome Assume that the string consists of lower case letters only, and no punctuation. Think about how to handle spaces...removing them before testing the string might be a good approach. Name your function palindrome(myString). In this case, there may be spaces that do not need to line up, as in the example “nurses run”.
def palindrome(myString):
    no_space = []
    #iterate through myString
    for ch in myString:
        #if character (ch) is not equal to a space
        if ch != ' ':
            #append ch to no_space
            no_space.append(ch)
        #if ch is a space ignore it
        else:
            pass
    #create boolean flag called the_same
    the_same = True
    #iterate throgh length of no_space
    for i in range(0, len(no_space)):
        #create a value that is the opposite index of i 
        op_index = len(no_space) - i - 1
        #if the index is the same as it's opposite index don't alert the flag (pass)
        if no_space[i] == no_space[op_index]:
            pass
        #if the index is not the same as it's opposite, alert flag and break loop
        else:
            the_same = False
            break
    #after for loop has been run or broken, return boolean the_same
    return the_same


        

            
        