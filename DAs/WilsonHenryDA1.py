#Henry Wilson
#Discussion Assignment 1
#Section 0A04
# Aug/29/19

#return ['hawkid']
def getHawkID():
    return ['hbwilson']

#add two arguments into the function and return the
#first value minus the second value
def subtractThem(a,b):
    return a-b
#add the three arguments and return the sum 
def addEm(a, b, c):
    return a + b + c

#pass the word you want to echo then how many times you'd like to 
#eco and return result
def echo(word, x):
    return word*x

#pass in words1 copied 5 times, word2 copied 3 times, and retrun them both
#concatenated 
def addWords(word1, word2):
    first_word = word1 * 5
    second_word = word2 * 3
    return first_word + second_word

#takes 2 numbers as arguments, add them and return a descriptive sentence of the 
def sumDescription(value1, value2):
    new_value = value1 + value2
    return "The sum of " + str(value1) + " and " + str(value2) + " is " + str(new_value) + '.'

#pass in a persons name and town and return a sentence with those words.
def introduction(name, town):
    return "Hello. My name is " + name + " I love the weather in " + town + '.'
