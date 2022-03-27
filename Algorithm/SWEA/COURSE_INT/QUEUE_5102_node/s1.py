import sys
sys.stdin = open('input.txt')


def bfs(s_idx):
    q = [s_idx]
    while q:
        s_idx = q.pop(0)
        for linked_idx in graph[s_idx]:
            if not visited[linked_idx]:
                visited[linked_idx] = visited[s_idx] + 1
                q.append(linked_idx)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = dict()
    for _ in range(E):
        S, G = map(int, input().split())
        if S not in graph:
            graph[S] = []
        if G not in graph:
            graph[G] = []
        graph[S].append(G)
        graph[G].append(S)
    visited = [0 for _ in range(V + 1)]

    S, G = map(int, input().split())
    bfs(S)
    dist = visited[G]

    print('#{} {}'.format(tc, dist))