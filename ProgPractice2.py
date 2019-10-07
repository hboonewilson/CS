#pass as an argument a letter and a list... iterate through list looking for all
#indexes that have that letter (should not be case sensitive)

def whereIsLet(let, myList):
    retlist = []
    for i in range(0, len(myList)):
        if let == myList[i]:
            retlist.append(i)
        else:
            pass
    return retlist
