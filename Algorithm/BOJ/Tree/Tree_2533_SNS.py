import sys
sys.stdin = open('Tree_2533_SNS.txt')


def dfs(start):
    stack = [start]
    maps[start][0] = 0  # start is not early
    maps[start][1] = 1  # start is early
    visited[start] = 1
    while stack:
        parent = stack[-1]
        leaf_condi = len(tree[parent]) == 0
        children_condi = sum([visited[child] for child in tree[parent]]) == len(tree[parent])
        if children_condi:  # when children all visited
            stack.pop()
            if not leaf_condi:
                for child in tree[parent]:  # update dynamic programming table
                    maps[parent][0] += maps[child][1]
                    maps[parent][1] += min(maps[child][0], maps[child][1])

        for child in tree[parent]:
            if not visited[child]:
                stack.append(child)
                maps[child][0] = 0  # start is not early
                maps[child][1] = 1  # start is early
                visited[child] = 1

# V = int(input())
# E = V - 1
# tree = [[] for _ in range(V + 1)]  # zero padding for using index
# for _ in range(E):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
# visited = [0 for _ in range(V + 1)]
# maps = [[0, 0] for _ in range(V + 1)]  # DP, index 0 : not early case, index 1: early case
# dfs(1)  # 시작점은 상관없음
# print(f'{min(maps[1][0], maps[1][1])}')

T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    E = V - 1
    tree = [[] for _ in range(V + 1)]  # zero padding for using index
    for _ in range(E):
        s, e = map(int, input().split())
        tree[s].append(e)
        # tree[e].append(s)
    visited = [0 for _ in range(V + 1)]
    maps = [[0, 0] for _ in range(V + 1)]  # DP, index 0 : not early case, index 1: early case
    dfs(1)  # 시작점은 상관없음
    print(f'#{tc} {min(maps[1][0], maps[1][1])}')