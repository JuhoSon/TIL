import sys
sys.stdin = open('input.txt')


def dp(num):
    if not num:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 3
    else:
        return dp(num-1) + 2*dp(num-2)


T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, dp(N)))

