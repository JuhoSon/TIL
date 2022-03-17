import sys
sys.stdin = open('BOJ_2606_virus.txt')


def dfs(start_node_idx):
    linked_com_cnt = 0

    stack = [start_node_idx]
    visited = [False for _ in range(V + 1)]  # zero padding
    visited[start_node_idx] = True

    while stack:
        start_idx = stack.pop()

        end_idx = graph[start_idx]
        for i in end_idx:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                linked_com_cnt += 1
    return linked_com_cnt


V = int(input())  # vertex count
E = int(input())  # edge count
graph = [[] for _ in range(V + 1)]  # zero padding
for _ in range(E):
    start_idx, end_idx = map(int, input().split())
    
    # adjcent list, undirected graph
    graph[start_idx].append(end_idx)
    # graph[end_idx].append(start_idx)

virus_cnt = dfs(1)
print(virus_cnt)