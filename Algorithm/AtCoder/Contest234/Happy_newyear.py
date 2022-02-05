'''
Time Limit: 2 sec / Memory Limit: 1024 MB

Score : 300 points

Problem Statement
Among the positive integers that consist of 0's and 2's when written in base 10, find the K-th smallest integer.

Example
3 -> 22
'''
K = int(input())


def solution(K):
    zerotwo_arr = []
    n = 1
    while len(zerotwo_arr) < K:  # maximum 10**18
        if (set(str(n)) == {"2"}) or (set(str(n)) == {"0","2"}):
            zerotwo_arr.append(n)
        n += 1
    return sorted(zerotwo_arr)[K-1]


print(solution(K))

'''
3 -> 00011
2 -> 00010
3&2 -> 00010
'''