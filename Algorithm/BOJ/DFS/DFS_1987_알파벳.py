import sys
sys.stdin = open('DFS_1987_알파벳.txt')

delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def dfs(r, c):
    global ans
    visited = set()
    stack = [(r, c)]
    while stack:

        r, c = stack[-1]

        if maps[r][c] not in visited:

            visited.add(maps[r][c])
            for d_idx in range(4):
                dx, dy = delta[d_idx]
                new_r = r + dy
                new_c = c + dx
                if 0 <= new_c < C and 0 <= new_r < R and maps[new_r][new_c] not in visited:
                    stack.append((new_r, new_c))
        else:
            cnt = len(visited)
            ans = max(cnt, ans)
            visited.remove(maps[r][c])
            stack.pop()


def dfs_rec(r, c, cnt):
    global ans
    global visited_rec
    ans = max(ans, cnt)
    for d_idx in range(4):
        dx, dy = delta[d_idx]
        new_r = r + dy
        new_c = c + dx
        if 0 <= new_c < C and 0 <= new_r < R and maps[new_r][new_c] not in visited_rec:
            visited_rec.add(maps[new_r][new_c])
            dfs_rec(new_r, new_c, cnt + 1)
            visited_rec.remove(maps[new_r][new_c])


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    maps = [list(input()) for _ in range(R)]
    ans = 0
    dfs(0, 0)
    print(f'#{tc} {ans}')

    ans = 0
    visited_rec = {maps[0][0]}
    dfs_rec(0, 0, 1)
    print(f'#{tc} {ans}')