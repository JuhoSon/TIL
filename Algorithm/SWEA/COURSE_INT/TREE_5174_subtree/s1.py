import sys
sys.stdin = open('input.txt')


def subtree(N):
    sub_node_cnt = 1
    stack = []
    # init
    if sum(tree[N]) != 0:
        for child in tree[N]:
            if child != 0:
                stack.append(child)
                sub_node_cnt += 1
    while stack:  # until no child
        cur_idx = stack.pop()
        for child in tree[cur_idx]:
            if child != 0:
                stack.append(child)
                sub_node_cnt += 1
    return sub_node_cnt


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())  # whole edge count E, goal node index N
    V = E + 1  # vertex = edge + 1 (binary tree)
    tree_inp = list(map(int, input().split()))  # [partent_idx1, child_idx1, parent_idx2, child_idx2, ...]
    tree = [[0, 0] for _ in range(V + 1)]  # padding on 0 index

    for idx in range(E):
        p = tree_inp[idx * 2]  # parent node index
        c = tree_inp[idx * 2 + 1]  # child node index
        LEFT_IDX = 0
        RIGHT_IDX = 1
        if tree[p][LEFT_IDX] == 0:  # blank
            tree[p][LEFT_IDX] = c
        else:
            tree[p][RIGHT_IDX] = c



    print('#{} {}'.format(tc, subtree(N)))

