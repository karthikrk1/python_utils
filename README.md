# python_utils
This repository contains some small utility functions that can be used in a variety of different algorithms. 

## Note:

The repository is coded in Python 3.5 and hence some 3.5+ stuff may not work well with Python 2 implementations. The idea being similar, it is easy to reproduce the code in Python 2 given these stuff are available

## List of Utilities:

This covers a comprehensive list of all the utilities stored in this git repo. This list will be constantly updated with the name of the utility and a small two or three line description of the uses of those functions

1. The Sieve of Eratosthenes:
 
This utility function is used to build the Sieve of Eratosthenes and initialize a prime number array upto size 10^6. The sieve algorithm runs in time O(n^1/2).

2. Base Conversion:

This file contains a simple implementation of the base conversion system. There are two functions in this implemenation.

`convertFromBaseTen`
`convertToBaseTen`

Note: Both these functions deal with integer as a String representation and hence I have type casted it inside the code. This was made with the assumption that Strings are efficient in storing huge numbers and thus avoid Arithmetic Errors in the code. 
    
