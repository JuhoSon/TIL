'''5097 회전
N개의 숫자로 이루어진 수열이 주어진다. 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램을 만드시오.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1 <= T <= 50
다음 줄부터 테스트 케이스의 첫 줄에 N과 M이 주어지고, 다음 줄에 10억 이하의 자연수 N개가 주어진다. 3 <= N <= 20, N <= M <= 1000,
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
'''
# 3
# 3 10
# 5527 731 31274
# 5 12
# 18140 14618 18641 22536 23097
# 10 23
# 17236 31594 29094 2412 4316 5044 28515 24737 11578 7907
from collections import dequefrom collections import dequefrom collections import dequefrom collections import dequefrom collections import deque
from collections import deque
T = int(input()) + 1
for t in range(1, T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        tmp = arr.pop(0)
        arr.append(tmp)
    result = arr.pop(0)
    print('#{} {}'.format(t, result))


'''5105 미로의 거리
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
def bfs(row_idx, col_idx, matrix):
    distance = 0
    drow = [0, 0, 1, -1]
    dcol = [1, -1, 0, 0]
    Q = [(row_idx, col_idx)]
    visited = [[0 for _ in range(len(matrix))] for __ in range(len(matrix))]
    while Q:
        ri, ci = Q.pop(0)
        for d in range(4):  # 상하좌우
            new_row_idx = row_idx + drow[d]
            new_col_idx = col_idx + dcol[d]
            
            if 0 <= new_row_idx <= len(visited) and 0 <= new_col_idx <= len(visited):
                Q.append(new_row_idx, new_col_idx)
                distance += 1
            
            elif matrix[new_row_idx][new_col_idx] == 3:
                distance += 1
                return distance

T = int(input()) + 1
# for t in range(1, T):

N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]
*_, (row_idx, col_idx) = [(ri, ci) for ri, rowArr in enumerate(matrix) for ci, colVal in enumerate(rowArr) if colVal==2]
bfs(row_idx, col_idx)
print('#{} {}'.format(1, 1))


        
