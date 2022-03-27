import sys
from collections import deque
sys.stdin = open('BFS_16236_아기상어.txt')
delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def update_size():
    global shark_size
    global eat_cnt
    eat_cnt += 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0


def bfs(start):
    path = []

    q = [start]
    visited[start[0]][start[1]] = 1
    while q:
        sr, sc = q.pop(0)
        for dr, dc in delta:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] += visited[sr][sc] + 1
                fish_size = maps[nr][nc]
                if fish_size > shark_size:
                    continue
                elif fish_size == shark_size or fish_size == 0:
                    q.append((nr, nc))
                else:  # togo_size < shark_size:
                    path.append((visited[nr][nc] - 1, nr, nc))

    if path:
        return sorted(path, key=lambda x: (x[0], x[1], x[2]))[0]  # distance, row, column order
    else:
        return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    for ri, row in enumerate(maps):
        for ci, kind in enumerate(row):
            if kind == 9:
                start = (ri, ci)
    maps[start[0]][start[1]] = 0

    shark_size = 2
    eat_cnt = 0

    total_distance = 0
    while sum([sum(_) for _ in maps]):
        visited = [[0 for _ in range(N)] for __ in range(N)]
        next = bfs(start)
        if next:
            dist, nr, nc = next
            total_distance += dist
            start = (nr, nc)
            update_size()
            maps[nr][nc] = 0
        else:
            break

    print(f'#{tc} {total_distance}')
