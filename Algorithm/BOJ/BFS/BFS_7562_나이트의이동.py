import sys
from collections import deque
sys.stdin = open('BFS_7562_나이트의이동.txt')


delta = list(zip(*[[-1, 1, 2, 2, 1, -1, -2, -2],  # row
                   [2, 2, 1, -1, -2, -2, -1, 1]]))  # col -> (row, col) throgh zip


def bfs(start_row, start_col, end_r, end_c):
    start = ' '.join(map(str, [start_row, start_col]))
    q = deque([start])
    while q:
        start = q.popleft()
        start_row, start_col = map(int, start.split())
        if (start_row, start_col) == (end_r, end_c):
            break
        for dr, dc in delta:
            togo_row, togo_col = start_row + dr, start_col + dc
            togo = ' '.join(map(str, [togo_row, togo_col]))
            if 0 <= togo_row < l and 0 <= togo_col < l and not maps[(togo_row, togo_col)]:
                maps[(togo_row, togo_col)] = maps[(start_row, start_col)] + 1
                q.append(togo)


T = int(input())
for tc in range(1, T + 1):
    l = int(input())  # 체스판 한 변의 길이 (l x l)
    maps = {(row, col): 0 for row in range(l) for col in range(l)}
    cur_r, cur_c = map(int, input().split())
    goal_r, goal_c = map(int, input().split())

    bfs(cur_r, cur_c, goal_r, goal_c)
    depth = maps[(goal_r, goal_c)]
    print(f'{depth}')