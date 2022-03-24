# import sys
# from collections import deque
# sys.stdin = open('BFS_16236_아기상어.txt')
# delta = list(zip(*[[-1, 1, 0, 0], [0, 0, -1, 1]]))
#
#
# def bfs(start_row, start_col):
#     global shark_size
#     eat_cnt = 0
#
#     start = ' '.join(map(str, [start_row, start_col]))
#     q = deque([start])
#     while q:
#         start = q.popleft()
#         start_row, start_col = map(int, start.split())
#         for dr, dc in delta:
#             togo_row, togo_col = start_row + dr, start_col + dc
#             togo = ' '.join(map(str, [togo_row, togo_col]))
#             if 0 <= togo_row < N and 0 <= togo_col < N and not visited[togo_row][togo_col]:
#
#                 FISH_FLAG = False
#                 togo_size = maps[togo_row][togo_col]
#                 if togo_size > shark_size:
#                     pass
#                 elif togo_size == shark_size:
#                     FISH_FLAG = True
#                 else:  # togo_size < shark_size:
#                     maps[togo_row][togo_col] = 0
#                     FISH_FLAG = True
#                     eat_cnt += 1
#                     if eat_cnt == shark_size:
#                         shark_size += 1
#                         eat_cnt = 0
#
#                 if FISH_FLAG:
#                     visited[togo_row][togo_col] += 1
#                     q.append(togo)
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     maps = [list(map(int, input().split())) for _ in range(N)]
#     visited = [[0 for _ in range(N)] for __ in range(N)]
#     for ri, row in enumerate(maps):
#         for ci, kind in enumerate(row):
#             if kind == 9:
#                 start_row, start_col = ri, ci
#
#     shark_size = 2
#     bfs(start_row, start_col)
#     # print(f'{}')
