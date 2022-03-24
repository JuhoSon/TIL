import sys
sys.stdin = open('DFS_11724_연결요소의개수.txt')


def dfs(v):
    global connected_cnt
    stack = []
    if not visited[v]:
        stack.append(v)
        connected_cnt += 1
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            for linked_v in graph[v]:
                if not visited[linked_v]:
                    stack.append(linked_v)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        s_idx, e_idx = map(int, input().split())
        graph[s_idx].append(e_idx)
        graph[e_idx].append(s_idx)

    visited = [0 for _ in range(V + 1)]
    connected_cnt = 0
    for s in range(1, V + 1):
        dfs(s)

    print(f'#{tc} {connected_cnt}')