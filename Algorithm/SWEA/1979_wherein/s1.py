import sys
sys.stdin = open('input.txt')


def line_blank(line_arr):
    start_idx = 0
    end_idx = 0
    FLAG = False

    blank_arr = set()
    for idx, val in enumerate(line_arr):
        if val == 0:
            if FLAG == True:
                blank_arr.add(range(start_idx, end_idx+1))
                FLAG = False
            start_idx, end_idx = idx, idx
        else:
            if FLAG == False:
                FLAG = True
                start_idx = idx
            end_idx = idx
    blank_arr.add(range(start_idx, end_idx + 1))
    return list(map(len, blank_arr))


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(zip(*arr))
    # white: 1, black: 0

    hori = [1 for line in arr for size in line_blank(line) if size==K]
    vert = [1 for line in arr_T for size in line_blank(line) if size==K]
    print('#{} {}'.format(tc, sum(hori) + sum(vert)))

