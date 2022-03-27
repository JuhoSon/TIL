import sys
sys.stdin = open('input.txt')


delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def bfs(start):
    q = [start]
    while q:
        sr, sc = q.pop(0)

        for dr, dc in delta:
            nr = sr+dr
            nc = sc+dc
            if 0 <= nr < N and 0 <= nc < N and not maps[nr][nc]:
                maps[nr][nc] = maps[sr][sc] + 1
                q.append((nr, nc))


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 3:
                end = (i, j)
            elif maps[i][j] == 2:
                start = (i, j)
    maps[start[0]][start[1]] = 1
    maps[end[0]][end[1]] = 0
    bfs(start)

    result = maps[end[0]][end[1]]
    if not result:
        pass
    else:
        result -= 2
    print('#{} {}'.format(tc, result))