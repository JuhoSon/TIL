import sys
sys.stdin = open('input.txt')


def node_sum(N):
    if not tree[N]:  # tree[N] == 0
        left_sum = node_sum(N*2) if N*2 < len(tree) else 0
        right_sum = node_sum(N*2+1) if N*2+1 < len(tree) else 0
        return left_sum + right_sum
    else:
        return tree[N]


T = int(input())
for tc in range(1, T+1):
    # init
    N, M, L = map(int, input().split())  # node cnt N, left node cnt M, goal node L
    tree = [0 for _ in range(N + 1)]

    # tree input
    for _ in range(M):
        leaf_idx, num = map(int, input().split())
        tree[leaf_idx] = num

    # calculate sum
    s = node_sum(L)

    print('#{} {}'.format(tc, s))

