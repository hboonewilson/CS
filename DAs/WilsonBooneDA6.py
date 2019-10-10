#Wilson Boone
#Discussion Assignment 
#Section 0A04
# OCT/10/19

def getHawkID():
    return ['hbwilson']

def returnLetters(myString):
    #create excluded list (exclist)
    exclist = []
    #iterate through string
    for ch in myString:
        #if ch is letter add it to exclist 
        if ch.isalpha():
            exclist.append(ch)
        #if not ignore letter
        else:
            pass
    #return excelist
    return exclist

def returnUniqueLetters(myString):
    exclist = returnLetters(myString)
    retlist = []
    #iterate through exclist
    for letter in exclist:
        if len(retlist) != 0:
            #create flag (letterflag)
            letterflag = True
            #iterate retlist
            for i in retlist:
                if i != letter:
                    pass
                else:
                    letterflag = False
                    break
            if letterflag:
                retlist.append(letter)
            else:
                pass
        else:
            retlist.append(letter)
    return retlist

def makeTwoListsOfLists(string1, string2):
    s1 = returnUniqueLetters(string1)
    s2 = returnUniqueLetters(string2)
    return [s1,s2]