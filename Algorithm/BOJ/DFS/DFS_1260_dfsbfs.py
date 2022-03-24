import sys
from collections import deque
sys.stdin = open('DFS_1260_dfsbfs.txt')


def dfs(start_idx):
    path = []
    stack = [start_idx]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            path.append(v)
            for linked_v in sorted(graph[v], reverse=True):
                if not visited[linked_v]:
                    stack.append(linked_v)
    return path


def bfs(start_idx):
    path = []
    dq = deque([start_idx])
    while dq:
        start_idx = dq.popleft()
        if not visited[start_idx]:
            visited[start_idx] += 1
            path.append(start_idx)
            for linked_v in sorted(graph[start_idx]):
                if not visited[linked_v]:
                    dq.append(linked_v)
    return path


T = int(input())
for tc in range(1, T + 1):
    V, E, start_v = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # zero padding
    for _ in range(E):
        start_idx, end_idx = map(int, input().split())
        graph[start_idx].append(end_idx)
        graph[end_idx].append(start_idx)

    visited = [0 for _ in range(V + 1)]
    dfs_path = dfs(start_v)
    visited = [0 for _ in range(V + 1)]
    bfs_path = bfs(start_v)

    print(*dfs_path)
    print(*bfs_path)
