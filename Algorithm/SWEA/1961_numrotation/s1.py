import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rot90 = [[0]*N for _ in range(N)]
    rot180 = [[0]*N for _ in range(N)]
    rot270 = [[0] * N for _ in range(N)]

    for ori_row_idx, row in enumerate(arr):
        for ori_col_idx, ele in enumerate(row):
            new_row_idx = ori_col_idx
            new_col_idx = -1 - (ori_row_idx)
            rot90[new_row_idx][new_col_idx] = ele

    for ori_row_idx, row in enumerate(arr):
        for ori_col_idx, ele in enumerate(row):
            new_row_idx = (N - 1) - ori_row_idx
            new_col_idx = (N - 1) - ori_col_idx
            rot180[new_row_idx][new_col_idx] = ele

    for ori_row_idx, row in enumerate(arr):
        for ori_col_idx, ele in enumerate(row):
            new_row_idx = (N-1) - ori_col_idx
            new_col_idx = ori_row_idx
            rot270[new_row_idx][new_col_idx] = ele

    print('#{}'.format(tc))
    for r90, r180, r270 in zip(rot90, rot180, rot270):
        print(''.join(map(str, r90)), end=' ')
        print(''.join(map(str, r180)), end=' ')
        print(''.join(map(str, r270)), end=' ')
        print()


