import sys
sys.stdin = open('input2.txt')


def pal_max(arr):
    max_num = 0
    for str_line in arr:
        for slice_num in range(1, 101):
            for idx in range(len(str_line) - slice_num + 1):
                slice_str = str_line[idx: idx + slice_num]
                if (slice_str == slice_str[::-1]) and slice_num > max_num:
                    max_num = slice_num
    return max_num


T = 10
for tc in range(1, T+1):
    _ = input()
    arr = [input() for _ in range(100)]
    arr_T = list(zip(*arr))
    row_max = pal_max(arr)
    col_max = pal_max(arr_T)

    print('#{} {}'.format(tc, max(row_max, col_max)))