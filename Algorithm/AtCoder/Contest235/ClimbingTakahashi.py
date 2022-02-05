'''
Problem Statement
There are N platforms arranged in a row. The height of the i-th platform from the left is H_i.
Takahashi is initially standing on the leftmost platform.

Since he likes heights, he will repeat the following move as long as possible.

If the platform he is standing on is not the rightmost one, and the next platform to the right has a height greater than that of the current platform, step onto the next platform.
Find the height of the final platform he will stand on.
example)
5
1 5 10 4 2
->
10
'''
N = int(input())
heights = list(map(int, input().split()))
max_h = 0  # constraints 1 <= height
for h in heights:
    if h > max_h:
        max_h = h
    else:
        break
print(max_h)