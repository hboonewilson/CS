#Collatz Conjecture - Start with a number n > 1. Find the number of steps it... 
#takes to reach one using the following process: If n* is even, divide it by 2. 
#If *n is odd, multiply it by 3 and add 1.

collatz = True
while collatz:
        input_num = int(input("Give me a number higher than 1: "))
        if input_num > 1:
                number = input_num
                collatz = False
        elif input_num == 1:
                print("A number larger than 1 please.")
        else:
                print("That number is less than 1!")


steps = 0
while number != 0:
        print(number)
        steps += 1
        if number%2 == 0:
                number = number/2       
        if number == 1:
                print(f"It took {steps} steps to make it to one.")  
                break
        if number%2 == 1:
                number = number*3 + 1        
        
  