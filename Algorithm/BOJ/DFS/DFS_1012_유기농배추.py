import sys
print(sys.path)
# sys.path.append()
sys.stdin = open('DFS_1012_유기농배추.txt')

delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))


def dfs(x, y):
    global cabbage_cnt
    stack = []
    if maps[(y, x)]:  # cabbage exist
        stack.append((y, x))
        cabbage_cnt += 1
    while stack:
        y, x = stack.pop()
        if maps[(y, x)]:  # cabbage exist
            maps[(y, x)] = 0
            for delta_idx in range(4):
                dy, dx = delta[delta_idx]
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < M and 0 <= new_y < N and maps[(new_y, new_x)]:  # cabbage exist
                    stack.append((new_y, new_x))


T = int(input())
for tc in range(1, T + 1):
    TT = int(input())
    for ttc in range(1, TT + 1):
        M, N, K = map(int, input().split())  # col, row, loc_cnt
        # M : col size -> use x index
        # N : row size -> use y index
        maps = {(y, x): 0 for y in range(N) for x in range(M)}
        for _ in range(K):
            x, y = map(int, input().split())  # col_idx, row_idx
            maps[(y, x)] = 1

        cabbage_cnt = 0
        for y in range(N):
            for x in range(M):
                dfs(x, y)

        print(f'#{ttc} {cabbage_cnt}')