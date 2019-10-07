def getHawkID():
    return ['hbwilson']

#return the sum of all numbers in odd indexes
def getSumOdds(aList):
    #create variable to add to called add
    add = 0
    #iterate for indexes
    for i in range(0, len(aList)):
        #if index is odd
        if i % 2 != 0:
            #add to add variable
            add += aList[i]
        #if index is even
        else:
            #do nothing
            pass
    #return variable add
    return add

def reverseList(myList):
    #make negatives positive
    pos_list = []
    for number in myList:
        pos_list.append(abs(number))
    #make order revers
    reverse_list = []
    for i in range(0, len(myList)):
        new_i = len(myList) - i - 1
        reverse_list.append(pos_list[new_i])
    return reverse_list

#return all individuals letters and ignoring all digits and punctuation
def getLetters(myString):
    #create list to return
    retlist = []
    #iterate each character (ch)
    for ch in myString:
        #if ch is a letter
        if ch.isalpha():
            #check to see if it's not aready in retlist
            #boolean flag
            flag = False
            #iterate
            for i in retlist:
                #if myString[ch] is the same as retlist[i] 
                if ch == i:
                    #break from for loop, turn the flag True and check next ch in myString
                    flag = True
                    break
                #if ch is not in i
                else:
                    #go to next letter in retlist
                    pass
            #if flag was not swithced to ture (the letter in myString is not in retlist)   
            if not flag:
                #add to retlist
                retlist.append(ch)
            #if it wasn't switched to True (letter is already in retlist)
            else:
                #do nothing
                pass
    return retlist