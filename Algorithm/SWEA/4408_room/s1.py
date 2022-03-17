import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    odds = [_ for _ in range(1, 401) if _ % 2 == 1]
    room_idx = {room_num:idx for idx, room_num in enumerate(odds)}
    even = [_ for _ in range(1, 401) if _ % 2 == 0]
    tmp = {room_num:idx for idx, room_num in enumerate(even)}
    room_idx.update(tmp)

    total_time = [0]*200

    for start, end in arr:
        if start > end:
            start, end = end, start
        start_idx = room_idx[start]
        end_idx = room_idx[end]
        for idx in range(start_idx, end_idx+1):
            total_time[idx] += 1

    print('#{} {}'.format(tc, max(total_time)))
