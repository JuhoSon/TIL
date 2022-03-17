def sub(n):
    subsets = []
    nodes = [_ for _ in range(n)]
    for bit in range(1 << len(nodes)):
        subset = []
        # get subset
        for idx in range(len(nodes)):
            if bit & (1 << idx):
                subset.append(nodes[idx])
        if len(subset) == 3:
            subsets.append(subset)
    return subsets


def cal_path(S, E, tree):  # start, end
    visited = [0] * (len(tree)+1)                  # 방문 체크 리스트(인덱스 관리를 위해 V+1)
    stack = [S]                                  # 출발 지점을 스택에 넣어놓고 시작

    path = -1
    while stack:                                 # stack이 빌 때까지 반복 (모든 정점 방문 완료)
        v = stack.pop()                          # 먼저 스택에서 정점을 하나 꺼내
        if not visited[v]:                       # 그 정점이 방문하지 않은 정점이라면
            visited[v] = 1                       # 방문 처리를 하고
            path += 1
            for v in tree[v]:                   # 해당 정점에 연결된 다른 정점(인접 정점)을 돌며
                if v == E:
                    path += 1
                    return path
                if not visited[v]:               # 만약 그 곳이 방문하지 않은 곳이라면
                    stack.append(v)              # stack에 추가
    return path


def solution(n, edges):
    answer = 0

    # build tree
    tree = {}
    for edge in edges:
        start_node = edge[0]
        end_node = edge[1]
        if start_node not in tree:
            tree[start_node] = []
        if end_node not in tree:
            tree[end_node] = []
        tree[start_node].append(end_node)
        tree[end_node].append(start_node)
    
    # all cases
    cases = sub(n)
    
    # cal path
    for case in cases:
        i, j, k = case
        path_ij = cal_path(i, j, tree)
        path_jk = cal_path(j, k, tree)
        path_ik = cal_path(i, k, tree)
        print(path_ij, path_jk, path_ik)
        if path_ij + path_jk == path_ik:
            answer += 1

    return answer

a = 16
s = solution(5, [[0,1],[0,2],[1,3],[1,4]])
print(a, s)

