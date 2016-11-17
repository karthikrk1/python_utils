#!/bin/python35
'''
This is an implementation of the base conversion algorithm that converts the base of the number from 10 to anything specified.
The reverse conversion is also feasible with this implementation. 

Author: Karthik Ramakrishnan
'''
def convertFromBaseTen(n, base=2):
    '''
    This function is the implementation of the base conversion from Base 10 to Base 'base', which is given as input param to the program
    The default value of base is 2 for this implementation and can be overridden with additional bases as needed in the program.
    
    Input:
        n - The String representation of the number which is sent in for conversion. 
        base - The int base, which is the base to which the String must be converted from base 10.
    
    Output:
        num - The String representation of the number in base 'base' as specified by the program's input
    '''
    n = int(n)
    num = "" # This is a list to which the individual bits are added to. The list is a temporary store.
    while n > 0:
        digit = n%base
        nextValue= n//base # Integer division. Written in python 3+. May cause issues when run with Python 2. 
        n=nextValue
        num = str(digit)+num
    
    return num

    
def convertToBaseTen(n, base=2):
    '''
    This function is the implementation of the base conversion from Base 'base' to Base 10. This can be used to efficiently to convert a number into 
    base 10 representation. 
    
    Note: These functions use strings to manipulate the values and hence may not be the most optimised solution. The reason for returning an integer
    as a String representation is to represent higher order numbers as a String, since sometimes some values may overflow the int maxsize 
    
    Input:
         n - A String representation of the number in Base 'base'. 
         
         base - An integer representing the current base of the number.
    
    Output:
        
        num -  A string representation of the number in base 10.
    '''
    running_total = 0 # The running total. This contains the base 10 representation of the number after the loop terminates
    multiplier = 1 # This is used to multiply the base at each iteration
    
    # Iterate a string in reverse. Side Note: N is represented as a String in the input
    
    for i in range(len(n)-1,-1,-1): 
        running_total+=int(n[i])*multiplier
        multiplier*=base
    
    return str(running_total)

print(convertFromBaseTen("375931851", 5))
print(convertToBaseTen("20302030203", 4))

    
    
    