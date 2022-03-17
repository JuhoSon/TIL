import sys
sys.stdin = open('input.txt')


def pal_cnt(arr, pal_size):
    cnt = 0
    for row_str in arr:
        for idx in range(len(row_str) - pal_size + 1):
            slice_str = row_str[idx: idx + pal_size]
            if slice_str == slice_str[::-1]:
                cnt += 1
    return cnt


T = 10
for tc in range(1, T+1):
    pal_size = int(input())
    arr = [input() for _ in range(8)]
    arr_T = list(zip(*arr))
    row_cnt = pal_cnt(arr, pal_size)
    col_cnt = pal_cnt(arr_T, pal_size)

    print('#{} {}'.format(tc, row_cnt + col_cnt))

