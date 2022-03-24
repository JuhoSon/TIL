import sys
from itertools import permutations, combinations
sys.stdin = open('C_nested.txt')

T = int(input())
for tc in range(1, T + 1):
    _ = input()
    n, m = map(int, input().split())
    xw = dict()
    for _ in range(m):
        x, w = map(int, input().split())
        xw[x] = w
    xs = xw.keys()

    min_num = 2*100000
    combi = list(combinations(xs, 2))
    # 모든 경우의 수 중, l_i < l_j < r_j < r_i 만족하는 n개의 쌍 뽑기

    # 그냥 w 기준으로 소팅하면 된다.


    print()