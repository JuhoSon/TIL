# N = int(input())
# # 버텍스는 사람번호, 엣지는 점수, 모든 엣지 돌면서 XOR연산 값이 큰 페어 찾기
# # 1번 : 순열로 모든 가능한 엣지 나열 후 XOR연산으로 max 가져오기
# # 2번 : DFS? 양방향 아니고 한방향이네 ? traceback에서 되돌아가는코드 ?


# graph = dict()
# edges = dict()
# for i in range(2*N-1):
#     # i, j is vertex (person pair)
#     # scores are edges
#     scores = list(map(int, input().split()))
#     for edge_idx, j in enumerate(range(i+1, 2*N)):
#         if i not in graph:
#             graph[i] = []
#         graph[i].append(j)
#         edges[(i,j)] = scores[edge_idx]
# print(graph, edges)

# # visited = []  # init
# # stack = ['A']  # root
# # while stack:
# #     n = stack.pop()
# #     if n not in visited:
# #         visited.append(n)
# #         stack += graph[n]
# # print(visited)


# 아래는 정답코드

N = int(input())
M = 2*N
A = [[0]*(i+1) + [*map(int,input().split())] for i in range(M-1)]
ans = []
stack = [([*range(M)], 0)]
while stack:
    members, score = stack.pop()
    if len(members) == 2:
        i, j = members
        ans.append(score ^ A[i][j])
        continue
    i = members[0]
    for m in range(1, len(members)):
        j = members[m]
        stack.append((members[1:m] + members[m+1:], score ^ A[i][j]))
print(max(ans))