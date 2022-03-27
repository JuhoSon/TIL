import sys
sys.stdin = open('Tree_11725_트리의부모찾기.txt')


def dfs(root):
    stack = [root]
    visited[root] = 1
    while stack:
        start = stack.pop()

        for linked_v in tree[start]:
            if not visited[linked_v]:
                visited[linked_v] = start
                stack.append(linked_v)


T = int(input())
for tc in range(1, T + 1):
    root = 1
    V = int(input())
    E = V - 1
    tree = [[] for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        tree[s].append(e)
        tree[e].append(s)
    visited = [0 for _ in range(V + 1)]
    dfs(root)

    for num in visited[2:]:
        print(num)