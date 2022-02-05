'''
Problem Statement
Let xyz denote the 3-digit integer whose digits are x, y, z from left to right.

Given a 3-digit integer abc none of whose digits is 0, find abc+bca+cab.
example)
123 -> 666 (123+231+312)
'''

def solution():
    a,b,c = list(input())
    return int(''.join([a,b,c])) + int(''.join([b,c,a])) + int(''.join([c,a,b]))
print(solution())
