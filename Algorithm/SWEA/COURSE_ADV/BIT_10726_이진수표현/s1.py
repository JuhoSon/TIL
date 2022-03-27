import sys
sys.stdin = open('input.txt')


def check(d):
    for bit in range(N):
        if not d & (1<<bit):
            return 'OFF'

    return 'ON'


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = check(M)
    print(f'#{tc} {result}')