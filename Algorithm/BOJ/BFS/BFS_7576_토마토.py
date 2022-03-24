import sys
from collections import deque
sys.stdin = open('BFS_7576_토마토.txt')


delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def bfs(starts):
    q = deque()
    for (start_row, start_col) in starts:
        start = ' '.join(map(str, [start_row, start_col]))
        q.append(start)
    while q:
        start = q.popleft()
        start_row, start_col = map(int, start.split())
        for dr, dc in delta:
            togo_row, togo_col = start_row + dr, start_col + dc
            if 0 <= togo_row < rows and 0 <= togo_col < cols and not maps[togo_row][togo_col]:
                maps[togo_row][togo_col] = maps[start_row][start_col] + 1
                togo = ' '.join(map(str, [togo_row, togo_col]))
                q.append(togo)


def check_condition():
    max_val = -1
    for r_idx, r in enumerate(maps):
        for c_idx, status in enumerate(r):
            if status == 0:
                return -1
            elif status > max_val:
                max_val = status
    return max_val - 1  # consider first tomato status


T = int(input())
for tc in range(1, T + 1):
    cols, rows = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(rows)]
    starts = []
    for r_idx, r in enumerate(maps):
        for c_idx, status in enumerate(r):
            if status == 1:
                starts.append((r_idx, c_idx))
    bfs(starts)
    max_val = check_condition()
    print(f'{max_val}')