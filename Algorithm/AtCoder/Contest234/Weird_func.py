'''Time Limit : 2sec/ Memory Limit : 1024MB
Problem Statement
Let us define a function f as f(x)=x x^2+2x+3.
Given an integer t, find f(f(f(t)+t)+f(f(t))).
Here, it is guaranteed that the answer is an integer not greater than 2x10^9.

Constraints
t is an integer between 0 and 10 (inclusive).
Example
0 -> 1371
3 -> 722502
10 -> 1111355571
'''

f_x = lambda x: x**2 + 2*x + 3
def solution(x):
    return f_x( (f_x( (f_x(x)+x) ) ) + f_x(f_x(x)))

inp = int(input())
print(solution(inp))
