"""
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 '부모 -> 자식' 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위/중위/후회 순회하여 정점의 번호를 출력하시오.
13 -> 정점의 개수
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

참고)
1) Tree에서는 정점의 개수만 알려줘도 간선 정보를 알 수 있음 (정점이 V개 일 때 간선은 V-1개)
2) 트리는 1차원 배열 / 2차원 배열 모두 표현이 가능하지만 이 문제는 2차원으로 접근 해보자
"""
# 전위 순회 (V -> L -> R)
def pre_order(node):
    global cnt
    if node != 0:
        cnt += 1                           # 방문한 정점의 개수 체크
        print('{}'.format(node), end=' ')  # 노드
        pre_order(tree[node][0])           # 왼쪽
        pre_order(tree[node][1])           # 오른쪽

# 중위 순회 (L -> V -> R)
def in_order(node):
    if node != 0:
        in_order(tree[node][0])             # 왼쪽
        print('{}'.format(node), end=' ')   # 노드
        in_order(tree[node][1])             # 오른쪽

# 후위 순회 (L -> R -> V)
def post_order(node):
    if node != 0:
        post_order(tree[node][0])           # 왼쪽
        post_order(tree[node][1])           # 오른쪽
        print('{}'.format(node), end=' ')   # 노드

def print_tree():
    # 0은 생략
    for i in range(1, V+1):
        print('{} {} {} {}'.format(i, tree[i][0], tree[i][1], tree[i][2]))

import sys
sys.stdin = open('Tree_order_input.txt')
V = int(input())    # 정점 V
E = V - 1           # 트리에서의 간선은 정점 개수-1 (V-1)

# left, right, parent - 2차원 배열 준비 -> 0, 1, 2 필요
# 2차원 배열을 쓰지 않고 단일 배열을 사용하는 것도 가능
# 모두 0으로 초기화 / 1번 노드부터 시작하는 것을 표현하기 위해 V+1 (1번 ~ 13번)
tree = [[0 for _ in range(3)] for _ in range(V+1)]
"""
                1          2          3      ...
[[0, 0, 0], [2, 3, 0], [4, 0, 1], [5, 6, 1], ...]

1번 노드
- 왼쪽: 2번
- 오른쪽: 3번
- 부모: 없음

2번 노드
- 왼쪽: 4번
- 오른쪽: 없음
- 부모: 1번

3번 노드
- 왼쪽: 5번
- 오른쪽: 6번
- 부모: 1번
"""
temp = list(map(int, input().split()))  # 정점 간 연결 정보(부모-자식의 구성)
cnt = 0                                 # 방문한 정점의 개수 체크
for i in range(E):                      # 간선의 수만큼 반복을 돌며
    # parent, child -> 노드 번호를 의미(1번 ~ 13번)
    # [0, 0, 0] -> 0번째: 왼쪽 자식 / 1번째: 오른쪽 자식 / 2번째: 부모 노드
    parent, child = temp[i*2], temp[i*2+1]
    if not tree[parent][0]:
        tree[parent][0] = child
    else:
        tree[parent][1] = child
    tree[child][2] = parent

# print_tree()
# print('-------------')

print('전위 순회 : ', end='')
pre_order(1)                  # 1번 노드부터 시작
print()
# print(cnt)                    # 1을 root로 하는 서브트리의 정점 개수
# print(cnt-1)                  # 1을 root로 하는 자손의 수

print('중위 순회 : ', end='')
in_order(1)                   # 1번 노드부터 시작
print()

print('후위 순회 : ', end='')
post_order(1)                 # 1번 노드부터 시작
print()


def pre_order(n):
    global cnt
    if n:                    # 자식이 있는 정점이면
        cnt += 1
        print(n, end=' ')
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        pre_order(right[n])  # n의 오른쪽 자식으로 이동

def in_order(n):
    if n:                    # 자식이 있는 정점이면
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        print(n, end=' ')
        pre_order(right[n])  # n의 오른쪽 자식으로 이동

def post_order(n):
    if n:                    # 자식이 있는 정점이면
        pre_order(left[n])   # n의 왼쪽 자식으로 이동
        pre_order(right[n])  # n의 오른쪽 자식으로 이동
        print(n, end=' ')

import sys
sys.stdin = open('Tree_order_input.txt')
V = int(input())
E = V - 1
edge = list(map(int, input().split()))
left = [0] * (V+1)              # 부모를 인덱스로 자식 번호 저장
right = [0] * (V+1)             # 부모를 인덱스로 자식 번호 저장
par = [0] * (V+1)               # 자식을 인덱스로 부모 번호 저장

for i in range(E):
    parent, child = edge[i*2], edge[i*2+1]
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent] = child

    par[child] = parent         # (1) 조상을 찾는데 사용 & (2) root를 찾는데 사용

cnt = 0
pre_order(1)


# 조상 찾기
c = 6             # 노드 c의 조상을 찾자
while par[c]:
    print(par[c]) # 부모 번호 찍고
    c = par[c]    # 부모의 부모 찾기

# 부모가 없으면 root
root = 1
while par[root]: # root로 추정한 정점이 부모가 있으면
    root += 1
print(root)

print(cnt)      # 1을 루트로하는 서브트리의 정점 개수
print(cnt-1)    # 3의 자손 수
