import sys
sys.stdin = open('BFS_2644_촌수계산.txt')


def bfs(start):
    q = [start]
    visited[start] = 1
    while q:
        start = q.pop(0)
        for linked_v in graph[start]:
            if not visited[linked_v]:
                q.append(linked_v)
                visited[linked_v] = visited[start] + 1
    return visited[p2]


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    p1, p2 = map(int, input().split())
    m = int(input())

    graph = [[] for _ in range(n + 1)]  # zero padding
    visited = [0 for _ in range(n + 1)]
    for _ in range(m):
        parent, child = map(int, input().split())
        graph[parent].append(child)
        graph[child].append(parent)

    dist = bfs(p1) - 1
    print(f'#{tc} {dist}')