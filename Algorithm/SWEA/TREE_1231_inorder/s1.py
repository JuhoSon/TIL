import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node:
        inorder(tree[node][1])
        print(tree[node][0], end='')
        inorder(tree[node][2])


T = 10
for tc in range(1, T+1):
    node_cnt = int(input())
    tree = [[0, 0, 0] for _ in range(node_cnt + 1)]
    for _ in range(node_cnt):
        tmp = input().split()
        node_idx = int(tmp[0])
        row = tmp[1:]

        for idx, info in enumerate(row):
            if idx == 0:  # node index
                tree[node_idx][idx] = info
            else:  # children
                info = int(info)
                tree[node_idx][idx] = info


    print('#{} '.format(tc, ), end='')
    inorder(1)
    print()


