import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fly_die_arr = []
    for row_idx in range(N - M + 1):
        for col_idx in range(N - M + 1):
            fly_die = 0
            for row_slice in range(M):
                for col_slice in range(M):
                    fly_die += arr[row_idx+row_slice][col_idx+col_slice]
            fly_die_arr.append(fly_die)

    print('#{} {}'.format(tc, max(fly_die_arr)))

