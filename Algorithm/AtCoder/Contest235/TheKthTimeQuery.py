'''
Problem Statement
We have a sequence of N numbers: A=(a_1, a_2, ..., a_N).
Process the Q queries explained below.

Query i: You are given a pair of integers (x_i, k_i). 
Let us look at the elements of A one by one from the beginning: 
a_1, a_2, ...Which element will be the k_i-th occurrence of the number x_i?
Print the index of that element, or -1 if there is no such element.
example)
6 8
1 1 2 3 1 2
1 1
1 2
1 3
1 4
2 1
2 2
2 3
4 1
->
1
2
5
-1
3
6
-1
-1
'''
N, Q = map(int, input().split())
A = list(map(int, input().split()))  # length N
num_cnt = {}
for idx, n in enumerate(A):
    if n not in num_cnt:
        num_cnt[n] = []
    num_cnt[n].append(idx)

def solution(num_cnt, *args):
    check_num, cnt = args
    try:
        return num_cnt[check_num][cnt-1] + 1
    except:
        return -1

for _ in range(Q):
    check_num, cnt = map(int, input().split())
    print(solution(num_cnt, check_num, cnt))