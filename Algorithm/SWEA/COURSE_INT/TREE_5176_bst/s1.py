import sys
sys.stdin = open('input.txt')


def inorder_inp(node):
    global num
    if node < N + 1:
        inorder_inp(node * 2)
        tree[node] = num
        num += 1
        inorder_inp(node * 2 + 1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())  # node cnt
    tree = [0 for _ in range(N + 1)]

    num = 1
    inorder_inp(1)

    root_num = tree[1]
    goal = tree[int(N/2)]
    print('#{} {} {}'.format(tc, root_num, goal))

