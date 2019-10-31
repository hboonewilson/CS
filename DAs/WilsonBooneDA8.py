#Boone Wilson
#Discussion Assignment 6
#Section A04
#10/31
import random

def getHawkID():
    return ['hbwilson']

def fourBitStrings(n):
    filename = 'fourBits.txt'
    fileouput = open(filename, 'w')
    counter = 0
    while counter < n:
        linestr = ''
        for i in range(0,4):
            randnum = int(random.random()*2)
            randnum = str(randnum)
            linestr += randnum
        fileouput.write(linestr + '\n')
        counter += 1
    fileouput.close()

def makeStrings(bits, strings, fileName):
    filename = fileName
    fileoutput = open(filename, 'w')
    counter = 0
    while counter < strings:
        bitstr = ''
        for i in range(0, bits):
            numrand = int(random.random() * 2)
            numrand = str(numrand)
            bitstr += numrand
        fileoutput.write(bitstr + '\n')
        counter += 1
    fileoutput.close()
    
def eightBits(n):
    if n > 0 and n < 256:
        filename = 'nBits.txt'
        fileoutput = open(filename, 'w')
        counter = 0
        while counter < n:
            linstr = ''
            for i in range(0, 8):
                numrand = int(random.random() * 2)
                numrand = str(numrand)
                linstr += numrand
            fileoutput.write(linstr + '\n')
            counter += 1
        fileoutput.close()
    else:
        return "Error: value is out of range."