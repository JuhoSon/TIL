import sys
"""
1. bfs - 인접 행렬 구현 - 리스트로 큐 구현
"""
def bfs(v):
    Q = [v]                                          # Q 생성 & 시작 정점 넣어놓고
    while Q:                                         # Q가 빌때까지
        v = Q.pop(0)                                 # Q에서 정점을 꺼내고
        if not visited[v]:                           # 해당 정점에 방문하지 않았다면
            visited[v] = 1                           # 방문체크
            print('{}번 정점에 방문'.format(v))
            for w in range(1, V+1):                  # 모든 정점 반복을 돌며
                if G[v][w] == 1 and not visited[w]:  # 해당 정점의 인접 정점이고 방문 안했다면
                    Q.append(w)                      # Q에 넣자
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())                     # V(ertex), E(dge)
temp = list(map(int, input().split()))               # 간선 정보 초기화
G = [[0 for _ in range(V+1)] for _ in range(V+1)]    # Graph 초기화
for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
visited = [0] * (V+1)                                # 방문 표시 초기화
bfs(1)                                               # bfs 탐색 시작


"""
1. bfs - 인접 행렬 구현 - 포인터로 구현
"""
def bfs(v):
    Q = [0] * V                 # 배열 초기화
    front = rear = -1           # front & rear 인덱스 초기화
    rear += 1                   # rear 늘리고
    Q[rear] = v                 # 시작값 세팅
    visited[v] = 1              # 방문 체크

    while front != rear:
        front += 1
        v = Q[front]
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:
                rear += 1
                Q[rear] = w
                visited[w] = 1
                print(*visited)
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(len(temp)//2):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
visited = [0] * (V+1)
bfs(1)


"""
2. bfs - 인접 리스트 구현
"""
def bfs(v):
    Q = [v]
    while Q:
        v = Q.pop(0)
        if v not in visited:              # 방문 리스트 안에 없으면
            visited.append(v)             # 방문 처리
            for w in G[v]:                # v의 인접 정점 돌며
                if w not in visited:      # 해당 정점이 아직 방문하지 않은 곳이라면
                    Q.append(w)           # Q에 넣자
    return ' -> '.join(map(str, visited))
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())        # 정점 & 간선
temp = list(map(int, input().split()))  # 정점 정보
G = [[] for _ in range(V+1)]            # 그래프 초기화
for i in range(len(temp)//2):           # 그래프 생성
    # 0, 2, 4, 6 ...        1, 3, 5, 7 ...
    G[temp[i*2]].append(temp[i*2+1])
visited = []                            # (이전과는 다른 방식의) 방문 체크
print(bfs(1))


"""
3. bfs - 인접 딕셔너리 구현
"""
def bfs(v):
    not_visited.append(v)               # 방문하지 않은 리스트에 추가
    while not_visited:                  # 모든 정점을 다 탐색할 때까지 진행
        v = not_visited.pop(0)          # 리스트의 가장 앞에 있는 정점을 뽑아
        if v not in visited:            # 해당 정점이 방문하지 않은 곳이라면
            visited.append(v)           # 방문 체크
            not_visited.extend(G[v])    # 해당 정점과 연결된 인접 정점을 방문하지 않은 리스트에 연결
    return ' -> '.join(map(str, visited))
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = {}                          # 연결 정점 정보 그래프 생성(무방향 그래프) -> 각 정점에 필요한 정보를 넣기 위한 준비
for i in range(1, V+1):
    G[i] = []
for i in range(0, len(temp), 2):
    G[temp[i]].append(temp[i+1])
    G[temp[i+1]].append(temp[i])
print(G)
# 다른 방식의 방문체크
visited = []
not_visited = []
print(bfs(1))


"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""
def bfs(v):
    Q = [v]        # Q 생성 & 바로 정점 정보 추가
    visited[v] = 1 # 방문 처리

    while Q:
        v = Q.pop(0)
        for w in range(V+1):
            if G[v][w] == 1 and not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)

    max_dist = max(visited)
    # max_dist_vertex = visited.index(max_dist)
    return max_dist-1
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    G[temp[2*i]][temp[2*i+1]] = 1
    G[temp[2*i+1]][temp[2*i]] = 1
visited = [0 for _ in range(V+1)]
print(bfs(1))


"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""
def bfs(v):
    Q = [0] * V                             # 정점 정보를 담기 위한 Queue
    front = rear = -1                       # front & rear 초기화
    rear += 1                               # 시작점 enQueue를 위한 포인터
    Q[rear] = v                             # enQueue
    visited[v] = 1                          # 방문 처리
    print(*visited)

    while front != rear:                    # Queue가 비어있지 않으면
        front += 1                          # deQueue를 위한 포인터 생성
        v = Q[front]                        # 이후에 deQueue
        for w in range(1, V+1):
            if G[v][w] and not visited[w]:  # v에 인접하고 아직 방문하지 않은 곳이라면
                rear += 1                   # enQueue를 위해 값을 하나 증가 시키고
                Q[rear] = w                 # 해당 위치(rear)에 인접 정점(w)을 추가
                visited[w] = visited[v] + 1 # 방문처리(거리정보) 갱신
                print(*visited)
    return max(visited)-1
sys.stdin = open('Queue_BFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
for i in range(E):
    n1, n2 = temp[2*i], temp[2*i+1]
    G[n1][n2] = 1
    G[n2][n1] = 1
visited = [0] * (V+1)
print(f'1번 정점으로부터 가장 멀리 떨어진 정점은 {bfs(1)}만큼 떨어져 있습니다.')
