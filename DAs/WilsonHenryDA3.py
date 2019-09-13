#Henry Wilson
#Discussion 0A04
#September 12 2019

#getHawkID
def getHawkID():
    return ['hbwilson']

#take a temprature in farenheit roundng to the nearest integer
def celsiusToFahrenheit(temprature):
    #calculate
    f = temprature * (9/5) + 32
    #round to nearest int
    f_round = int(round(f, 0))
    return f_round


#checks to make sure temptrature is within -273.15 and 1000 then calculates f
#and adds it to a string
def celciusToFarenheitWords(temprature):
    #check to make sure argument is within this range
    if -273.15 <= temprature <= 1000:
        #calculate
        f = temprature * (9/5) + 32
        #round to nearest int
        f_round = int(round(f, 0))
        string = f"Notice: {temprature} degrees Celsius is equivalent to "  
        string += f"{f_round} degrees Fahrenheit."
        return string
    else:
        #if not: return out of range string.
        return "Temprature is out of range."

#function that takes a string as an argument if the string ONLY has 0s and 1s
#if only 0s and 1s return 'string' is a binary string. Otherwise return
#The length of the input is (len)
def AmIBinary(aString):
    isBinary = True
    for index in aString:
        if index == '0' or index == '1':
            pass
        else:
            isBinary = False
    if isBinary:
        return f"{aString} is a binary string."
    else:
        length = len(aString)
        return f"The length of the input is {length}."     