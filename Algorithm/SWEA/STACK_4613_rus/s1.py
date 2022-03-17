import sys
sys.stdin = open('input.txt')
color_cnt = lambda array, color: len([c for r in array for c in r if c != color])


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    color_need = []
                                                                                 # total range : 0 ~ N-1
    for white_row_idx in range(N-1):                                             # white range : 0 ~ N-2
        for blue_row_idx in range(white_row_idx+1, N):                           # blue_range  : white_idx+1 ~ N-1

            white_need = color_cnt(arr[:white_row_idx], 'W')                # slice range : 0 ~ N-3
            blue_need = color_cnt(arr[white_row_idx:blue_row_idx], 'B')     # slice range : white_idx ~ N-2
            red_need = color_cnt(arr[blue_row_idx:], 'R')                   # slice range : blue_idx ~ N-1

            if white_need > 0 and blue_need > 0 and red_need > 0:
                color_need.append(sum([white_need, blue_need, red_need]))
    print('#{} {}'.format(tc, min(color_need)))
