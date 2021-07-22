'''4874 Forth
Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
3 4 + .
Forth에서는 동작은 다음과 같다.
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.
Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
다음은 Forth 연산의 예이다.
코드 -> 출력
4 2 / . -> 2
4 3 - . -> 1
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.
[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.
'''
def doit(x, a, b):
    if x == '/':
        return int(a)/int(b)
    elif x == '*':
        return int(a)*int(b)
    elif x == '+':
        return int(a)+int(b)
    elif x == '-':
        return int(a)-int(b)


T = int(input()) + 1
for t in range(1, T):
    li = input().split()
    stack = [li[0]]
    for s in li[1:]:
        if s == '.':
            if len(stack) != 1:  # 연산이 덜 끝났을 때
                result = 'error'
                break
            else:
                result = int(float(stack.pop(-1)))
        elif not s.isdigit():
            if len(stack) < 2:
                result = 'error'
                break
            else:
                sec = stack.pop(-1)
                fir = stack.pop(-1)
                stack.append(str(int(float(doit(s, fir, sec)))))
        else:
            stack.append(s)
    print('#{} {}'.format(t, result))


'''4875 미로
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
주어진 미로 밖으로는 나갈 수 없다.
다음은 5x5 미로의 예이다.
13101
10101
10101
10101
10021
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.'''
def dfs(x, y, maze):
    maze[x][y] = -1
    for dx, dy in zip([0, 0, 1, -1], [1, -1, 0, 0]):
        if (0 <= x + dx <= len(maze)-1) and (0<=y+dy<=len(maze)-1):
            if (maze[x+dx][y+dy] != -1) and (maze[x+dx][y+dy] != 1):
                dfs(x+dx, y+dy, maze)

T = int(input()) + 1
for t in range(1, T):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    [(startx, starty)] = [(r, c) for r, rows in enumerate(maze) 
    for c, value in enumerate(rows) if value==2]

    dfs(startx, starty, maze)
    if True in [True for rows in maze if 3 in rows]:
        result = 0
    else:
        result = 1
    print('#{} {}'.format(t, result))


'''4880 토너먼트 카드게임
사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다.
그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다. (i+j)//2, (i+j)//2+1
두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다.
다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.
N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.
'''
# 3
# 4
# 1 3 2 1
# 6
# 2 1 1 2 3 3
# 7
# 1 3 3 3 1 1 3
def merge(arr, i, j):
    if arr[i-1] == arr[j-1]:  # 무승부
        return i
    elif (arr[i-1] == 1) and (arr[j-1] == 2):
        return j
    elif (arr[i-1] == 2) and (arr[j-1] == 3):
        return j
    elif (arr[i-1] == 3) and (arr[j-1] == 1):
        return j
    else:
        return i
def dc(i, j):  # divide and conquer
    global arr
    if len(arr[i-1:j]) <= 1:
        return i
    q = (i+j)//2
    i = dc(i, q)
    j = dc(q+1, j)
    tmp = merge(arr, i, j)
    return merge(arr, i, j)

T = int(input()) + 1
for t in range(1, T):
    N = int(input())
    card = list(map(int, input().split()))
    arr = card
    result = dc(1, len(card))
    print('#{} {}'.format(t, result))


'''4881 배열 최소 합
NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
예를 들어 다음과 같이 배열이 주어진다.
2 1 2
5 8 5
7 2 2
이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.
[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10
[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.'''
# 3
# 3
# 2 1 2
# 5 8 5
# 7 2 2
# 3
# 9 4 7
# 8 6 5
# 5 3 7
# 5
# 5 2 1 1 9
# 3 3 8 3 1
# 9 2 8 8 6
# 1 5 7 8 3
# 5 5 4 6 8
T = int(input()) + 1
for t in range(1, T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    matCol = [[], [], []]
    for firstValue, secondValue, thirdValue in matrix:
        matCol[0].append(firstValue)
        matCol[1].append(secondValue)
        matCol[2].append(thirdValue)
    perSet = {''.join(map(str, [f, s, t])) for f in matCol[0]
            for s in matCol[1] for t in matCol[2]}


    def calMin(x): return sum(list(map(int, list(x))))


    sumSet = [calMin(p) for p in perSet]
    print('#{} {}'.format(t, min(sumSet)))
