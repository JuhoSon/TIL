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
    distance = [[0 for _ in range(len(matrix))] for __ in range(len(matrix))]
    while Q:
        ri, ci = Q.pop(0)
        visited[ri][ci] = 1
        for d in range(4):  # 상하좌우
            new_row_idx = ri + drow[d]
            new_col_idx = ci + dcol[d]
            if (0 <= new_row_idx < len(visited)) and (0 <= new_col_idx < len(visited)) and \
                (visited[new_row_idx][new_col_idx] == 0) and (matrix[new_row_idx][new_col_idx]!=1):
                Q.append((new_row_idx, new_col_idx))
                distance[new_row_idx][new_col_idx] = distance[ri][ci] + 1

                if matrix[new_row_idx][new_col_idx] == 3:
                    return distance[ri][ci]


T = int(input()) + 1
for t in range(1, T):
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    *_, (row_idx, col_idx) = [(ri, ci) for ri, rowArr in enumerate(matrix) for ci, colVal in enumerate(rowArr) if colVal==2]
    result = bfs(row_idx, col_idx, matrix)
    result = 0 if result==None else result
    print('#{} {}'.format(t, result))


'''5099 피자굽기
N개의 피자를 동시에 구울 수 있는 화덕이 있다. 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈의 양은 피자마다 다르다.
1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때, 치즈의 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
주어진 조건에 따라 피자를 구울 때, 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램을 작성하시오.
- 피자는 1번위치에서 넣거나 뺄 수 있다.  # Queue
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.
3<=N<=20, N<=M<=100, 1<=Ci<=20
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 번호를 출력한다.
'''
T = int(input()) + 1
# for t in range(1, T):
    # print('#{} {}'.format(t, result))


N, M = map(int, input().split())
Ci = list(map(int, input().split()))
pizza = []
for _ in range(N):  # init
    pizza.append(Ci.pop(0))
while Ci:
    checkPizza = pizza.pop(0)
    checkPizza = checkPizza//2
    if checkPizza == 0:
        pizza.append(Ci.pop(0))
    else:
        pizza.append(checkPizza)
