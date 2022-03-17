import sys
sys.stdin = open('input.txt')


def div_cnt(N, div):
    cnt = 0
    while N % div == 0:
        N //= div
        cnt += 1
    return N, cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    N, a = div_cnt(N, 2)
    N, b = div_cnt(N, 3)
    N, c = div_cnt(N, 5)
    N, d = div_cnt(N, 7)
    N, e = div_cnt(N, 11)
    print('#{} {} {} {} {} {}'.format(tc, a, b, c, d, e))

