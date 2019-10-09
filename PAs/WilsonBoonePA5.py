import random

def getHawkID():
    return ['hbwilson']

#Write a function that takes, as an argument a positive integer n and creates a file named eightBits.txt containing n randomly generated eight-bit binary strings, each on its own line. Examples of eight-bit binary strings include 00110101 name function eightBitStrings(n).
def eightBitStrings(n):
    #create file name 
    filename = 'eightBits.txt'
    #open file
    outputFile = open(filename, 'w')
    #create counter to refer to in while loop
    counter = 0
    #while loop saying: while our counter varialbe is less than argument
    while counter < n:
        #create a line string called linestr
        linestr = ''
        #iterate through range 0-8 to create an 8 digit string
        for i in range(0, 8):
            #create a random number between 0 and 1
            randnum = int(random.random()*2)
            #add each number to linestr as a string
            linestr += str(randnum)
        #after adding 8 binary digits to linestr write in that string and 
        #go to a new line
        outputFile.write(linestr + '\n')
        #increment counter by one to record how many loops the program has
        #done
        counter += 1
    outputFile.close()

#write function that takes an integer and a string as arguments that creates a file nCharacters.txt containing n lines... each showing a random character that is in the string       
def randomCharacters(n, myString):
    #filename
    filename = 'nCharacters.txt'
    #create file
    outputFile = open(filename, 'w')
    #counter value
    counter = 0
    #create while loop that runs until it reaches the number n
    while counter < n:
        #create a random number that is simplified to an index position
        randomindex = int(random.random()*len(myString))
        #use index to pick out a value from the string 
        randomvalue = myString[randomindex]
        #write value into program and create new line
        outputFile.write(randomvalue + '\n')
        #add one to counter to document a passing throught the loop
        counter += 1
    outputFile.close()
#takes two arguments myFile and case, which will be either upper or lower. if case is equal to upper the function will open the file convert all characters on each line to upper write each line to a new file named 'upperCase.txt' and return the string "Converted file to upper case." if case is eqal to "lower" the function will open file convert all characters on each line to lower write each line to a new file called 'lowerCase.txt' and return the string "Converted file to lower case" if case argument is anything other than upper or lower return 'Invalid parameter'

def changeTheCase(myFile, case):
    #if case is upper filetowrite is 'upperCase.txt' 
    if case == 'upper':
        filetowrite = 'upperCase.txt'
    #eilf case is upper filetowrite is 'lowerCase.txt'
    elif case == 'lower':
        filetowrite = 'lowerCase.txt'
    #finally if case is neither return Invalid parameter
    else:
        return "Invalid parameter."
    
    #read file by setting it to a varable (readfile), opening it and reading it
    reader = open(myFile)
    readfile = reader.read()
    #if case is == upper alter capitalize everything in readfile (readfile.upper()) setting it to alteredfile
    if case == 'upper':
        alteredfile = readfile.upper()
    #at this point case has to be 'lower' because anything would have broken out of function
    #if it is 'lower' alter the readfile into all lower (readfile.lower()) setting it to alteredfile
    else:
        alteredfile = readfile.lower()
    #rewrite myFile by replacing it with altered file contents
    rewritefile = open(myFile, 'w')
    rewritefile.write(alteredfile)
    #make the new file 
    fileOutput = open(filetowrite, 'w')
    fileOutput.write(alteredfile)
    #close all files 
    rewritefile.close()
    fileOutput.close()