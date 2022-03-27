import sys
sys.stdin = open('input.txt')
delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def bfs(start):
    q = [start]
    while q:
        sr, sc = q.pop()
        for dr, dc in delta:
            nr, nc = sr+dr, sc+dc
            if 0 <= nr < 16 and 0 <= nc < 16 and not maze[nr][nc]:
                maze[nr][nc] = maze[sr][sc] + 1
                q.append((nr, nc))


T = 10
for tc in range(1, T+1):
    _ = input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    for ri in range(16):
        for ci in range(16):
            if maze[ri][ci] == 2:
                start = (ri, ci)
                maze[ri][ci] = 1
            if maze[ri][ci] == 3:
                end_r, end_c = ri, ci
                maze[ri][ci] = 0

    bfs(start)

    if not maze[end_r][end_c]:  # not visited
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 1))