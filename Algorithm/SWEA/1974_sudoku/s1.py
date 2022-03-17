import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr_T = list(zip(*arr))

    hori = [True if len(set(line)) == 9 else False for line in arr]
    vert = [True if len(set(line)) == 9 else False for line in arr_T]

    start_idx = [(0,0), (0,3), (0,6),
                 (3,0), (3,3), (3,6),
                 (6,0), (6,3), (6,6)]
    area = []
    for x, y in start_idx:
        check_area = set()
        for x_slice in range(3):
            for y_slice in range(3):
                check_area.add(arr[x + x_slice][y + y_slice])
        if len(check_area) == 9:
            area.append(True)
        else:
            area.append(False)

    if sum(hori)==9 and sum(vert)==9 and sum(area)==9:
        result = 1
    else:
        result = 0
    print('#{} {}'.format(tc, result))

