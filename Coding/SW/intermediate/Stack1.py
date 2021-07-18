# '''4869 종이붙이기
# 어린이 알고리즘 교실의 선생님은 경우의 수 놀이를 위해, 그림처럼 가로x세로 길이가 10x20, 20x20인 직사각형 종이를 잔뜩 준비했다.
# 그리고 교실 바닥에 20xN 크기의 직사각형을 테이프로 표시하고, 이 안에 준비한 종이를 빈틈없이 붙이는 방법을 찾아보려고 한다. N이 30인 경우 다음 그림처럼 종이를 붙일 수 있다.
# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만든 표시한 영역을 몇 개나 만들어야 되는지 계산하는 프로그램을 만드시오. 직사각형 종이가 모자라는 경우는 없다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 N이 주어진다. 10≤N≤300, N은 10의 배수
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# '''
# # 3
# # 30
# # 50
# # 70
# # <기본생각>  1, 2의 합으로 N을 만드는 모든 경우의 수
# T = int(input())  # test case number
# # two_cnt = N // 2
# # one_cnt = N % 2
# # init_list = list(map(str, [2] * two_cnt + [1] * one_cnt))
# # subset_idx = [idx for idx, _ in enumerate(init_list) if _ == "2"]
# # subset = []
# # for i in range(2**len(subset_idx)):
# #     flag = bin(i)[2:].zfill(len(subset_idx))
# #     sub = [subset_idx[j] for j in range(len(subset_idx)) if flag[j] == '1']
# #     subset.append(sub)
# # whole_case = {''.join(init_list)}
# # for case in subset:
# #     tmp = list(init_list)
# #     for pop_idx in case:
# #         tmp.pop(pop_idx)
# #         tmp.insert(pop_idx, "1")
# #         tmp.insert(pop_idx, "1")
# #     whole_case.add(''.join(tmp))  # 기본 생각은 틀려먹었음 ㅜㅜ
# # <코드치팅> dynamic programming 으로 ! rod cutting랑 비슷하다고 생각하면 될듯
# def dp(num):
#     if not num:
#         return 0
#     if num == 1:
#         return 1
#     if num == 2:
#         return 3
#     return dp(num-1) + 2*dp(num-2)


# for t in range(1, T+1):
#     N = int(int(input())/10)  # 10의 배수 = 20(가로) * N(세로) 의 전체 크기
#     print('#{} {}'.format(t, dp(N)))


# '''4866 괄호검사
# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
# '''
# # <first try>
# def check_bracket():
#     test_str = ''.join([_ for _ in input() if _ in '{}()']) # test string
#     bra_dic = {'}': '{', ')': '(', ']':'[', '(':'', '{':'', '[':''}
#     stack = []
#     for s in test_str:
#         if len(stack) == 0:
#             stack.append(s)
#         else:
#             if bra_dic[s] == stack[-1]:
#                 stack.pop(-1)
#             else:
#                 stack.append(s)
#     if len(stack) == 0:
#         flag = 1
#     else:
#         flag = 0
#     return flag


# T = int(input())  # test case number
# for _ in range(T):
#     print('#{} {}'.format(_+1, check_bracket()))


'''4871 그래프 경로
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경로를 찾는 경우, 경로가 존재하므로 1을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5≤V≤50, 4≤E≤1000
테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 출발 도착 노드로 간선 정보가 주어진다.
E개의 줄 이후에는 경로의 존재를 확인할 출발 노드 S와 도착노드 G가 주어진다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# 1 (T)
# 6 5 (V, E)
# 1 4 (Start, End)
# 1 3
# 2 3
# 2 5
# 4 6
# 1 6 (S, G)
def dfs(start_idx, visited, grap):
    visited[start_idx] = True
    for node in grap[start_idx]:
        if visited[node] != True:
            dfs(node, visited, grap)
        
        
T = int(input())
for t in range(1, T+1):
    V, E = list(map(int, input().split(' ')))
    grap = dict()
    for _ in range(E):
        start, end = list(map(int, input().split(' ')))
        if start not in grap:
            grap[start] = []
        if end not in grap:
            grap[end] = []
        grap[start].append(end)
    S, G = list(map(int, input().split(' ')))
    visited = {k:False for k in grap.keys()}
    print(visited, grap)
    flag = 0
    if visited[S] == True:
        flag = 1
    print(visited, grap)
    print('#{} {}'.format(t, flag))


# def dfs(node_index, visited, nodes):
#     visited[node_index] = 1
#     for node in nodes[node_index]:
#         if visited[node] != 1:
#             dfs(node, visited, nodes)


# for t in range(int(input())):
#     V, E = map(int, input().split())
#     nodes = [[] for _ in range(V+1)]
#     for _ in range(E):
#         start, end = map(int, input().split())
#         nodes[start].append(end)
#     S, G = map(int, input().split())
#     visited = [0 for _ in range(V+1)]
#     print(nodes, visited)
#     dfs(S, visited, nodes)
#     answer = 0
#     if visited[G] == 1:
#         answer = 1
#     print(nodes, visited)
#     print('#{} {}'.format(t+1, answer))
# '''4873 반복문자 지우기
# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
# 다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤ 50
# 다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.
# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.
# '''
# # 3
# # ABCCB
# # NNNASBBSNV
# # UKJWHGGHNFTCRRCTWLALX
# T = int(input())
# for t in range(1, T+1):
#     inp = list(input())
#     stack = []
#     stack.append(inp[0])
#     for s in inp[1:]:
#         if len(stack) >= 1:
#             if stack[-1] == s:
#                 stack.pop(-1)
#             else:
#                 stack.append(s)
#         else:
#             stack.append(s)
#     print('#{} {}'.format(t, len(stack)))
