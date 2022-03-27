import sys
sys.stdin = open('Tree_2533_SNS.txt')


def dfs(start):
    stack = [start]
    while stack:
        start = stack.pop()
        visited[start] = 1
        maps[start][0] = 0  # start is not early
        maps[start][1] = 1  # start is early

        for linked_v in tree[start]:
            if not visited[linked_v]:
                stack.append(linked_v)
            else:  # leaf node
                maps[start][0] += maps[linked_v][1]
                maps[start][1] += min(maps[linked_v][0], maps[linked_v][1])


# V = int(input())
# E = V - 1
# tree = [[] for _ in range(V + 1)]  # zero padding for using index
# for _ in range(E):
#     s, e = map(int, input().split())
#     tree[s].append(e)
#     tree[e].append(s)
# visited = [0 for _ in range(V + 1)]
# needs = dfs(1)  # 시작점은 상관없음
# print(f'#{len(needs)}')

T = int(input())
for tc in range(1, T + 1):
    V = int(input())
    E = V - 1
    tree = [[] for _ in range(V + 1)]  # zero padding for using index
    for _ in range(E):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s)
    visited = [0 for _ in range(V + 1)]
    maps = [[0, 0] for _ in range(V + 1)]  # DP, index 0 : not early case, index 1: early case
    dfs(1)  # 시작점은 상관없음
    print(f'#{tc} {min(maps[1][0], maps[1][1])}')