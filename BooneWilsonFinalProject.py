#CS Project: Huffman codes.  This project will focus on the process of
#creating and using Huffman codes.  Review the lecture notes related
#to Huffman codes and fixed length codes.  Do not modify the two helper 
#functions that bave been provided.

#helper function 0: this function creates a file which we can use to
#create files to test
def createFiles(fileName):
    myFile = open(fileName, "w")
    string1 = "The quick brown fox jumps over the lazy dogs."
    myFile.write(string1)
    myFile.write("\n")
    string2 = "Now is the time for all good men to come to the aid of their country."
    myFile.write(string2)
    myFile.close()

#getHawkID() function
#this function is worth 5 points
def getHawkID():
    return ['hbwilson']

#Write a function that takes, as an argument, the name of 
#a file and returns a list consisting of two lists: the first list
#contains all of the individual characters in the file, in the order in
#which they appear in the file, and the
#second contains the corresponding frequencies of each character.
#we will name this function getCharacterFrequencies(myFile).
#for example, for the file created in problem 0, the result should be
#following list of lists:

#[['T', 'h', 'e', ' ', 'q', 'u', 'i', 'c', 'k', 'b', 'r', 'o', 'w', 'n', 'f', 'x',
#'j', 'm', 'p', 's', 'v', 't', 'l', 'a', 'z', 'y', 'd', 'g', '.', '\n', 'N'],
#[1, 5, 9, 23, 1, 3, 5, 3, 1, 1, 5, 13, 2, 3, 3, 1, 1, 4, 1, 3, 1, 8, 3, 3, 1, 2, 3, 2, 2, 1, 1]]

#This problem is worth 15 points

def getCharacterFrequencies(myFile):
    #open and read file
    actionFile = open(myFile, 'r')
    actionFile = actionFile.read()
    unique = [actionFile[0]]
    #iterate from index 1 to the length of actionFile
    for i in range(1, len(actionFile)):
        #let is the index we are in
        let = actionFile[i]
        #set flag = True (newlet)
        newlet = True
        #iterate by character of uniqe
        for char in unique:
            #if character in uniqe == letter from actionFile..
            if char == let:
                #newlet = False and break
                newlet = False
            #if char is not == let do nothing
        #if newlet is true..
        if newlet:
            #add newlet to unique
            unique.append(let)
        #otherwise grab next letter
    #count how many times each character appears in file and adding that to..
    #another list
    #create couting list (liscount)
    liscount = []
    #iterate through unique for characters
    for char in unique:
        #create variable to count number of times seen
        numtimes = 0        
        #iterate through actionFile for letters
        for letter in actionFile:
            if char == letter:
                numtimes += 1
        liscount.append(numtimes)
    #return two lists
    return [unique, liscount]
    

#write a function that takes, as arguments, two lists, one of which is a
#character list and the other is the corresponding frequencies, and sorts
#the characters in ascending order of frequencies.  The function should
#return a list consististing of two lists: the first list is the list of
#characters and the second is the list of corresponding frequencies, consistent
#with the rearranged characters.  for example, 

#>>>sortCharacters(["a", "b", "c", "d"], [5, 8, 3, 2]) 

#should return the list [["d", "c", "a", "b"], [2, 3, 5, 8]]
#notice that both the characters and the frequencies have been rearranged.

#this problem is worth 25 points

def sortCharacters(characterList, frequencyList):
    #create ret lists
    char_ret = []
    freq_ret = []    
    while len(frequencyList) != 0:
        #set first number in frequencyList to low
        low = frequencyList[0]
        #set first index to in_low
        in_low = 0
        #iterate frequencyList for index
        for i in range(0, len(frequencyList)):
            num = frequencyList[i]
            #if low is bigger than num
            if num < low:
                #num is new low
                low = num
                #num's index is new in_low
                in_low = i
        #after finding smallest...
        #pop from index in_low from characterList and frequencyList
        char_ret.append(characterList.pop(in_low))
        freq_ret.append(frequencyList.pop(in_low))
    return [char_ret, freq_ret]

#write a function that takes, as arguments, a string of characters, a list
#of characters and the corresponding huffman code for those characters.  
#It encodes the string using the huffman code, and returns the resulting
#binary string.  For example, 

#>>>encodeStringHuffman("ABAABCCAACCCCCAA", ["A", "B", "C"], ["1", "00", "01"])

#should return the binary string '1001100010111010101010111'
#you should assume that every character in myString is in the list of
#characters myCharacters.

#this problem is worth 10 points

def encodeStringHuffman(myString, myCharacters, myCode):
    #create return string
    retstr = ''
    #iterating for value of the string
    for let in myString:
        #iterate through myCharacters for index
        for i in range(0, len(myCharacters)):
            #if the letter we're looking at is the same in the string and list
            if let == myCharacters[i]:
                #add corresponding index from myCode to the return string
                retstr += myCode[i]    
                break
    return retstr

#write a function that takes, as arguments, a binary string, a list
#of characters and the corresponding huffman code for those characters.  
#It decodes the binary string using the huffman code, and returns the
#resulting decoded string.  For example, 

#>>>decodeStringHuffman("1001100010111010101010111", ["A", "B", "C"], ["1", "00", "01"])

#should return the string 'ABAABCCAACCCCCAA'

#this problem is worth 20 points

def decodeStringHuffman(binaryString, myCharacters, myCode):
    #create return string
    retstr = ''
    #create an eval string
    st_eval = ''
    #iterate binaryString for value
    for num in binaryString:
        #add num to st_eval
        st_eval += num
        #iterate myCode for index
        for i in range(0, len(myCode)):
            #if st_eval is equal to this index in myCode
            if st_eval == myCode[i]:
                #add corresponding index in myCharacters to retstr
                retstr += myCharacters[i] 
                st_eval = ''
                break
    return retstr

    
#write a function that takes, as arguments, a string of characters, a list
#of characters, and the corresponding fixed length code for those characters.
#It encodes the string using the fixed length code, and returns the resulting
#binary string.  For example, 

#>>>encodeStringFixed("ABAABCCAACCCCCAA", ["A", "B", "C"], ["11", "10", "00"])

#should return the binary string '11101111100000111100000000001111'
#your function should work for fixed length codes of arbitrary length.

#this problem is worth 10 points

def encodeStringFixed(myString, myCharacters, myCode):
    #create return string
    retstr = ''
    #iterating for value of the string
    for let in myString:
        #iterate through myCharacters for index
        for i in range(0, len(myCharacters)):
            #if the letter we're looking at is the same in the string and list
            if let == myCharacters[i]:
                #add corresponding index from myCode to the return string
                retstr += myCode[i]    
                break
    return retstr


#write a function that takes, as arguments, a binary string, a list
#of characters and the corresponding fixed length code for those characters.  
#It decodes the binary string using the fixed length code, and returns the
#resulting decoded string.  For example, 

#>>>decodeStringFixed("11101111100000111100000000001111", ["A", "B", "C"], ["11", "10", "00"])

#should return the string 'ABAABCCAACCCCCAA'
#your function should be able to handle fixed length encodings of arbitrary length

#this problem is worth 15 points
def decodeStringFixed(binaryString, myCharacters, myCode):
    #create return string
    retstr = ''
    #create an eval string
    st_eval = ''
    #iterate binaryString for value
    for num in binaryString:
        #add num to st_eval
        st_eval += num
        #iterate myCode for index
        for i in range(0, len(myCode)):
            #if st_eval is equal to this index in myCode
            if st_eval == myCode[i]:
                #add corresponding index in myCharacters to retstr
                retstr += myCharacters[i] 
                st_eval = ''
                break
    return retstr


    

