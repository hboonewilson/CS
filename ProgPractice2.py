#pass as an argument a letter and a list... iterate through string looking for all
#indexes that have that letter (should not be case sensitive). Return 'letter not 
#found in string' if no instances of the letter are found in myString. If there
#are return those instances 

def whereIsLet(let, myString):
    under_list = myString.lower()
    retlist = []
    for i in range(0, len(myString)):
        if let == under_list[i]:
            retlist.append(i)
        else:
            pass
    if len(retlist) == 0:
        return 'Letter not found in string'
    else:
        return retlist 

