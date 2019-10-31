#Boone Wilson
#Programming Assignment 6
#Section A04
#10/31
def getHawkID():
    return ['hbwilson']


def maxValueInFile(fileName):
    filename = open(fileName)
    valmax = 0
    for number in filename:
        number =  int(number)
        if number < 0:
            lismax = number
            for number in filename:
                number = int(number)
                if lismax < number:
                    lismax = number
                else:
                    pass
            return lismax
        else:
            if valmax < number:
                valmax = number
            else:
                pass
    return valmax

def averageValueInFile(fileName):
    filename = open(fileName)
    runningtally = 0
    long = 0 
    for number in filename:
        number = int(number)
        runningtally += number
        long += 1
    return runningtally / long 

def greaterThanN(fileName, n):
    if n <= 750 and n >= -750:
        filename = open(fileName)
        linecounter = 0
        for line in filename:
            if int(line) > n:
                linecounter += 1
            else:
                pass
        return linecounter
    else:
        return 'Your integer is out of range.'