#!/bin/python35

def euclideanGCD(a,b):
    '''
    This is an implementation of the Euclidean algorithm for finding the Greatest Common Divisor of two numbers a and b.
    Source: https://en.wikipedia.org/wiki/Euclidean_algorithm
    
    Input:
        a,b - Two integers for which we are going to find the greatest common divisor
    
    Output:
        a - An integer which will contain the GCD value for two numbers
    ''' 
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a





