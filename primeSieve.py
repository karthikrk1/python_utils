#!/bin/python3
'''
This is an implementation of the sieve of eratosthenes. It is created for n=10^6 (Default Value).
To use this in the program, please import this program as import primeSieve and call the default buildSieve method 

Author: Karthik Ramakrishnan
'''

def buildSieve(N=1000000):
    '''
    This function is an implementation of the sieve of eratosthenes. The function creates a boolean array of size N and marks the 
    prime numbers as True. This is an utility function that creates a boolean array for the sieve and sets up the prime numbers. 
    
    Args:
        N - The upper bound until which we need to set up the sieve. 
        
    Return:
        isPrime - The boolean array with all the prime numbers set as True. The remaining values are made False.
    '''
    N+=1 # This is to make sure we have the N inclusive in the array and not getting it lost due to 0-based indexing of Python lists 
    isPrime = [True] * N # Initializing the isPrime list with all True values.
    isPrime[0] = isPrime[1] = False # Since 0 and 1 are considered Neither Prime nor composite. So we make them False.
    for (ind, num) in enumerate(isPrime):
        if num:
            for no in range(ind*ind, N, ind): # This is used to mark the factors as not Prime. 
                isPrime[no] = False
    return isPrime
    
    


