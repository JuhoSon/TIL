'''
Problem Statement
We have a positive integer a. Additionally, there is a blackboard with a number written in base 10.
Let x be the number on the blackboard. Takahashi can do the operations below to change this number.

Erase x and write x multiplied by a, in base 10.
See x as a string and move the rightmost digit to the beginning. This operation can only be done when x≥10 and x is not divisible by 10.

For example, when a=2,x=123, Takahashi can do one of the following.

Erase x and write x×a=123×2=246.
See x as a string and move the rightmost digit 3 of 123 to the beginning, changing the number from 123 to 312.
The number on the blackboard is initially 1. What is the minimum number of operations needed to change the number on the blackboard to N? If there is no way to change the number to N, print −1.

example)
3 72 -> 4
'''

# a, N = map(int, input().split())
# init = 1
# result_cnt = 0

# way1 = lambda x: x*a
# way2 = lambda x: int(str(x[-1]) + str(x[:-1]))

# # while init != N:
# while result_cnt <= 120:
    
#     if (init >= 10) and (init % 10 != 0):

#     result_cnt += 1
# print(result_cnt)

# BFS 공부하고 다시 도전..