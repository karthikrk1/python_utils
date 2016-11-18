#!/bin/python35

import euclidean_gcd
def lcm(a,b):
    '''
    This implementation find the Least Common Multiplier for two numbers by calculating the GCD and then dividing the product by the GCD
    
    Input:
        a,b - Two numbers for which we need the LCM
    Output:
        out -  The integer value which corresponds to the LCM of a and b
    '''
    
    gcdiv = euclidean_gcd.euclideanGCD(a, b)
    prod = a*b
    out = prod//gcdiv
    return out
