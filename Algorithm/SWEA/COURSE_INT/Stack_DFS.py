import sys
# 인접 행렬 - 반복
def dfs(v):
    stack = [v]                # 시작 정점 stack에 넣어놓고 시작
    while stack:               # stack이 빌때까지 while len(stack) 등도 가능
        v = stack.pop()        # stack의 가장 위에서 정점을 꺼내
        if not visited[v]:     # 아직 방문하지 않았다면
            visited[v] = 1     # 방문 체크
            print(visited)
            for w in range(1, V+1):                     # 모든 정점에 대한 반복을 수행하며
                if G[v][w] == 1 and not visited[w]:     # 해당의 인접 정점이고 아직 방문하지 않았다면
                    stack.append(w)                     # stack에 push
sys.stdin = open('Stack_DFS_input.txt')
V, E = map(int, input().split())                   # V(ertex): 정점 / E(dge): 간선
temp = list(map(int, input().split()))             # 정점에 대한 연결 정보
# V+1 -> 정점을 방문할 때 인덱스 == 정점 번호로 맞추기 위함
G = [[0 for _ in range(V+1)] for _ in range(V+1)]  # 그래프 초기화 (인덱스 관리를 쉽게하기 위해 V+1)
visited = [0 for _ in range(V+1)]                  # 방문 체크 (인덱스 관리를 쉽게하기 위해 V+1)
for i in range(E):                                 # 그래프 초기화 -> 무방향 그래프
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
dfs(1)                                             # 1번 정점부터 dfs 탐색 시작


# 인접 행렬 - 재귀
def dfs(v):
    if not visited[v]:                                          # 방문하지 않았다면 방문 체크
        visited[v] = 1
    print('방문 정점: {}, 방문 체크 확인: {}'.format(v, visited))
    for w in range(1, V+1):                                     # 모든 정점을 돌며
        if G[v][w] == 1 and not visited[w]:                     # 해당 정점(w)이 정점 v의 인접 정점이고 아직 방문하지 않았다면
            dfs(w)                                              # 방문 처리를 위한 재귀 호출 -> 언제 함수가 종료되는지 고민해보세요!
sys.stdin = open('Stack_DFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
dfs(1)


# 인접 행렬 - 재귀(방문처리 시점의 차이)
def dfs(v):
    visited[v] = 1
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

    for w in range(1, V+1):
        if not visited[w] and G[v][w]:
            dfs(w)
sys.stdin = open('Stack_DFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
dfs(1)


# 인접 리스트 - 재귀
def dfs(v):
    visited[v] = 1                                          # 방문 체크
    print('방문 정점: {}, 방문 체크: {}'.format(v, visited))

    for w in G[v]:                                          # 정점 v의 인접 정점 w 중에서
        if not visited[w]:                                  # 아직 방문하지 않은 정점이 있다면
            dfs(w)                                          # 호출
sys.stdin = open('Stack_DFS_input.txt')
V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(1, len(temp), 2):
    G[temp[i-1]].append(temp[i])
    G[temp[i]].append(temp[i-1])
dfs(1)
