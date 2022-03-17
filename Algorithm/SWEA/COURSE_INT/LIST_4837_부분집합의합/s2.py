from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range (1, T+1):
    N, K = map(int, input().split())        # N개의 원소의 합 -> K
    ans = 0
    # 1 ~ 12 사이의 N개의 부분집합
    # ex. N: 3 / K: 6 -> 3개의 요소를 원소로 가진 부분집합의 합이 6
    subsets = combinations(range(1, 13), N)
    for subset in subsets:
        if sum(subset) == K:
            ans += 1
    print('#{} {}'.format(tc, ans))